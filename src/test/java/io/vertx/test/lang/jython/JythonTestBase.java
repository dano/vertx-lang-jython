package io.vertx.test.lang.jython;

import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.concurrent.TimeUnit;

import org.junit.Assert;

/**
 * @author <a href="http://tfox.org">Tim Fox</a>
 */
public abstract class JythonTestBase {

  protected String getMethodName() {
    return Thread.currentThread().getStackTrace()[3].getMethodName();
  }

  protected abstract String getTestFile();

  protected void runTest() throws Exception {
    JythonRunner runner = new JythonRunner();
    runner.run(getTestFile(), getMethodName());
  }
}
