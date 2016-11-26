package io.vertx.test.lang.jython;

import org.junit.Test;

/**
 * @author <a href="mailto:julien@julienviet.com">Julien Viet</a>
 */
public class GenericsTCKTest extends JythonTestBase {

  @Override
  protected String getTestFile() {
    return "generics_tck_test.py";
  }

  @Test
  public void testMethodWithBasicParameterizedReturn() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithHandlerBasicParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultBasicParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithFunctionParamBasicParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithJsonParameterizedReturn() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithHandlerJsonParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultJsonParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithFunctionParamJsonParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithDataObjectParameterizedReturn() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithHandlerDataObjectParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultDataObjectParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithFunctionParamDataObjectParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithEnumParameterizedReturn() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithHandlerEnumParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultEnumParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithFunctionParamEnumParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithUserTypeParameterizedReturn() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithHandlerUserTypeParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultUserTypeParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithFunctionParamUserTypeParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithClassTypeParameterizedReturn() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithHandlerClassTypeParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultClassTypeParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithFunctionParamClassTypeParameterized() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithClassTypeParam() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithClassTypeReturn() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithClassTypeHandler() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithClassTypeHandlerAsyncResult() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithClassTypeFunctionParam() throws Exception {
    runTest();
  }

  @Test
  public void testMethodWithClassTypeFunctionReturn() throws Exception {
    runTest();
  }

  @Test
  public void testInterfaceWithStringArg() throws Exception {
    runTest();
  }

  @Test
  public void testInterfaceWithVariableArg() throws Exception {
    runTest();
  }

  @Test
  public void testInterfaceWithApiArg() throws Exception {
    runTest();
  }

}
