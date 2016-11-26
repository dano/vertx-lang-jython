package io.vertx.test.lang.jython;

/**
 * @author <a href="http://tfox.org">Tim Fox</a>
 */
public abstract class JythonTestBase {

  protected String getMethodName() {
    return Thread.currentThread().getStackTrace()[3].getMethodName();
  }

  protected abstract String getTestFile();

  protected void runTest(String method) {
    JythonRunner runner = new JythonRunner();
    try {
      runner.run(getTestFile(), method);
    } catch (Exception e) {
      throw new AssertionError(e);
    }
  }

  protected void runTest() {
    runTest(getMethodName());
  }
}
