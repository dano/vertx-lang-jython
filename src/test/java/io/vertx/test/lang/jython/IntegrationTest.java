package io.vertx.test.lang.jython;

import org.junit.Test;

/**
 * @author <a href="mailto:julien@julienviet.com">Julien Viet</a>
 */
public class IntegrationTest extends JythonTestBase {

  @Override
  protected String getTestFile() {
    return "integration_test.py";
  }

  @Test
  public void testMultiMapNames() {
    runTest("test_multi_map_names");
  }
}
