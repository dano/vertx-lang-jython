import re
import sys
import unittest

from testmodel_jython.testmodel.test_interface import TestInterface
from testmodel_jython.testmodel.refed_interface1 import RefedInterface1
from testmodel_jython.testmodel.refed_interface2 import RefedInterface2
from testmodel_jython.testmodel.super_interface1 import SuperInterface1
from testmodel_jython.testmodel.super_interface2 import SuperInterface2
from testmodel_jython.testmodel.generic_refed_interface import GenericRefedInterface
from testmodel_jython.testmodel.factory import Factory
from acme_jython.pkg.my_interface import MyInterface
from acme_jython.sub.sub_interface import SubInterface

from vertx_jython import util

import io.vertx.codegen.testmodel.TestInterfaceImpl
import io.vertx.codegen.testmodel.RefedInterface1Impl

obj = TestInterface(io.vertx.codegen.testmodel.TestInterfaceImpl())
refed_obj = RefedInterface1(io.vertx.codegen.testmodel.RefedInterface1Impl())
refed_obj2 = RefedInterface1(io.vertx.codegen.testmodel.RefedInterface1Impl())

class TestAPI(unittest.TestCase):

    #def testNullDataObjectParam(self):
        #data_object = {}
        #obj.method_with_null_data_object_param(**data_object)

    def testMethodWithHandlerListNullJsonObject(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(type(val), list)
            self.assertEqual(len(val), 1)
            self.assertIsNone(val[0])
            dct['count'] += 1
        obj.method_with_handler_list_null_json_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultListNullJsonObject(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), list)
            self.assertEqual(len(val), 1)
            self.assertIsNone(val[0])
            dct['count'] += 1
        obj.method_with_handler_async_result_list_null_json_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerSetNullJsonObject(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(type(val), set)
            self.assertEqual(len(val), 1)
            for elt in val:
                self.assertIsNone(None)
            dct['count'] += 1
        obj.method_with_handler_set_null_json_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultSetNullJsonObject(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), set)
            self.assertEqual(len(val), 1)
            for elt in val:
                self.assertIsNone(None)
            dct['count'] += 1
        obj.method_with_handler_async_result_set_null_json_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerListNullJsonArray(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(type(val), list)
            self.assertEqual(len(val), 1)
            self.assertIsNone(val[0])
            dct['count'] += 1
        obj.method_with_handler_list_null_json_array(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultListNullJsonArray(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), list)
            self.assertEqual(len(val), 1)
            self.assertIsNone(val[0])
            dct['count'] += 1
        obj.method_with_handler_async_result_list_null_json_array(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerSetNullJsonArray(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(type(val), set)
            self.assertEqual(len(val), 1)
            for elt in val:
                self.assertIsNone(elt)
            dct['count'] += 1
        obj.method_with_handler_set_null_json_array(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultSetNullJsonArray(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), set)
            self.assertEqual(len(val), 1)
            for elt in val:
                self.assertIsNone(elt)
            dct['count'] += 1
        obj.method_with_handler_async_result_set_null_json_array(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerListNullDataObject(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(type(val), list)
            self.assertIsNone(val[0])
            dct['count'] += 1
        obj.method_with_handler_list_null_data_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerSetNullDataObject(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(val, set([None]))
            dct['count'] += 1
        obj.method_with_handler_set_null_data_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultListNullDataObject(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(val, [None])
            dct['count'] += 1
        obj.method_with_handler_async_result_list_null_data_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultSetNullDataObject(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(val, set([None]))
            dct['count'] += 1
        obj.method_with_handler_async_result_set_null_data_object(handler)
        self.assertEqual(dct['count'], 1)

    def testNullJsonHandlerParams(self):
        dct = dict(count=0)
        def obj_handler(val):
            self.assertIsNone(val)
            dct['count'] += 1
        def arr_handler(val):
            self.assertIsNone(val)
            dct['count'] += 1
        obj.method_with_handler_null_json(obj_handler, arr_handler)
        self.assertEqual(dct['count'], 2)

    def testMapNullReturn(self):
        map = obj.method_with_null_map_return()
        self.assertIsNone(map)

# if __name__ == "__main__":
#     unittest.main()
