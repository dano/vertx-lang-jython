package io.vertx.test.lang.jython;

import org.junit.Test;

/**
 * @author <a href="mailto:julien@julienviet.com">Julien Viet</a>
 */
public class CollectionTCKTest extends JythonTestBase {

  @Override
  protected String getTestFile() {
    return "collection_tck_test.py";
  }

  @Override
  protected String getTestClass() {
    return "TestAPI";
  }

  @Test
  public void testMethodWithHandlerListAndSet() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultListAndSet() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerListVertxGen() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerListAbstractVertxGen() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultListVertxGen() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultListAbstractVertxGen() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerSetVertxGen() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerSetAbstractVertxGen() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultSetVertxGen() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultSetAbstractVertxGen() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerListJsonObject() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerListComplexJsonObject() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultListJsonObject() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultListComplexJsonObject() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerSetJsonObject() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerSetComplexJsonObject() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultSetJsonObject() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultSetComplexJsonObject() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerListJsonArray() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultListJsonArray() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultListComplexJsonArray() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerSetJsonArray() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerSetComplexJsonArray() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultSetJsonArray() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerListComplexJsonArray() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerListDataObject() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerSetDataObject() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultSetComplexJsonArray() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultListDataObject() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultSetDataObject() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerListEnum() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerSetEnum() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultListEnum() {
    runTest();
  }

  @Test
  public void testMethodWithHandlerAsyncResultSetEnum() {
    runTest();
  }

  @Test
  public void testMapComplexJsonArrayReturn() {
    runTest();
  }

  @Test
  public void testMapReturn() {
    runTest();
  }

  @Test
  public void testMapStringReturn() {
    runTest();
  }

  @Test
  public void testMapJsonObjectReturn() {
    runTest();
  }

  @Test
  public void testMapComplexJsonObjectReturn() {
    runTest();
  }

  @Test
  public void testMapJsonArrayReturn() {
    runTest();
  }

  @Test
  public void testMapIntegerReturn() {
    runTest();
  }

  @Test
  public void testMapShortReturn() {
    runTest();
  }

  @Test
  public void testMapByteReturn() {
    runTest();
  }

  @Test
  public void testMapCharacterReturn() {
    runTest();
  }

  @Test
  public void testMapBooleanReturn() {
    runTest();
  }

  @Test
  public void testMapFloatReturn() {
    runTest();
  }

  @Test
  public void testMapDoubleReturn() {
    runTest();
  }

  @Test
  public void testMapLongReturn() {
    runTest();
  }

  @Test
  public void testListStringReturn() {
    runTest();
  }

  @Test
  public void testListLongReturn() {
    runTest();
  }

  @Test
  public void testListJsonObjectReturn() {
    runTest();
  }

  @Test
  public void testListComplexJsonObjectReturn() {
    runTest();
  }

  @Test
  public void testListJsonArrayReturn() {
    runTest();
  }

  @Test
  public void testListComplexJsonArrayReturn() {
    runTest();
  }

  @Test
  public void testListVertxGenReturn() {
    runTest();
  }

  @Test
  public void testListDataObjectReturn() {
    runTest();
  }

  @Test
  public void testListEnumReturn() {
    runTest();
  }

  @Test
  public void testSetStringReturn() {
    runTest();
  }

  @Test
  public void testSetLongReturn() {
    runTest();
  }

  @Test
  public void testSetJsonObjectReturn() {
    runTest();
  }

  @Test
  public void testSetComplexJsonObjectReturn() {
    runTest();
  }

  @Test
  public void testSetJsonArrayReturn() {
    runTest();
  }

  @Test
  public void testSetComplexJsonArrayReturn() {
    runTest();
  }

  @Test
  public void testSetVertxGenReturn() {
    runTest();
  }

  @Test
  public void testSetDataObjectReturn() {
    runTest();
  }

  @Test
  public void testSetEnumReturn() {
    runTest();
  }

  @Test
  public void testMethodWithListParams() {
    runTest();
  }

  @Test
  public void testMethodWithSetParams() {
    runTest();
  }

  @Test
  public void testMethodWithMapParams() {
    runTest();
  }

}
