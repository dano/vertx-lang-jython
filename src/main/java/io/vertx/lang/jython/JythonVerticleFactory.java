package io.vertx.lang.jython;

import org.python.core.Options;
import org.python.core.PySystemState;
import org.python.util.PythonInterpreter;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.concurrent.atomic.AtomicInteger;

import io.vertx.core.AbstractVerticle;
import io.vertx.core.Verticle;
import io.vertx.core.Vertx;
import io.vertx.core.VertxException;
import io.vertx.core.spi.VerticleFactory;

/**
 * @author <a href="https://github.com/sjhorn">Scott Horn</a>
 * @author <a href="http://tfox.org">Tim Fox</a>
 * @author <a href="https://github.com/dano">Dan O'Reilly</a>
 */
public class JythonVerticleFactory implements VerticleFactory {

  private Vertx vertx;
  private PythonInterpreter py;
  private static final AtomicInteger seq = new AtomicInteger();


  @Override
  public void init(Vertx vertx) {
    this.vertx = vertx;
    System.setProperty("python.options.internalTablesImpl","weak");
    Options.includeJavaStackInExceptions = false;
    this.py = new PythonInterpreter(null, new PySystemState());
  }

  @Override
  public String prefix() {
    return "py";
  }

  @Override
  public Verticle createVerticle(String verticleName, ClassLoader classLoader) throws Exception {
    Thread.currentThread().setContextClassLoader(classLoader);
    verticleName = VerticleFactory.removePrefix(verticleName);
    return new JythonVerticle(verticleName, classLoader);
  }

  private class JythonVerticle extends AbstractVerticle {

    private final String verticleName;
    private final ClassLoader cl;
    private String funcName;
    private StringBuilder stopFuncName;
    private StringBuilder stopFuncVar;


    private JythonVerticle(String verticleName, ClassLoader cl) {
      this.verticleName = verticleName;
      this.cl = cl;
    }

    @Override
    public void start() throws Exception {
      try (InputStream is = cl.getResourceAsStream(verticleName)) {
        if (is == null) {
          throw new IllegalArgumentException("Cannot find verticle: " + verticleName);
        }
        // We wrap the python verticle in a function so different instances don't see each others top level vars
        String genName = "__VertxInternalVert__" + seq.incrementAndGet();
        funcName = "f" + genName;
        StringBuilder sWrap = new StringBuilder("def ").append(funcName).append("():\n");
        BufferedReader br = new BufferedReader(new InputStreamReader(is));
        for (String line = br.readLine(); line != null; line = br.readLine()) {
          // Append line indented by a tab
          sWrap.append("\t").append(line).append("\n");
        }
        br.close();
        // The return value of the wrapping function is the vertx_stop function (if defined)
        sWrap.append("\tif 'vertx_stop' in locals():\n");
        sWrap.append("\t\treturn vertx_stop\n");
        sWrap.append("\telse:\n");
        sWrap.append("\t\treturn None\n");

        // And then we have to add a top level wrapper method that calls the actual vertx_stop method
        stopFuncVar = new StringBuilder("v").append(genName);
        sWrap.append(stopFuncVar).append(" = ").append(funcName).append("()\n");
        stopFuncName = new StringBuilder(funcName).append("_stop");
        sWrap.append("def ").append(stopFuncName).append("():\n");
        sWrap.append("\tif ").append(stopFuncVar).append(" is not None:\n");
        sWrap.append("\t\t").append(stopFuncVar).append("()\n");


        // We have to convert it back to an inputstream since for some reason there is no version
        // py.exec which takes a String AND a fileName - and without the filename
        // any stack traces from errors won't show the filename and be hard for the user to parse.
        try (InputStream sis = new ByteArrayInputStream(sWrap.toString().getBytes("UTF-8"))) {
          py.execfile(sis, verticleName);
        }

      } catch (Exception e) {
        funcName = null;
        stopFuncName = null;
        stopFuncVar = null;
        throw new VertxException(e);
      }
    }

    @Override
    public void stop() throws Exception {
      if (stopFuncName != null) {
        py.exec(stopFuncName.toString() + "()");
        // And delete the globals
        py.exec("del " + stopFuncVar);
        py.exec("del " + stopFuncName);
        py.exec("del " + funcName);
      }
    }
  }
}
