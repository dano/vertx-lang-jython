package io.vertx.test.lang.jython;

import org.junit.Test;

/**
 * @author <a href="mailto:julien@julienviet.com">Julien Viet</a>
 */
public class LangTest extends JythonTestBase {

  @Test
  public void testLinearOverload() {
    runTest("test_linear_overload");
  }

  @Test
  public void testMultiOverload() {
    runTest("test_multi_overload");
  }

  @Test
  public void testMultiOverloadOptionalHandler() {
    runTest("test_multi_overload_optional_handler");
  }

  @Test
  public void testMultiOverloadOptionalHandlers() {
    runTest("test_multi_overload_handlers");
  }
  @Test
  public void testMixinInheritance() {
    runTest("test_mixin_inheritance");
  }

  @Test
  public void testInclude() {
    runTest("test_include");
  }

  @Test
  public void testReservedWords() {
    runTest("test_reserved_words");
  }

  @Test
  public void testClosureCallback() {
    runTest("test_closure_callback");
  }

  @Test
  public void testOverloadWithOptions() {
    runTest("test_overload_with_options");
  }

  @Override
  protected String getTestFile() {
    return "lang_test.py";
  }

}
