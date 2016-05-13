package io.vertx.test.lang.jython;

import org.python.core.Options;
import org.python.core.PySystemState;
import org.python.util.PythonInterpreter;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.io.InputStreamReader;

import io.vertx.core.Vertx;
import io.vertx.core.VertxException;

/**
 * @author <a href="https://github.com/dano">Dan O'Reilly</a>
 */
public class JythonRunner {

  public static void main(String[] args) {
  }

  public Vertx getVertx() {
    return Vertx.vertx();
  }

  public int run(String scriptName, String testName) throws Exception {
    return run(scriptName, testName, true, true);
  }

  public int run(String scriptName, String testName, boolean provideRequire, 
                 boolean provideConsole) throws Exception {
    System.setProperty("python.options.internalTablesImpl","weak");
    Options.includeJavaStackInExceptions = false;
    PythonInterpreter py = new PythonInterpreter(null, new PySystemState());
    try (InputStream is = this.getClass().getClassLoader().getResourceAsStream(scriptName)) {
      if (is == null) {
        throw new IllegalArgumentException("Cannot find script: " + scriptName);
      }
      // We wrap the python script in a function so different instances don't see each others top level vars
      String genName = "__VertxInternalVert__" + 1;
      String funcName = "f" + genName;
      StringBuilder sWrap = new StringBuilder();
//      StringBuilder sWrap = new StringBuilder("def ").append(funcName).append("():\n");
      BufferedReader br = new BufferedReader(new InputStreamReader(is));
      for (String line = br.readLine(); line != null; line = br.readLine()) {
        // Append line indented by a tab
        sWrap.append(line).append("\n");
      }
      br.close();
      sWrap.append("\n").append("TestAPI('").append(testName).append("')")
      .append(".debug()");

      // We have to convert it back to an inputstream since for some reason there is no version
      // py.exec which takes a String AND a fileName - and without the filename
      // any stack traces from errors won't show the filename and be hard for the user to parse.
//      System.out.println(sWrap.toString());
      try (InputStream sis = new ByteArrayInputStream(sWrap.toString().getBytes("UTF-8"))) {
        py.execfile(sis, scriptName);
      }

    } catch (Exception e) {
      throw new VertxException(e);
    }
    return 0;
  }
}
