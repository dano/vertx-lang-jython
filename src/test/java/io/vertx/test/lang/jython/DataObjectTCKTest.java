package io.vertx.test.lang.jython;

import org.junit.Test;

/**
 * @author <a href="mailto:julien@julienviet.com">Julien Viet</a>
 */
public class DataObjectTCKTest extends JythonTestBase {

  @Override
  protected String getTestFile() {
    return "data_object_tck_test.py";
  }

  @Test
  public void testMethodWithOnlyJsonObjectConstructorDataObject() {
    runTest();
  }

}
