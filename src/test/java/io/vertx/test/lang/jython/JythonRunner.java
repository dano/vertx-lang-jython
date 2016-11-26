package io.vertx.test.lang.jython;

import org.python.core.Options;
import org.python.core.PySystemState;
import org.python.util.PythonInterpreter;

import java.io.BufferedReader;
import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.io.InputStreamReader;

import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;

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

  public void run(String scriptName, String className, String testName) throws Exception {
    System.setProperty("python.options.internalTablesImpl","weak");
    Options.includeJavaStackInExceptions = false;
    PythonInterpreter py = new PythonInterpreter(null, new PySystemState());
    String moduleName = getModuleName(scriptName);
    py.exec("import " + moduleName);
    if (className != null) {
      py.exec(moduleName + "." + className + "('" + testName + "').debug()");
    } else {
      py.exec(moduleName + "." + testName + "()");
    }
  }

  private String getModuleName(String scriptName) {
    return scriptName.substring(0, scriptName.length() -3);
  }
}
