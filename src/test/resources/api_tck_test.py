import unittest

import io.vertx.codegen.testmodel.RefedInterface1Impl

from acme_jython.pkg.my_interface import MyInterface
from testmodel_jython.testmodel.factory import Factory
from testmodel_jython.testmodel.generic_refed_interface import GenericRefedInterface
from testmodel_jython.testmodel.refed_interface1 import RefedInterface1
from testmodel_jython.testmodel.refed_interface2 import RefedInterface2
from testmodel_jython.testmodel.super_interface1 import SuperInterface1
from testmodel_jython.testmodel.super_interface2 import SuperInterface2
from testmodel_jython.testmodel.test_interface import TestInterface

obj = TestInterface(io.vertx.codegen.testmodel.TestInterfaceImpl())
refed_obj = RefedInterface1(io.vertx.codegen.testmodel.RefedInterface1Impl())
refed_obj2 = RefedInterface1(io.vertx.codegen.testmodel.RefedInterface1Impl())


class TestTCKAPI(unittest.TestCase):

    def testMethodWithBasicParams(self):
        obj.method_with_basic_params(123, 12345, 1234567, 1265615234, 12.345, 12.34566, True, 88, 'foobar')

    def testMethodWithBasicBoxedParams(self):
        obj.method_with_basic_boxed_params(123, 12345, 1234567, 1265615234, 12.345, 12.34566, True, 88)

    def testMethodWithHandlerBasicTypes(self):
        dct = dict(count=0)

        def byte_handler(b):
            self.assertEqual(type(b), int)
            self.assertEqual(123, b)
            dct['count'] += 1

        def short_handler(s):
            self.assertEqual(type(s), int)
            self.assertEqual(12345, s)
            dct['count'] += 1

        def int_handler(i):
            self.assertEqual(type(i), int)
            self.assertEqual(1234567, i)
            dct['count'] += 1

        def long_handler(l):
            self.assertEqual(type(l), long)
            self.assertEqual(1265615234, l)
            dct['count'] += 1

        def float_handler(f):
            self.assertEqual(type(f), float)
            self.assertAlmostEqual(12.345, f)
            dct['count'] += 1

        def double_handler(d):
            self.assertEqual(type(d), float)
            self.assertEqual(12.34566, d)
            dct['count'] += 1

        def boolean_handler(b):
            self.assertEqual(type(b), bool)
            self.assertTrue(b)
            dct['count'] += 1

        def char_handler(c):
            self.assertEqual(type(c), unicode)
            self.assertEqual('X', c)
            dct['count'] += 1

        def string_handler(s):
            self.assertEqual(type(s), unicode)
            self.assertEqual('quux!', s)
            dct['count'] += 1

        obj.method_with_handler_basic_types(byte_handler, short_handler,
                                            int_handler, long_handler,
                                            float_handler, double_handler,
                                            boolean_handler, char_handler,
                                            string_handler)
        self.assertEqual(dct['count'], 9)

    def testMethodWithHandlerAsyncResultBasicTypes(self):
        dct = dict(count=0)

        def byte_handler(b, err):
            self.assertEqual(type(b), int)
            self.assertEqual(123, b)
            self.assertIsNone(err)
            dct['count'] += 1

        def short_handler(s, err):
            self.assertEqual(type(s), int)
            self.assertEqual(12345, s)
            self.assertIsNone(err)
            dct['count'] += 1

        def int_handler(i, err):
            self.assertEqual(type(i), int)
            self.assertEqual(1234567, i)
            self.assertIsNone(err)
            dct['count'] += 1

        def long_handler(l, err):
            self.assertEqual(type(l), long)
            self.assertEqual(1265615234, l)
            self.assertIsNone(err)
            dct['count'] += 1

        def float_handler(f, err):
            self.assertEqual(type(f), float)
            self.assertAlmostEqual(12.345, f)
            self.assertIsNone(err)
            dct['count'] += 1

        def double_handler(d, err):
            self.assertEqual(type(d), float)
            self.assertAlmostEqual(12.34566, d)
            self.assertIsNone(err)
            dct['count'] += 1

        def boolean_handler(b, err):
            self.assertEqual(type(b), bool)
            self.assertTrue(b)
            self.assertIsNone(err)
            dct['count'] += 1

        def char_handler(c, err):
            self.assertEqual(type(c), unicode)
            self.assertEqual('X', c)
            self.assertIsNone(err)
            dct['count'] += 1

        def string_handler(s, err):
            self.assertEqual(type(s), unicode)
            self.assertEqual('quux!', s)
            self.assertIsNone(err)
            dct['count'] += 1

        obj.method_with_handler_async_result_byte(False, byte_handler)
        obj.method_with_handler_async_result_short(False, short_handler)
        obj.method_with_handler_async_result_integer(False, int_handler)
        obj.method_with_handler_async_result_long(False, long_handler)
        obj.method_with_handler_async_result_float(False, float_handler)
        obj.method_with_handler_async_result_double(False, double_handler)
        obj.method_with_handler_async_result_boolean(False, boolean_handler)
        obj.method_with_handler_async_result_character(False, char_handler)
        obj.method_with_handler_async_result_string(False, string_handler)
        self.assertEqual(dct['count'], 9)

    def testMethodWithUserTypes(self):
        refed_obj.set_string('aardvarks')
        obj.method_with_user_types(refed_obj)

    def testObjectParam(self):
        obj.method_with_object_param('null', None)
        obj.method_with_object_param('string', 'wibble')
        obj.method_with_object_param('True', True)
        obj.method_with_object_param('False', False)
        obj.method_with_object_param('long', 123)
        obj.method_with_object_param('double', 123.456)
        json_obj = {"foo" : "hello", "bar" : 123}
        obj.method_with_object_param('JsonObject', json_obj)
        json_arr = ["foo", "bar", "wib"]
        obj.method_with_object_param('JsonArray', json_arr)

    def testDataObjectParam(self):
        data_object = {"foo" : "hello", "bar" : 123, "wibble" : 1.23}
        obj.method_with_data_object_param(**data_object)

    def testMethodWithHandlerDataObject(self):
        dct = dict(count=0)
        def handler(option):
            self.assertEqual("foo", option['foo'])
            self.assertEqual(123, option['bar'])
            self.assertEqual(0.0, option['wibble'])
            dct['count'] += 1
        obj.method_with_handler_data_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultDataObject(self):
        dct = dict(count=0)
        def handler(option, err):
            self.assertIsNone(err)
            self.assertEqual("foo", option['foo'])
            self.assertEqual(123, option['bar'])
            self.assertEqual(0.0, option['wibble'])
            dct['count'] += 1
        obj.method_with_handler_async_result_data_object(False, handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultDataObjectFails(self):
        dct = dict(count=0)
        def handler(option, err):
            self.assertIsNone(option)
            self.assertIsNotNone(err)
            self.assertEqual("foobar!", str(err))
            dct['count'] += 1
        obj.method_with_handler_async_result_data_object(True, handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerStringReturn(self):
        handler = obj.method_with_handler_string_return("the-result")
        handler.call("the-result")
        failed = False
        try:
            handler.call("the-result")
        except Exception:
            failed = True
        self.assertEqual(True, failed)

    def testMethodWithHandlerGenericReturn(self):
        d = {'result': None}
        def h(val):
            d['result'] = val
        handler = obj.method_with_handler_generic_return(h)
        handler.call("the-result")
        self.assertEqual(d['result'], "the-result")
        handler.call(obj)
        self.assertEqual(d['result'], obj)

    def testMethodWithHandlerVertxGenReturn(self):
        handler = obj.method_with_handler_vertx_gen_return("the-result")
        refed_obj.set_string('the-result')
        handler.call(refed_obj)

    def testMethodWithHandlerAsyncResultStringReturn(self):
        succeeding_handler = obj.method_with_handler_async_result_string_return("the-result", False)
        succeeding_handler.call(None, "the-result")
        failed = False
        try:
            succeeding_handler.call(None)
        except Exception:
            failed = True
        self.assertEqual(failed, True)
        failing_handler = obj.method_with_handler_async_result_string_return("an-error", True)
        failing_handler.call("an-error")
        failed = False
        try:
            failing_handler.call(None, "unexpected")
        except Exception:
            failed = True
        self.assertEquals(failed, True)

    def testMethodWithHandlerAsyncResultGenericReturn(self):
        dct = {"result": None}
        def h(err, val):
            if err is None:
                dct['result'] = val
            else:
                dct['result'] = err

        succeeding_handler = obj.method_with_handler_async_result_generic_return(h)
        succeeding_handler.call(None, "the-result")
        self.assertEquals(dct['result'], "the-result")
        succeeding_handler.call(None, obj)
        self.assertEquals(dct['result'], obj)

    def testMethodWithHandlerAsyncResultVertxGenReturn(self):
        handler = obj.method_with_handler_async_result_vertx_gen_return("the-async-result", False)
        refed_obj.set_string('the-async-result')
        handler.call(None, refed_obj)
        handler = obj.method_with_handler_async_result_vertx_gen_return("the-async-failure", True)
        handler.call("the-async-failure", None)

    def testMethodWithHandlerUserTypes(self):
        dct = {'count': 0}

        def h(val):
            self.assertEquals(type(val), RefedInterface1)
            self.assertEquals(val.get_string, 'echidnas')
            dct['count'] += 1

        obj.method_with_handler_user_types(h)
        self.assertEquals(1, dct['count'])

    def testMethodWithHandlerAsyncResultUserTypes(self):
        dct = {'count': 0}

        def h(err, val):
            self.assertIsNone(err)
            self.assertEquals(type(val), RefedInterface1)
            self.assertEquals(val.get_string, 'cheetahs')
            dct['count'] += 1

        obj.method_with_handler_async_result_user_types(h)
        self.assertEquals(1, dct['count'])

    def testMethodWithConcreteHandlerUserTypeSubtype(self):
        dct = {'count': 0}

        def h(refed_obj):
            self.assertEquals(type(refed_obj), RefedInterface1)
            self.assertEquals(refed_obj.get_string, 'echidnas')
            dct['count'] += 1

        arg = Factory.create_concrete_handler_user_type(h)
        obj.method_with_concrete_handler_user_type_subtype(arg)
        self.assertEquals(1, dct['count'])

    def testMethodWithAbstractHandlerUserTypeSubtype(self):
        dct = {'count': 0}

        def h(refed_obj):
            self.assertEquals(type(refed_obj), RefedInterface1)
            self.assertEquals(refed_obj.get_string, 'echidnas')
            dct['count'] += 1

        arg = Factory.create_abstract_handler_user_type(h)
        obj.method_with_abstract_handler_user_type_subtype(arg)
        self.assertEquals(1, dct['count'])

    def testMethodWithConcreteHandlerUserTypeSubtypeExtension(self):
        dct = {'count': 0}

        def h(refed_obj):
            self.assertEquals(type(refed_obj), RefedInterface1)
            self.assertEquals(refed_obj.get_string, 'echidnas')
            dct['count'] += 1

        arg = Factory.create_concrete_handler_user_type_extension(h)
        obj.method_with_concrete_handler_user_type_subtype_extension(arg)
        self.assertEquals(1, dct['count'])

    def testMethodWithHandlerVoid(self):
        dct = {'count': 0}

        def h(val):
            self.assertIsNone(val)
            dct['count'] += 1

        obj.method_with_handler_void(h)
        self.assertEquals(1, dct['count'])

    def testMethodWithHandlerAsyncResultVoid(self):
        dct = {'count': 0}

        def h(err):
            self.assertIsNone(err)
            dct['count'] += 1

        obj.method_with_handler_async_result_void(False, h)
        self.assertEquals(1, dct['count'])

    def testMethodWithHandlerAsyncResultVoidFails(self):
        dct = {'count': 0}

        def h(err):
            self.assertIsNotNone(err)
            self.assertEquals(err.message, 'foo!')
            dct['count'] += 1

        obj.method_with_handler_async_result_void(True, h)
        self.assertEquals(1, dct['count'])

    def testMethodWithHandlerThrowable(self):
        dct = {'count': 0}

        def h (err):
            self.assertIsNotNone(err)
            self.assertEquals(err.message, 'cheese!')
            dct['count'] += 1

        obj.method_with_handler_throwable(h)
        self.assertEquals(1, dct['count'])

    def testMethodWithHandlerGenericUserType(self):
        def run_test(value, assertion):
            dct = dict(count=0)

            def handler(obj):
                self.assertIsNotNone(obj)
                self.assertEqual(type(obj), GenericRefedInterface)
                assertion(obj.get_value())
                dct['count'] += 1

            obj.method_with_handler_generic_user_type(value, handler)
            self.assertEqual(dct['count'], 1)

        run_test('string_value', lambda x: self.assertEqual(x, 'string_value'))
        run_test({'key' : 'key_value'}, lambda x: self.assertEqual(x, {'key' : 'key_value'}))
        run_test(['foo', 'bar', 'juu'], lambda x: self.assertEqual(x, ['foo', 'bar', 'juu']))

    def testMethodWithHandlerAsyncResultGenericUserType(self):
        def run_test(value, assertion):
            dct = dict(count=0)

            def handler(obj, err):
                self.assertIsNone(err)
                self.assertIsNotNone(obj)
                self.assertEqual(type(obj), GenericRefedInterface)
                assertion(obj.get_value())
                dct['count'] += 1

            obj.method_with_handler_async_result_generic_user_type(value, handler)
            self.assertEqual(dct['count'], 1)

        run_test('string_value', lambda x: self.assertEqual(x, 'string_value'))
        run_test({'key' : 'key_value'}, lambda x: self.assertEqual(x, {'key' : 'key_value'}))
        run_test(['foo', 'bar', 'juu'], lambda x: self.assertEqual(x, ['foo', 'bar', 'juu']))

    def testMethodWithGenericParam(self):
        obj.method_with_generic_param('String', 'foo')
        obj.method_with_generic_param('JsonObject', {'foo' : 'hello','bar' : 123})
        obj.method_with_generic_param('JsonArray', ['foo', 'bar', 'wib'])

    def testMethodWithGenericHandler(self):
        dct = dict(count=0)

        def str_handler(val):
            self.assertEqual(type(val), unicode)
            self.assertEqual(val, 'foo')
            dct['count'] += 1

        obj.method_with_generic_handler('String', str_handler)
        self.assertEqual(dct['count'], 1)

        dct = dict(count=0)

        def do_handler(val):
            self.assertEqual(val.getString(), 'bar')
            dct['count'] += 1

        obj.method_with_generic_handler('Ref', do_handler)
        self.assertEqual(dct['count'], 1)

        dct = dict(count=0)

        def json_obj_handler(val):
            self.assertEqual(type(val), dict)
            self.assertEqual(val, {'foo' : 'hello', 'bar' : 123})
            dct['count'] += 1

        obj.method_with_generic_handler('JsonObject', json_obj_handler)
        self.assertEqual(dct['count'], 1)

        dct = dict(count=0)

        def json_arr_handler(val):
            self.assertEqual(type(val), list)
            self.assertEqual(val, ['foo', 'bar', 'wib'])
            dct['count'] += 1

        obj.method_with_generic_handler('JsonArray', json_arr_handler)
        self.assertEqual(dct['count'], 1)

        dct = dict(count=0)

        def json_obj_complex_handler(val):
            self.assertEqual(type(val), dict)
            self.assertEqual(val, {'outer' : {'foo' : 'hello'},
                                   'bar' : ['this', 'that']})
            dct['count'] += 1

        obj.method_with_generic_handler('JsonObjectComplex', json_obj_complex_handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithGenericHandlerAsyncResult(self):
        dct = dict(count=0)

        def str_handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), unicode)
            self.assertEqual(val, 'foo')
            dct['count'] += 1

        obj.method_with_generic_handler_async_result('String', str_handler)
        self.assertEqual(dct['count'], 1)

        dct = dict(count=0)

        def do_handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(val.getString(), 'bar')
            dct['count'] += 1

        obj.method_with_generic_handler_async_result('Ref', do_handler)
        self.assertEqual(dct['count'], 1)

        dct = dict(count=0)

        def json_obj_handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), dict)
            self.assertEqual(val, {'foo' : 'hello', 'bar' : 123})
            dct['count'] += 1

        obj.method_with_generic_handler_async_result('JsonObject', json_obj_handler)
        self.assertEqual(dct['count'], 1)

        dct = dict(count=0)

        def json_arr_handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), list)
            self.assertEqual(val, ['foo', 'bar', 'wib'])
            dct['count'] += 1

        obj.method_with_generic_handler_async_result('JsonArray', json_arr_handler)
        self.assertEqual(dct['count'], 1)

        dct = dict(count=0)

        def json_obj_complex_handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), dict)
            self.assertEqual(val, {'outer' : {'foo' : 'hello'},
                                   'bar' : ['this', 'that']})
            dct['count'] += 1

        obj.method_with_generic_handler_async_result('JsonObjectComplex', json_obj_complex_handler)
        self.assertEqual(dct['count'], 1)

    def testBasicReturns(self):
        ret = obj.method_with_byte_return()
        self.assertEqual(type(ret), int)
        self.assertEqual(ret, 123)
        ret = obj.method_with_short_return()
        self.assertEqual(type(ret), int)
        self.assertEqual(ret, 12345)
        ret = obj.method_with_int_return()
        self.assertEqual(type(ret), int)
        self.assertEqual(ret, 12345464)
        ret = obj.method_with_long_return()
        self.assertEqual(type(ret), long)
        self.assertEqual(ret, 65675123)
        ret = obj.method_with_float_return()
        self.assertEqual(type(ret), float)
        self.assertAlmostEquals(ret, 1.23)
        ret = obj.method_with_double_return()
        self.assertEqual(type(ret), float)
        self.assertAlmostEqual(ret, 3.34535)
        ret = obj.method_with_boolean_return()
        self.assertEqual(type(ret), bool)
        self.assertEqual(ret, True)
        ret = obj.method_with_char_return()
        self.assertEqual(type(ret), str)
        self.assertEqual(ret, 'Y')
        ret = obj.method_with_string_return()
        self.assertEqual(type(ret), unicode)
        self.assertEqual(ret, 'orangutan')

    def testVertxGenReturn(self):
        ret = obj.method_with_vertx_gen_return()
        self.assertEqual(type(ret), RefedInterface1)
        self.assertEqual(ret.get_string(), 'chaffinch')

    def testVertxGenNullReturn(self):
        ret = obj.method_with_vertx_gen_null_return()
        self.assertIsNone(ret)

    def testAbstractVertxGenReturn(self):
        ret = obj.method_with_abstract_vertx_gen_return()
        self.assertIsInstance(ret, RefedInterface2)
        self.assertEqual(ret.get_string(), 'abstractchaffinch')

    def testDataObjectReturn(self):
        ret = obj.method_with_data_object_return()
        self.assertEquals(ret, {'foo': 'foo', 'bar': 123, 'wibble': 0.0})

    def testDataObjectNullReturn(self):
        ret = obj.method_with_data_object_null_return()
        self.assertEquals(None, ret)

    def testOverloadedMethods(self):
        refed_obj.set_string('dog')
        dct = dict(called=False)
        ret = obj.overloaded_method('cat', refed=refed_obj)
        self.assertEqual(ret, 'meth1')
        def handler(animal):
            self.assertEqual(animal, 'giraffe')
            dct['called'] = True
        ret = obj.overloaded_method('cat', refed=refed_obj, period=12345,
                                    handler=handler)
        self.assertEqual(ret, 'meth2')
        self.assertEqual(dct['called'], True)
        dct = dict(called=False)

        def handler2(animal):
            dct['called'] = True

        ret = obj.overloaded_method('cat', handler=handler2)
        self.assertEqual(ret, 'meth3')
        self.assertEqual(dct['called'], True)
        dct = dict(called=False)
        ret = obj.overloaded_method('cat', refed=refed_obj, handler=handler)
        self.assertEqual(ret, 'meth4')
        self.assertEqual(dct['called'], True)
        self.assertRaises(TypeError, obj.overloaded_method, 'cat')
        self.assertRaises(TypeError, obj.overloaded_method, 'cat', refed=refed_obj,
                          period=12345)
        self.assertRaises(TypeError, obj.overloaded_method)

    def testSuperInterfaces(self):
        obj.super_method_with_basic_params(123, 12345, 1234567, 1265615234, 12.345, 12.34566, True, 88, 'foobar')
        self.assertIsInstance(obj, SuperInterface1)
        obj.other_super_method_with_basic_params(123, 12345, 1234567, 1265615234, 12.345, 12.34566, True, 88, 'foobar')
        self.assertIsInstance(obj, SuperInterface2)

    def testMethodWithGenericReturn(self):
        ret = obj.method_with_generic_return('JsonObject')
        self.assertEqual(type(ret), dict)
        self.assertEqual(ret, {'foo' : 'hello', 'bar' : 123})
        ret = obj.method_with_generic_return('JsonArray')
        self.assertIsInstance(ret, list)
        self.assertEqual(ret, ['foo', 'bar', 'wib'])

    def testFluentMethod(self):
        ret = obj.fluent_method('bar')
        self.assertEqual(ret, obj)

    def testStaticFactoryMethod(self):
        ret = TestInterface.static_factory_method('bar')
        self.assertEqual(type(ret), RefedInterface1)
        self.assertEqual(ret.get_string(), 'bar')

    def testMethodWithCachedReturn(self):
        ret = obj.method_with_cached_return('bar')
        ret2 = obj.method_with_cached_return('bar')
        self.assertEqual(ret, ret2)
        ret3 = obj.method_with_cached_return('bar')
        self.assertEqual(ret, ret3)
        self.assertEqual(ret.get_string(), 'bar')
        self.assertEqual(ret2.get_string(), 'bar')
        self.assertEqual(ret3.get_string(), 'bar')
        ret.set_string('foo')
        self.assertEqual(ret2.get_string(), 'foo')
        self.assertEqual(ret3.get_string(), 'foo')

    def testMethodWithCachedListReturn(self):
        ret = obj.method_with_cached_list_return()
        ret2 = obj.method_with_cached_list_return()
        self.assertEquals(ret, ret2)
        ret3 = obj.method_with_cached_list_return()
        self.assertEquals(ret, ret3)
        self.assertEquals(ret.size, 2)
        self.assertEquals(ret[0].get_string, 'foo')
        self.assertEquals(ret[1].get_string, 'bar')

    def testJsonReturns(self):
        ret = obj.method_with_json_object_return()
        self.assertEqual(ret, {'cheese' : 'stilton'})
        ret = obj.method_with_json_array_return()
        self.assertEqual(ret, ['socks', 'shoes'])

    def testNullJsonReturns(self):
        ret = obj.method_with_null_json_object_return()
        self.assertIsNone(ret)
        ret = obj.method_with_null_json_array_return()
        self.assertIsNone(ret)

    def testComplexJsonReturns(self):
        ret = obj.method_with_complex_json_object_return()
        self.assertEqual(ret, {'outer' : {'socks' : 'tartan'}, 'list': ['yellow', 'blue']})
        ret = obj.method_with_complex_json_array_return()
        self.assertEqual(ret, [{'foo' : 'hello'}, {'bar' : 'bye'}])

    def testJsonParams(self):
        obj.method_with_json_params({'cat' : 'lion', 'cheese' : 'cheddar'},
                                    ['house', 'spider'])

    def testNullJsonParams(self):
        self.assertRaises(TypeError, obj.method_with_null_json_params, None, None)

    def testJsonHandlerParams(self):
        dct = dict(count=0)

        def obj_handler(val):
            self.assertEqual(val, {'cheese' : 'stilton'})
            dct['count'] += 1

        def arr_handler(val):
            self.assertEqual(val, ['socks', 'shoes'])
            dct['count'] += 1

        obj.method_with_handler_json(obj_handler, arr_handler)
        self.assertEqual(dct['count'], 2)

    def testComplexJsonHandlerParams(self):
        dct = dict(count=0)

        def obj_handler(val):
            print(type(val))
            self.assertEqual(val, {'outer' : {'socks' : 'tartan'},
                                   'list' : ['yellow', 'blue']})
            dct['count'] += 1

        def arr_handler(val):
            self.assertEqual(val, [[{'foo' : 'hello'}], [{'bar' : 'bye'}]])
            dct['count'] += 1

        obj.method_with_handler_complex_json(obj_handler, arr_handler)
        self.assertEqual(dct['count'], 2)

    def testJsonHandlerAsyncResultParams(self):
        dct = dict(count=0)
        def obj_handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(val, {'cheese' : 'stilton'})
            dct['count'] += 1
        def arr_handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(val, ['socks', 'shoes'])
            dct['count'] += 1
        obj.method_with_handler_async_result_json_object(obj_handler)
        obj.method_with_handler_async_result_json_array(arr_handler)
        self.assertEqual(dct['count'], 2)

    def testNullJsonHandlerAsyncResultParams(self):
        dct = dict(count=0)
        def obj_handler(val, err):
            self.assertIsNone(val)
            self.assertIsNone(err)
            dct['count'] += 1
        def arr_handler(val, err):
            self.assertIsNone(val)
            self.assertIsNone(err)
            dct['count'] += 1

        obj.method_with_handler_async_result_null_json_object(obj_handler)
        obj.method_with_handler_async_result_null_json_array(arr_handler)
        self.assertEqual(dct['count'], 2)

    def testEnumParam(self):
        ret = obj.method_with_enum_param('sausages', "TIM")
        self.assertEqual(ret, 'sausagesTIM')

    def testThrowableParam(self):
        try:
            raise Exception('the_throwable')
        except Exception as t:
            ret = obj.method_with_throwable_param(t)
            self.assertEquals(ret, '(RuntimeError) the_throwable')

    def testSuperMethodOverloadedBySubclass(self):
        self.assertEquals(0, obj.super_method_overloaded_by_subclass)
        self.assertEquals(1, obj.super_method_overloaded_by_subclass('one_arg'))

    def testEnumReturn(self):
        ret = obj.method_with_enum_return('JULIEN')
        self.assertEqual('JULIEN', ret)

    def testComplexJsonHandlerAsyncResultParams(self):
        dct = dict(count=0)

        def obj_handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(val, {'outer' : {'socks' : 'tartan'},
                                   'list' : ['yellow', 'blue']})
            dct['count'] += 1

        def arr_handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(val, [{'foo' : 'hello'}, {'bar' : 'bye'}])
            dct['count'] += 1

        obj.method_with_handler_async_result_complex_json_object(obj_handler)
        obj.method_with_handler_async_result_complex_json_array(arr_handler)
        self.assertEqual(dct['count'], 2)

    def testThrowableReturn(self):
        ret = obj.method_with_throwable_return('bogies')
        self.assertEqual('bogies', ret.getMessage())

    def testCustomModule(self):
        my = MyInterface.create()
        test_interface = my.method()
        test_interface.method_with_basic_params(123, 12345, 1234567,
                                                1265615234, 12.345, 12.34566,
                                                True, 88, 'foobar')
        sub = my.sub()
        ret = sub.reverse("hello")
        self.assertEqual(ret, "olleh")

