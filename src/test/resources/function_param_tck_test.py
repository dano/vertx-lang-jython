import unittest

from io.vertx.codegen.testmodel import FunctionParamTCKImpl
from io.vertx.codegen.testmodel import RefedInterface1Impl

from testmodel_jython.testmodel.function_param_tck import FunctionParamTCK
from testmodel_jython.testmodel.refed_interface1 import RefedInterface1

obj = FunctionParamTCK(FunctionParamTCKImpl())
refed_obj = RefedInterface1(RefedInterface1Impl())

class TestAPI(unittest.TestCase):

    def testBasicParam(self):
        def handle_byte(arg):
            self.assertEquals(arg, 100)
            return "ok0"

        def handle_short(arg):
            self.assertEquals(arg, 1000)
            return "ok1"

        def handle_integer(arg):
            self.assertEquals(arg, 10000)
            return "ok2"

        def handle_long(arg):
            self.assertEquals(arg, 10000000000)
            return "ok3"

        def handle_float(arg):
            self.assertEquals(arg, 3.5)
            return "ok4"

        def handle_double(arg):
            self.assertEquals(arg, 0.01)
            return "ok5"

        def handle_boolean(arg):
            self.assertEquals(arg, True)
            return "ok6"

        def handle_char(arg):
            self.assertEquals(arg, 70)
            return "ok7"

        def handle_string(arg):
            self.assertEquals(arg, "wibble")
            return "ok8"

        ret = obj.method_with_basic_param(
            handle_byte,
            handle_short,
            handle_integer,
            handle_long,
            handle_float,
            handle_double,
            handle_boolean,
            handle_char,
            handle_string)
        self.assertEquals(ret, ["ok0","ok1","ok2","ok3","ok4","ok5","ok6","ok7","ok8"])

    def testJsonParam(self):

        def handle_obj(arg):
            self.assertEquals(arg, {"one": 1,"two": 2,"three": 3})
            return 'ok'

        def handle_array(arg):
            self.assertEquals(arg, ["one","two","three"])

        ret = obj.method_with_json_param(handle_obj, handle_array)
        self.assertEquals(ret, ["ok0","ok1"])

    def testUserTypeParam(self):
        def h(arg):
            arg.set_string("foobarjuu")
            self.assertEquals(arg.get_string(), "foobarjuu")
            return 'ok'

        ret = obj.method_with_user_type_param(refed_obj, h)
        self.assertEquals(ret, "ok")

    def testObjectParam(self):
        def h(arg):
            self.assertEquals(arg, 123)
            return 'ok'

        self.assertEquals('ok', obj.method_with_object_param(123, h))

        def h2(arg):
            self.assertEquals(arg, "the-string-arg")
            return 'ok'

        self.assertEquals('ok', obj.method_with_object_param("the-string-arg", h2))

    def testDataObjectParam(self):
        def h(arg):
            self.assertEquals(arg["foo"], "foo_value")
            self.assertEquals(arg["bar"], 3)
            self.assertEquals(arg["wibble"], 0.01)
            return 'ok'

        self.assertEquals('ok', obj.method_with_data_object_param(h))

    def testEnumParam(self):
        def h(arg):
            self.assertEquals(arg, 'TIM')
            return "ok"
        self.assertEquals('ok', obj.method_with_enum_param(h))

    def testListParam(self):
        def h(arg):
            self.assertEquals(arg, ["one","two","three"])
            return "ok"
        self.assertEquals('ok', obj.method_with_list_param(h))

    def testSetParam(self):
        def h(arg):
            self.assertEquals(arg, {"one","two","three"})
            return "ok"
        self.assertEquals('ok', obj.method_with_set_param(h))

    def testMapParam(self):
        def h(arg):
            self.assertEquals(arg, {"one": "one","two": "two","three": "three"})
            return "ok"

        self.assertEquals('ok', obj.method_with_map_param(h))

    def testGenericParam(self):
        def h(arg):
            self.assertEquals(arg, 123)
            return "ok"
        self.assertEquals('ok', obj.method_with_generic_param(123, h))

        def h2(arg):
            self.assertEquals(arg, "the-string-arg")
            return "ok"
        self.assertEquals('ok', obj.method_with_generic_param("the-string-arg", h2))

    def testGenericUserTypeParam(self):
        def h(arg):
            self.assertEquals(arg.get_value(), 123)
            return "ok"
        self.assertEquals('ok', obj.method_with_generic_user_type_param(123, h))

        def h2(arg):
            self.assertEquals(arg.get_value(), "the-string-arg")
            return "ok"
        self.assertEquals('ok', obj.method_with_generic_user_type_param("the-string-arg", h2))

    def testNullableListParam(self):
        # Cannot pass because nullable return is not implemented
        pass

    def testBasicReturn(self):
        ret = obj.method_with_basic_return(
            lambda arg: 10,
            lambda arg: 1000,
            lambda arg: 100000,
            lambda arg: 10000000000,
            lambda arg: 0.01,
            lambda arg: 0.00001,
            lambda arg: True,
            lambda arg: 67,
            lambda arg: "the-return"
        )
        self.assertEquals(ret, "ok")

    def testJsonReturn(self):
        ret = obj.method_with_json_return(
           lambda arg: {"foo": "foo_value", "bar":10, "wibble":0.1},
           lambda arg: ["one", "two", "three"]
        )
        self.assertEquals(ret, "ok")

    def testObjectReturn(self):
        def h(arg):
            if arg == 0:
                return "the-string"
            elif arg == 1:
                return 123
            elif arg == 2:
                return True
            elif arg == 3:
                return { "foo": "foo_value" }
            elif arg == 4:
                return ["foo", "bar"]
            else:
                return None
        ret = obj.method_with_object_return(h)
        self.assertEquals(ret, "ok")

    def testDataObjectReturn(self):
        ret = obj.method_with_data_object_return(lambda arg: {"foo": "wasabi","bar": 6,"wibble": 0.01})
        self.assertEquals(ret, "ok")

    def testEnumReturn(self):
        ret = obj.method_with_enum_return(lambda arg: "NICK")
        self.assertEquals(ret, "ok")

    def testListReturn(self):
        ret = obj.method_with_list_return(lambda x: ["one", "two", "three"])
        self.assertEquals(ret, "ok")

    def testSetReturn(self):
        ret = obj.method_with_set_return(lambda x: {"one", "two", "three"})
        self.assertEquals(ret, "ok")

    def testMapReturn(self):
        ret = obj.method_with_map_return(lambda x: {"one": "one", "two": "two", "three": "three"})
        self.assertEquals(ret, "ok")

    def testGenericReturn(self):
        def h(arg):
            if arg == 0:
                return "the-string"
            elif arg == 1:
                return 123
            elif arg == 2:
                return True
            elif arg == 3:
                return { "foo": "foo_value" }
            elif arg == 4:
                return ["foo", "bar"]
            else:
                return None
        ret = obj.method_with_generic_return(h)
        self.assertEquals(ret, "ok")

    def testGenericUserTypeReturn(self):
        ret = obj.method_with_generic_user_type_return(lambda x : x)
        self.assertEquals(ret, "ok")

    def testNullableListReturn(self):
        # Cannot pass because nullable return is not implemented
        pass
