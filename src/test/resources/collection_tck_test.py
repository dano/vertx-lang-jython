import unittest

import io.vertx.codegen.testmodel.RefedInterface1Impl
import re

from testmodel_jython.testmodel.collection_tck import CollectionTCK
from testmodel_jython.testmodel.refed_interface1 import RefedInterface1
from testmodel_jython.testmodel.refed_interface2 import RefedInterface2

obj = CollectionTCK(io.vertx.codegen.testmodel.CollectionTCKImpl())

class CollectionTCKTest(unittest.TestCase):

    def testMethodWithHandlerListAndSet(self):
        dct = dict(count=0)

        def handle_str_list(l):
            self.assertEqual(type(l), list)
            self.assertEqual("foo", l[0])
            self.assertEqual("bar", l[1])
            self.assertEqual("wibble", l[2])
            dct['count'] += 1

        def handle_int_list(l):
            self.assertEqual(type(l), list)
            self.assertEqual(5, l[0])
            self.assertEqual(12, l[1])
            self.assertEqual(100, l[2])
            dct['count'] += 1

        def handle_str_set(s):
            self.assertEqual(type(s), set)
            self.assertSetEqual(set(['foo', 'bar', 'wibble']), s)
            dct['count'] += 1

        def handle_int_set(s):
            self.assertEqual(type(s), set)
            self.assertSetEqual(set([5, 12, 100]), s)
            dct['count'] += 1

        obj.method_with_handler_list_and_set(handle_str_list, handle_int_list,
                                             handle_str_set, handle_int_set)
        self.assertEqual(dct['count'], 4)

    def testMethodWithHandlerAsyncResultListAndSet(self):
        dct = dict(count=0)

        def handle_str_list(l, err):
            self.assertIsNone(err)
            self.assertEqual(type(l), list)
            self.assertEqual("foo", l[0])
            self.assertEqual("bar", l[1])
            self.assertEqual("wibble", l[2])
            dct['count'] += 1

        def handle_int_list(l, err):
            self.assertIsNone(err)
            self.assertEqual(type(l), list)
            self.assertEqual(5, l[0])
            self.assertEqual(12, l[1])
            self.assertEqual(100, l[2])
            dct['count'] += 1

        def handle_str_set(s, err):
            self.assertIsNone(err)
            self.assertEqual(type(s), set)
            self.assertSetEqual({'foo', 'bar', 'wibble'}, s)
            dct['count'] += 1

        def handle_int_set(s, err):
            self.assertIsNone(err)
            self.assertEqual(type(s), set)
            self.assertSetEqual({5, 12, 100}, s)
            dct['count'] += 1

        obj.method_with_handler_async_result_list_string(handle_str_list)
        obj.method_with_handler_async_result_list_integer(handle_int_list)
        obj.method_with_handler_async_result_set_string(handle_str_set)
        obj.method_with_handler_async_result_set_integer(handle_int_set)
        self.assertEqual(dct['count'], 4)

    def testMethodWithHandlerListVertxGen(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(type(val), list)
            self.assertEqual(len(val), 2)
            self.assertEqual(type(val[0]), RefedInterface1)
            self.assertEqual(val[0].get_string(), 'foo')
            self.assertEqual(type(val[1]), RefedInterface1)
            self.assertEqual(val[1].get_string(), 'bar')
            dct['count'] += 1
        obj.method_with_handler_list_vertx_gen(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerListAbstractVertxGen(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(type(val), list)
            self.assertEqual(len(val), 2)
            self.assertIsInstance(val[0], RefedInterface2)
            self.assertEqual(val[0].get_string(), 'abstractfoo')
            self.assertIsInstance(val[1], RefedInterface2)
            self.assertEqual(val[1].get_string(), 'abstractbar')
            dct['count'] += 1

        obj.method_with_handler_list_abstract_vertx_gen(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultListVertxGen(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), list)
            self.assertEqual(len(val), 2)
            self.assertEqual(type(val[0]), RefedInterface1)
            self.assertEqual(val[0].get_string(), 'foo')
            self.assertEqual(type(val[1]), RefedInterface1)
            self.assertEqual(val[1].get_string(), 'bar')
            dct['count'] += 1
        obj.method_with_handler_async_result_list_vertx_gen(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultListAbstractVertxGen(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), list)
            self.assertEqual(len(val), 2)
            self.assertIsInstance(val[0], RefedInterface2)
            self.assertEqual(val[0].get_string(), 'abstractfoo')
            self.assertIsInstance(val[1], RefedInterface2)
            self.assertEqual(val[1].get_string(), 'abstractbar')
            dct['count'] += 1

        obj.method_with_handler_async_result_list_abstract_vertx_gen(handler)
        self.assertEqual(dct['count'], 1)


    def testMethodWithHandlerSetVertxGen(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(type(val), set)
            self.assertEqual(len(val), 2)
            for item in val:
                self.assertEqual(type(item), RefedInterface1)
            self.assertSetEqual(set([x.get_string() for x in val]),
                                {'foo', 'bar'})
            dct['count'] += 1
        obj.method_with_handler_set_vertx_gen(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerSetAbstractVertxGen(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(type(val), set)
            self.assertEqual(len(val), 2)
            for item in val:
                self.assertIsInstance(item, RefedInterface2)
            self.assertSetEqual(set([x.get_string() for x in val]),
                                set(['abstractfoo', 'abstractbar']))
            dct['count'] += 1

        obj.method_with_handler_set_abstract_vertx_gen(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultSetVertxGen(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), set)
            self.assertEqual(len(val), 2)
            for item in val:
                self.assertEqual(type(item), RefedInterface1)
            self.assertSetEqual(set([x.get_string() for x in val]),
                                set(['foo', 'bar']))
            dct['count'] += 1

        obj.method_with_handler_async_result_set_vertx_gen(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultSetAbstractVertxGen(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), set)
            self.assertEqual(len(val), 2)
            for item in val:
                self.assertIsInstance(item, RefedInterface2)
            self.assertSetEqual(set([x.get_string() for x in val]),
                                set(['abstractfoo', 'abstractbar']))
            dct['count'] += 1

        obj.method_with_handler_async_result_set_abstract_vertx_gen(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerListJsonObject(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(type(val), list)
            self.assertEqual(len(val), 2)
            self.assertEqual(type(val[0]), dict)
            self.assertEqual(val[0], dict(cheese='stilton'))
            self.assertEqual(type(val[1]), dict)
            self.assertEqual(val[1], dict(socks='tartan'))
            dct['count'] += 1
        obj.method_with_handler_list_json_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerListComplexJsonObject(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(type(val), list)
            self.assertEqual(len(val), 1)
            self.assertEqual(val[0], {'outer' : {'socks' : 'tartan'}, 'list' : ['yellow', 'blue']})
            dct['count'] += 1
        obj.method_with_handler_list_complex_json_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultListJsonObject(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), list)
            self.assertEqual(len(val), 2)
            self.assertEqual(type(val[0]), dict)
            self.assertEqual(val[0], dict(cheese='stilton'))
            self.assertEqual(type(val[1]), dict)
            self.assertEqual(val[1], dict(socks='tartan'))
            dct['count'] += 1
        obj.method_with_handler_async_result_list_json_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultListComplexJsonObject(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), list)
            self.assertEqual(len(val), 1)
            self.assertEqual(val[0], {'outer' : {'socks' : 'tartan'},
                                      'list' : ['yellow', 'blue']})
            dct['count'] += 1
        obj.method_with_handler_async_result_list_complex_json_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerSetJsonObject(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(type(val), set)
            for elt in val:
                self.assertEqual(type(elt), dict)
            self.assertEqual(val, set([dict(cheese='stilton'),
                                       dict(socks='tartan')]))
            dct['count'] += 1
        obj.method_with_handler_set_json_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerSetComplexJsonObject(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(type(val), set)
            self.assertEqual(len(val), 1)
            self.assertEqual(val, set([dict({'outer' : dict({'socks' : 'tartan'}),
                                             'list' : set(['yellow', 'blue'])})
                                       ])
                             )
            dct['count'] += 1
        obj.method_with_handler_set_complex_json_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultSetJsonObject(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), set)
            for elt in val:
                self.assertEqual(type(elt), dict)
            self.assertEqual(val, set([dict(cheese='stilton'),
                                       dict(socks='tartan')]))
            dct['count'] += 1
        obj.method_with_handler_async_result_set_json_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultSetComplexJsonObject(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), set)
            self.assertEqual(len(val), 1)
            self.assertEqual(val, set([dict({'outer' : dict({'socks' : 'tartan'}),
                                             'list' : set(['yellow', 'blue'])})
                                       ])
                             )
            dct['count'] += 1
        obj.method_with_handler_async_result_set_complex_json_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerListJsonArray(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(type(val), list)
            self.assertEqual(len(val), 2)
            self.assertEqual(type(val[0]), list)
            self.assertEqual(val[0], ['green', 'blue'])
            self.assertEqual(type(val[1]), list)
            self.assertEqual(val[1], ['yellow', 'purple'])
            dct['count'] += 1
        obj.method_with_handler_list_json_array(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultListJsonArray(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), list)
            self.assertEqual(len(val), 2)
            self.assertEqual(type(val[0]), list)
            self.assertEqual(val[0], ['green', 'blue'])
            self.assertEqual(type(val[1]), list)
            self.assertEqual(val[1], ['yellow', 'purple'])
            dct['count'] += 1
        obj.method_with_handler_async_result_list_json_array(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultListComplexJsonArray(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), list)
            self.assertEqual(val, [[{'foo' : 'hello'}], [{'bar' : 'bye'}]])
            dct['count'] += 1
        obj.method_with_handler_async_result_list_complex_json_array(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerSetJsonArray(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(type(val), set)
            for elt in val:
                self.assertEqual(type(elt), set)
            self.assertEqual(val, {{'green', 'blue'}, {'yellow', 'purple'}})
            dct['count'] += 1
        obj.method_with_handler_set_json_array(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerSetComplexJsonArray(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(type(val), set)
            self.assertEqual(val, {{dict({'foo': 'hello'})}, {dict({'bar': 'bye'})}}
                             )
            dct['count'] += 1
        obj.method_with_handler_set_complex_json_array(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultSetJsonArray(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), set)
            for elt in val:
                self.assertEqual(type(elt), set)
            self.assertEqual(val, {{'purple', 'yellow'}, {'blue', 'green'}}
                             )
            dct['count'] += 1
        obj.method_with_handler_async_result_set_json_array(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerListComplexJsonArray(self):
        dct = dict(count=0)

        def handler(val):
            self.assertEqual(type(val), list)
            self.assertEqual(val, [[{'foo' : 'hello'}], [{'bar' : 'bye'}]])
            dct['count'] += 1

        obj.method_with_handler_list_complex_json_array(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerListDataObject(self):
        dct = dict(count=0)

        def handler(val):
            self.assertEqual(type(val), list)
            for elt in val:
                self.assertEqual(type(elt), dict)
            self.assertEqual(val[0], {'foo' : 'String 1', 'bar' : 1, 'wibble' : 1.1})
            self.assertEqual(val[1], {'foo' : 'String 2', 'bar' : 2, 'wibble' : 2.2})
            dct['count'] += 1

        obj.method_with_handler_list_data_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerSetDataObject(self):
        dct = dict(count=0)
        def handler(val):
            self.assertEqual(val, set([dict({'foo' : 'String 1', 'bar' : 1, 'wibble' : 1.1}),
                                       dict({'foo' : 'String 2', 'bar' : 2, 'wibble' : 2.2})
                                       ])
                             )
            dct['count'] += 1
        obj.method_with_handler_set_data_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultSetComplexJsonArray(self):
        dct = dict(count=0)
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), set)
            self.assertEqual(val, set([set([dict({'foo' : 'hello'})]),
                                       set([dict({'bar' : 'bye'})])
                                       ])
                             )
            dct['count'] += 1
        obj.method_with_handler_async_result_set_complex_json_array(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultListDataObject(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(type(val), list)
            for elt in val:
                self.assertEqual(type(elt), dict)
            self.assertEqual(val[0], {'foo' : 'String 1', 'bar' : 1, 'wibble' : 1.1})
            self.assertEqual(val[1], {'foo' : 'String 2', 'bar' : 2, 'wibble' : 2.2})
            dct['count'] += 1
        obj.method_with_handler_async_result_list_data_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMethodWithHandlerAsyncResultSetDataObject(self):
        dct = dict(count=0)
        def handler(val, err):
            self.assertIsNone(err)
            self.assertEqual(val, set([dict({'foo' : 'String 1', 'bar' : 1, 'wibble' : 1.1}),
                                       dict({'foo' : 'String 2', 'bar' : 2, 'wibble' : 2.2})
                                       ])
                             )
            dct['count'] += 1
        obj.method_with_handler_async_result_set_data_object(handler)
        self.assertEqual(dct['count'], 1)

    def testMapReturn(self):
        readLog = []
        writeLog = []
        def handler(op):
            wpatt = '|'.join(['put\([^,]+,[^\)]+\)', 'remove\([^\)]+\)'])
            rpatt = 'get\([^\)]+\)'
            m = re.match(wpatt, op)
            if m or op == 'clear()':
                writeLog.append(op)
            else:
                m = re.match(rpatt, op)
                if m or op in ('size()', 'keySet()'):
                    readLog.append(op)
                else:
                    raise Exception("Unsupported: {}".format(op))
        map = obj.method_with_map_return(handler)
        map['foo'] = 'bar'
        self.assertEqual(writeLog, ['put(foo,bar)'])
        readLog[:] = []
        writeLog[:] = []
        self.assertEqual(map['foo'], 'bar')
        readLog.index('get(foo)')
        self.assertEqual(writeLog, [])
        map['wibble'] = 'quux'
        readLog[:] = []
        writeLog[:] = []
        self.assertEqual(len(map), 2)
        self.assertEqual(map['wibble'], 'quux')
        readLog.index('size()')
        self.assertEqual(writeLog, [])
        readLog[:] = []
        writeLog[:] = []
        del map['wibble']
        self.assertEqual(writeLog, ['remove(wibble)'])
        self.assertEqual(len(map), 1)
        map['blah'] = '123'
        key_dct = dict(count=0)
        readLog[:] = []
        writeLog[:] = []
        for k,v in map.iteritems():
            if key_dct['count'] == 0:
                self.assertEqual(k, 'foo')
                self.assertEqual(v, 'bar')
                key_dct['count'] += 1
            else:
                self.assertEqual(k, 'blah')
                self.assertEqual(v, '123')
        readLog.index('keySet()')
        self.assertEqual(writeLog, [])
        readLog[:] = []
        writeLog[:] = []
        map.clear()
        # Clear maps to removing each item one by one.
        self.assertEqual(writeLog, ['remove(foo)', 'remove(blah)'])

    def testMapStringReturn(self):
        map = obj.method_with_map_string_return(lambda x: x)
        val = map['foo']
        self.assertEqual(type(val), unicode)
        self.assertEqual(val, 'bar')
        map['juu'] = 'daa'
        self.assertEqual(map, {'foo' : 'bar','juu' : 'daa'})
        def test():
            map['wibble'] = 123
        self.assertRaises(Exception, test)
        self.assertEqual(map, {'foo' : 'bar','juu' : 'daa'})

    def testMapJsonObjectReturn(self):
        map = obj.method_with_map_json_object_return(lambda x: x)
        json = map['foo']
        self.assertEqual(type(json), dict)
        self.assertEqual(json['wibble'], 'eek')
        map['bar'] = {'juu' : 'daa'}
        self.assertEqual(map, {'foo' : {'wibble' : 'eek'}, 'bar' : {'juu' : 'daa'}})
        def test():
            map['juu'] = 123
        self.assertRaises(Exception, test)
        self.assertEqual(map, {'foo' : {'wibble' : 'eek'}, 'bar' : {'juu' : 'daa'}})

    def testMapComplexJsonObjectReturn(self):
        map = obj.method_with_map_complex_json_object_return(lambda x: x)
        m = map['foo']
        self.assertEqual(m, {'outer' : {'socks' : 'tartan'}, 'list' : ['yellow', 'blue']})

    def testMapJsonArrayReturn(self):
        map = obj.method_with_map_json_array_return(lambda x:x)
        arr = map['foo']
        self.assertEqual(type(arr), list)
        self.assertEqual(arr, ['wibble'])
        map['bar'] = ['spidey']
        self.assertEqual(map, {'foo': ['wibble'],'bar': ['spidey']})
        def test():
            map['juu'] = 123
        self.assertRaises(Exception, test)
        self.assertEqual(map, {'foo': ['wibble'],'bar': ['spidey']})

    def testMapLongReturn(self):
        map = obj.method_with_map_long_return(lambda x:x)
        num = map['foo']
        self.assertEqual(type(num), long)
        self.assertEqual(num, 123)
        map['bar'] = 321
        self.assertEqual(map, {'foo' : 123,'bar' : 321})
        def test():
            map['juu'] = 'something'
        self.assertRaises(Exception, test)
        self.assertEqual(map, {'foo' : 123,'bar' : 321})

    def testMapIntegerReturn(self):
        map = obj.method_with_map_integer_return(lambda x:x)
        num = map['foo']
        self.assertEqual(type(num), int)
        self.assertEqual(num, 123)
        map['bar'] = 321
        self.assertEqual(map, {'foo' : 123,'bar' : 321})
        def test():
            map['juu'] = 'something'
        self.assertRaises(Exception, test)
        self.assertEqual(map, {'foo' : 123,'bar' : 321})

    def testMapShortReturn(self):
        map = obj.method_with_map_short_return(lambda x:x)
        num = map['foo']
        self.assertEqual(type(num), int)
        self.assertEqual(num, 123)
        map['bar'] = 321
        self.assertEqual(map, {'foo' : 123,'bar' : 321})
        def test():
            map['juu'] = 'something'
        self.assertRaises(Exception, test)
        self.assertEqual(map, {'foo' : 123,'bar' : 321})

    def testMapByteReturn(self):
        map = obj.method_with_map_byte_return(lambda x:x)
        num = map['foo']
        self.assertEqual(type(num), int)
        self.assertEqual(num, 123)
        map['bar'] = 12
        self.assertEqual(map, {'foo' : 123,'bar' : 12})
        def test():
            map['juu'] = 'something'
        self.assertRaises(Exception, test)
        self.assertEqual(map, {'foo' : 123,'bar' : 12})

    def testMapCharacterReturn(self):
        map = obj.method_with_map_character_return(lambda x:x)
        num = map['foo']
        self.assertEqual(type(num), unicode)
        self.assertEqual(num, 'X')
        map['bar'] = 'Y'
        self.assertEqual(map, {'foo' : 'X','bar' : 'Y'})
        def test():
            map['juu'] = 'something'
        self.assertRaises(ValueError, test)
        self.assertEqual(map, {'foo' : 'X','bar' : 'Y'})

    def testMapBooleanReturn(self):
        map = obj.method_with_map_boolean_return(lambda x:x)
        num = map['foo']
        self.assertEqual(type(num), bool)
        self.assertEqual(num, True)
        map['bar'] = False
        self.assertEqual(map, {'foo' : True,'bar' : False})
        map['juu'] = 'something'
        map['daa'] = None
        self.assertEqual(map, {'foo' : True,'bar' : False,'juu' : True,'daa' : False})

    def testMapFloatReturn(self):
        map = obj.method_with_map_float_return(lambda x:x)
        num = map['foo']
        self.assertEqual(type(num), float)
        self.assertEqual(num, 0.123)
        map['bar'] = 0.321
        self.assertEqual(map['foo'], 0.123)
        self.assertEqual(map['bar'], 0.321)
        self.assertEqual(sorted(map.keys()), ['bar', 'foo'])
        def test():
            map['juu'] = 'something'
        self.assertRaises(Exception, test)
        self.assertEqual(map['foo'], 0.123)
        self.assertEqual(map['bar'], 0.321)
        self.assertEqual(sorted(map.keys()), ['bar', 'foo'])

    def testMapDoubleReturn(self):
        map = obj.method_with_map_double_return(lambda x:x)
        num = map['foo']
        self.assertEqual(type(num), float)
        self.assertEqual(num, 0.123)
        map['bar'] = 0.321
        self.assertEqual(map, {'foo' : 0.123,'bar' : 0.321})
        def test():
            map['juu'] = 'something'
        self.assertRaises(Exception, test)
        self.assertEqual(map, {'foo' : 0.123,'bar' : 0.321})

    def testListStringReturn(self):
        ret = obj.method_with_list_string_return()
        self.assertIsInstance(ret, list)
        self.assertEqual(ret, ['foo', 'bar', 'wibble'])

    def testListLongReturn(self):
        ret = obj.method_with_list_long_return()
        self.assertIsInstance(ret, list)
        self.assertEqual(ret, [123,456])

    def testListJsonObjectReturn(self):
        ret = obj.method_with_list_json_object_return()
        self.assertIsInstance(ret, list)
        self.assertEqual(ret, [{'foo' : 'bar'},{'blah' : 'eek'}])

    def testListComplexJsonObjectReturn(self):
        ret = obj.method_with_list_complex_json_object_return()
        self.assertIsInstance(ret, list)
        self.assertEqual(ret, [{'outer' : {'socks' : 'tartan'}, 'list' : ['yellow', 'blue']}])

    def testListJsonArrayReturn(self):
        ret = obj.method_with_list_json_array_return()
        self.assertIsInstance(ret, list)
        self.assertEqual(ret, [['foo'],['blah']])

    def testListComplexJsonArrayReturn(self):
        ret = obj.method_with_list_complex_json_array_return()
        self.assertIsInstance(ret, list)
        self.assertEqual(ret, [[{'foo' : 'hello'}],[{'bar' : 'bye'}]])

    def testListVertxGenReturn(self):
        ret = obj.method_with_list_vertx_gen_return()
        self.assertIsInstance(ret, list)
        self.assertEqual(type(ret[0]), RefedInterface1)
        self.assertEqual(ret[0].get_string(), 'foo')
        self.assertEqual(type(ret[1]), RefedInterface1)
        self.assertEqual(ret[1].get_string(), 'bar')

    def testListDataObjectReturn(self):
      ret = obj.method_with_list_data_object_return()
      self.assertEqual(type(ret), list)
      for elt in ret:
          self.assertTrue(isinstance(elt, dict))
      self.assertEquals(ret[0], {'foo': 'String 1','bar': 1,'wibble': 1.1})
      self.assertEquals(ret[1], {'foo': 'String 2','bar': 2,'wibble': 2.2})

    def testListEnumReturn(self):
      ret = obj.method_with_list_enum_return()
      self.assertEquals(type(ret), list)
      self.assertEquals(ret[0], 'JULIEN')
      self.assertEquals(ret[1], 'TIM')

    def testSetStringReturn(self):
        ret = obj.method_with_set_string_return()
        self.assertIsInstance(ret, set)
        self.assertEqual(ret, set(['foo', 'bar', 'wibble']))

    def testSetLongReturn(self):
        ret = obj.method_with_set_long_return()
        self.assertIsInstance(ret, set)
        self.assertEqual(ret, set([123,456]))

    def testSetJsonObjectReturn(self):
        ret = obj.method_with_set_json_object_return()
        self.assertEqual(type(ret), set)
        self.assertEqual(ret, set([dict({'foo':'bar'}),
                                   dict({'blah':'eek'})
                                   ])
                         )

    def testSetComplexJsonObjectReturn(self):
        ret = obj.method_with_set_complex_json_object_return()
        self.assertEqual(type(ret), set)
        self.assertEqual(ret, set([dict({'outer' : dict({'socks' : 'tartan'}),
                                         'list': set(['yellow', 'blue'])})
                                   ])
                         )

    def testSetJsonArrayReturn(self):
        ret = obj.method_with_set_json_array_return()
        self.assertIsInstance(ret, set)
        self.assertEqual(ret, set([set(['foo']),
                                   set(['blah'])
                                   ])
                         )

    def testSetComplexJsonArrayReturn(self):
        ret = obj.method_with_set_complex_json_array_return()
        self.assertIsInstance(ret, set)
        self.assertEqual(ret, set([set([dict({'foo' : 'hello'})]),
                                   set([dict({'bar' : 'bye'})])
                                   ])
                         )

    def testSetVertxGenReturn(self):
        ret = obj.method_with_set_vertx_gen_return()
        self.assertIsInstance(ret, set)
        for elt in ret:
            self.assertIsInstance(elt, RefedInterface1)
        self.assertEqual(set([o.get_string() for o in ret]), set(['foo', 'bar']))

    def testSetDataObjectReturn(self):
        ret = obj.method_with_set_data_object_return()
        self.assertEquals(ret, set([{'foo': 'String 1','bar': 1,'wibble': 1.1},
                                  {'foo': 'String 2','bar': 2,'wibble': 2.2}]))

    def testSetEnumReturn(self):
        ret = obj.method_with_set_enum_return()
        self.assertEquals(ret, {'JULIEN', 'TIM'})

    def testMapComplexJsonArrayReturn(self):
        out = obj.method_with_map_complex_json_array_return(lambda x: x)
        m = out['foo']
        self.assertEqual(m, [{'foo' : 'hello'}, {'bar' : 'bye'}])

    def testMethodWithHandlerListEnum(self):
        dct = dict(count=0)
        def h(val):
            self.assertEquals(val, ['TIM','JULIEN'])
            dct['count'] += 1
        obj.method_with_handler_list_enum(h)
        self.assertEquals(1, dct['count'])

    def testMethodWithHandlerSetEnum(self):
        dct = dict(count=0)
        def h(val):
            self.assertEquals(val, {'TIM', 'JULIEN'})
            dct['count'] += 1
        obj.method_with_handler_set_enum(h)
        self.assertEquals(1, dct['count'])

    def testMethodWithHandlerAsyncResultListEnum(self):
        dct = dict(count=0)
        def h(val, err):
            self.assertIsNone(err)
            self.assertEquals(val, ['TIM','JULIEN'])
            dct['count'] += 1

        obj.method_with_handler_async_result_list_enum(h)
        self.assertEquals(1, dct['count'])

    def testMethodWithHandlerAsyncResultSetEnum(self):
        dct = dict(count=0)

        def h(val, err):
            self.assertIsNone(err)
            self.assertEquals(val, {'TIM', 'JULIEN'})
            dct['count'] += 1

        obj.method_with_handler_async_result_set_enum(h)
        self.assertEquals(1, dct['count'])

    def testMethodWithListParams(self):
        obj.method_with_list_params(
            ['foo', 'bar'],
            [2, 3],
            [12, 13],
            [1234, 1345],
            [123, 456],
            [{'foo':'bar'}, {'eek':'wibble'}],
            [['foo'], ['blah']],
            [RefedInterface1(jvm.io.vertx.codegen.testmodel.RefedInterface1Impl()).set_string('foo'),
             RefedInterface1(jvm.io.vertx.codegen.testmodel.RefedInterface1Impl()).set_string('bar')],
            [{'foo':'String 1','bar':1,'wibble':1.1}, {'foo':'String 2','bar':2,'wibble':2.2}],
            ['JULIEN', 'TIM']
        )

    def testMethodWithSetParams(self):
        obj.method_with_set_params(
            {'foo', 'bar'},
            {2, 3},
            {12, 13},
            {1234, 1345},
            {123, 456},
            {dict({'foo': 'bar'}), dict({'eek': 'wibble'})},
            {{'foo'}, {'blah'}},
            {
                RefedInterface1(jvm.io.vertx.codegen.testmodel.RefedInterface1Impl()).set_string('foo'),
                RefedInterface1(jvm.io.vertx.codegen.testmodel.RefedInterface1Impl()).set_string('bar')
            },
            {dict({'foo': 'String 1', 'bar': 1, 'wibble': 1.1}),
             dict({'foo': 'String 2', 'bar': 2, 'wibble': 2.2})},
            {'TIM', 'JULIEN'}
        )

    def testMethodWithMapParams(self):
        obj.method_with_map_params(
            {'foo' : 'bar', 'eek' : 'wibble'},
            {'foo' : 2, 'eek' : 3},
            {'foo' : 12, 'eek' : 13},
            {'foo' : 1234, 'eek' : 1345},
            {'foo' : 123, 'eek' : 456},
            {'foo' : {'foo' : 'bar'}, 'eek' : {'eek' : 'wibble'}},
            {'foo' : ['foo'], 'eek' : ['blah']},
            {'foo' : RefedInterface1(jvm.io.vertx.codegen.testmodel.RefedInterface1Impl()).set_string('foo'),
             'eek' : RefedInterface1(jvm.io.vertx.codegen.testmodel.RefedInterface1Impl()).set_string('bar')}
        )

