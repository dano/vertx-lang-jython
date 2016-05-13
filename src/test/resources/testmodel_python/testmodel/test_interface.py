# Copyright 2014 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import unicode_literals, print_function, absolute_import
from vertx_python import util
from vertx_python.compat import long, basestring, iteritems

util.vertx_init()

from testmodel_python.testmodel.generic_refed_interface import GenericRefedInterface
from testmodel_python.testmodel.refed_interface1 import RefedInterface1
from testmodel_python.testmodel.abstract_handler_user_type import AbstractHandlerUserType
from testmodel_python.testmodel.concrete_handler_user_type import ConcreteHandlerUserType
from testmodel_python.testmodel.concrete_handler_user_type_extension import ConcreteHandlerUserTypeExtension
from testmodel_python.testmodel.super_interface1 import SuperInterface1
from testmodel_python.testmodel.refed_interface2 import RefedInterface2
from testmodel_python.testmodel.super_interface2 import SuperInterface2

TestDataObject = util.jvm.io.vertx.codegen.testmodel.TestDataObject

class TestInterface(SuperInterface1, SuperInterface2, object):
    """
    
    """
    def __init__(self, jval):
        self.jtestInterface = jval
        SuperInterface1.__init__(self, jval)
        SuperInterface2.__init__(self, jval)

    def other_super_method_with_basic_params(self, b, s, i, l, f, d, _bool, ch, _str):
        """"""
        if b is not None and isinstance(b, int) and s is not None and isinstance(s, int) and i is not None and isinstance(i, int) and l is not None and isinstance(l, int) and f is not None and isinstance(f, float) and d is not None and isinstance(d, float) and _bool is not None and isinstance(_bool, bool) and ch is not None and isinstance(ch, (basestring, int)) and _str is not None and isinstance(_str, basestring):
            return util.java_to_python(self.jtestInterface.otherSuperMethodWithBasicParams(util.convert_byte_to_java(b), util.convert_short_to_java(s), i, util.convert_long_to_java(l), util.convert_float_to_java(f), util.convert_double_to_java(d), util.convert_boolean_to_java(_bool), util.convert_char_to_java(ch), _str), hashable=False)
        else:
            raise TypeError("Invalid arguments for other_super_method_with_basic_params")

    def method_with_basic_params(self, b, s, i, l, f, d, _bool, ch, _str):
        """"""
        if b is not None and isinstance(b, int) and s is not None and isinstance(s, int) and i is not None and isinstance(i, int) and l is not None and isinstance(l, int) and f is not None and isinstance(f, float) and d is not None and isinstance(d, float) and _bool is not None and isinstance(_bool, bool) and ch is not None and isinstance(ch, (basestring, int)) and _str is not None and isinstance(_str, basestring):
            return util.java_to_python(self.jtestInterface.methodWithBasicParams(util.convert_byte_to_java(b), util.convert_short_to_java(s), i, util.convert_long_to_java(l), util.convert_float_to_java(f), util.convert_double_to_java(d), util.convert_boolean_to_java(_bool), util.convert_char_to_java(ch), _str), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_basic_params")

    def method_with_basic_boxed_params(self, b, s, i, l, f, d, _bool, ch):
        """"""
        if b is not None and isinstance(b, int) and s is not None and isinstance(s, int) and i is not None and isinstance(i, int) and l is not None and isinstance(l, int) and f is not None and isinstance(f, float) and d is not None and isinstance(d, float) and _bool is not None and isinstance(_bool, bool) and ch is not None and isinstance(ch, (basestring, int)):
            return util.java_to_python(self.jtestInterface.methodWithBasicBoxedParams(util.convert_byte_to_java(b), util.convert_short_to_java(s), i, util.convert_long_to_java(l), util.convert_float_to_java(f), util.convert_double_to_java(d), util.convert_boolean_to_java(_bool), util.convert_char_to_java(ch)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_basic_boxed_params")

    def method_with_handler_basic_types(self, byte_handler, short_handler, int_handler, long_handler, float_handler, double_handler, boolean_handler, char_handler, string_handler):
        """"""
        if byte_handler is not None and callable(byte_handler) and short_handler is not None and callable(short_handler) and int_handler is not None and callable(int_handler) and long_handler is not None and callable(long_handler) and float_handler is not None and callable(float_handler) and double_handler is not None and callable(double_handler) and boolean_handler is not None and callable(boolean_handler) and char_handler is not None and callable(char_handler) and string_handler is not None and callable(string_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerBasicTypes(ByteHandler(byte_handler), ShortHandler(short_handler), IntegerHandler(int_handler), LongHandler(long_handler), FloatHandler(float_handler), DoubleHandler(double_handler), BooleanHandler(boolean_handler), CharacterHandler(char_handler), StringHandler(string_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_basic_types")

    def method_with_handler_async_result_byte(self, send_failure, handler):
        """"""
        if send_failure is not None and isinstance(send_failure, bool) and handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultByte(util.convert_boolean_to_java(send_failure), AsyncByteHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_byte")

    def method_with_handler_async_result_short(self, send_failure, handler):
        """"""
        if send_failure is not None and isinstance(send_failure, bool) and handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultShort(util.convert_boolean_to_java(send_failure), AsyncShortHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_short")

    def method_with_handler_async_result_integer(self, send_failure, handler):
        """"""
        if send_failure is not None and isinstance(send_failure, bool) and handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultInteger(util.convert_boolean_to_java(send_failure), AsyncIntegerHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_integer")

    def method_with_handler_async_result_long(self, send_failure, handler):
        """"""
        if send_failure is not None and isinstance(send_failure, bool) and handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultLong(util.convert_boolean_to_java(send_failure), AsyncLongHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_long")

    def method_with_handler_async_result_float(self, send_failure, handler):
        """"""
        if send_failure is not None and isinstance(send_failure, bool) and handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultFloat(util.convert_boolean_to_java(send_failure), AsyncFloatHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_float")

    def method_with_handler_async_result_double(self, send_failure, handler):
        """"""
        if send_failure is not None and isinstance(send_failure, bool) and handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultDouble(util.convert_boolean_to_java(send_failure), AsyncDoubleHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_double")

    def method_with_handler_async_result_boolean(self, send_failure, handler):
        """"""
        if send_failure is not None and isinstance(send_failure, bool) and handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultBoolean(util.convert_boolean_to_java(send_failure), AsyncBooleanHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_boolean")

    def method_with_handler_async_result_character(self, send_failure, handler):
        """"""
        if send_failure is not None and isinstance(send_failure, bool) and handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultCharacter(util.convert_boolean_to_java(send_failure), AsyncCharacterHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_character")

    def method_with_handler_async_result_string(self, send_failure, handler):
        """"""
        if send_failure is not None and isinstance(send_failure, bool) and handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultString(util.convert_boolean_to_java(send_failure), AsyncStringHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_string")

    def method_with_handler_async_result_data_object(self, send_failure, handler):
        """"""
        if send_failure is not None and isinstance(send_failure, bool) and handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultDataObject(util.convert_boolean_to_java(send_failure), AsyncTestDataObjectHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_data_object")

    def method_with_user_types(self, refed):
        """"""
        return util.java_to_python(self.jtestInterface.methodWithUserTypes(refed._jdel), hashable=False)

    def method_with_object_param(self, _str, obj):
        """"""
        if _str is not None and isinstance(_str, basestring) and True:
            return util.java_to_python(self.jtestInterface.methodWithObjectParam(_str, util.python_to_java(obj)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_object_param")

    def method_with_data_object_param(self, **data_object):
        """"""
        if True:
            return util.java_to_python(self.jtestInterface.methodWithDataObjectParam(TestDataObject(util.dict_to_json(data_object)) if data_object is not None else None), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_data_object_param")

    def method_with_null_data_object_param(self, **data_object):
        """"""
        if True:
            return util.java_to_python(self.jtestInterface.methodWithNullDataObjectParam(TestDataObject(util.dict_to_json(data_object)) if data_object is not None else None), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_null_data_object_param")

    def method_with_list_params(self, list_string, list_byte, list_short, list_int, list_long, list_json_object, list_json_array, list_vertx_gen, list_data_object):
        """"""
        return util.java_to_python(self.jtestInterface.methodWithListParams(util.python_list_to_java([i for i in list_string] if list_string is not None else None), util.jvm.io.vertx.lang.python.TypeHelper.toByteList(util.python_list_to_java([util.convert_byte_to_java(i) for i in list_byte] if list_byte is not None else None)), util.jvm.io.vertx.lang.python.TypeHelper.toShortList(util.python_list_to_java([util.convert_short_to_java(i) for i in list_short] if list_short is not None else None)), util.python_list_to_java([i for i in list_int] if list_int is not None else None), util.python_list_to_java([util.convert_long_to_java(i) for i in list_long] if list_long is not None else None), util.python_list_to_java([util.dict_to_json(i) for i in list_json_object] if list_json_object is not None else None), util.python_list_to_java([util.list_to_json(i) for i in list_json_array] if list_json_array is not None else None), util.python_list_to_java([i._jdel for i in list_vertx_gen] if list_vertx_gen is not None else None), util.python_list_to_java([TestDataObject(util.dict_to_json(i)) if i is not None else None for i in list_data_object] if list_data_object is not None else None)), hashable=False)

    def method_with_set_params(self, set_string, set_byte, set_short, set_int, set_long, set_json_object, set_json_array, set_vertx_gen, set_data_object):
        """"""
        return util.java_to_python(self.jtestInterface.methodWithSetParams(util.python_set_to_java([i for i in set_string] if set_string is not None else None), util.jvm.io.vertx.lang.python.TypeHelper.toByteSet(util.python_set_to_java([util.convert_byte_to_java(i) for i in set_byte] if set_byte is not None else None)), util.jvm.io.vertx.lang.python.TypeHelper.toShortSet(util.python_set_to_java([util.convert_short_to_java(i) for i in set_short] if set_short is not None else None)), util.python_set_to_java([i for i in set_int] if set_int is not None else None), util.python_set_to_java([util.convert_long_to_java(i) for i in set_long] if set_long is not None else None), util.python_set_to_java([util.dict_to_json(i) for i in set_json_object] if set_json_object is not None else None), util.python_set_to_java([util.list_to_json(i) for i in set_json_array] if set_json_array is not None else None), util.python_set_to_java([i._jdel for i in set_vertx_gen] if set_vertx_gen is not None else None), util.python_set_to_java([TestDataObject(util.dict_to_json(i)) if i is not None else None for i in set_data_object] if set_data_object is not None else None)), hashable=False)

    def method_with_map_params(self, map_string, map_byte, map_short, map_int, map_long, map_json_object, map_json_array, map_vertx_gen):
        """"""
        return util.java_to_python(self.jtestInterface.methodWithMapParams(util.python_map_to_java({k:v for k,v in iteritems(map_string)}), util.jvm.io.vertx.lang.python.TypeHelper.toByteMap(util.python_map_to_java({k:util.convert_byte_to_java(v) for k,v in iteritems(map_byte)})), util.jvm.io.vertx.lang.python.TypeHelper.toShortMap(util.python_map_to_java({k:util.convert_short_to_java(v) for k,v in iteritems(map_short)})), util.python_map_to_java({k:v for k,v in iteritems(map_int)}), util.python_map_to_java({k:util.convert_long_to_java(v) for k,v in iteritems(map_long)}), util.python_map_to_java({k:util.dict_to_json(v) for k,v in iteritems(map_json_object)}), util.python_map_to_java({k:util.list_to_json(v) for k,v in iteritems(map_json_array)}), util.python_map_to_java({k:v._jdel for k,v in iteritems(map_vertx_gen)})), hashable=False)

    def method_with_handler_list_and_set(self, list_string_handler, list_int_handler, set_string_handler, set_int_handler):
        """"""
        if list_string_handler is not None and callable(list_string_handler) and list_int_handler is not None and callable(list_int_handler) and set_string_handler is not None and callable(set_string_handler) and set_int_handler is not None and callable(set_int_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerListAndSet(ListStringHandler(list_string_handler), ListIntegerHandler(list_int_handler), SetStringHandler(set_string_handler), SetIntegerHandler(set_int_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_list_and_set")

    def method_with_handler_async_result_list_string(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultListString(AsyncListStringHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_list_string")

    def method_with_handler_async_result_list_integer(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultListInteger(AsyncListIntegerHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_list_integer")

    def method_with_handler_async_result_set_string(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultSetString(AsyncSetStringHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_set_string")

    def method_with_handler_async_result_set_integer(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultSetInteger(AsyncSetIntegerHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_set_integer")

    def method_with_handler_list_vertx_gen(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerListVertxGen(ListRefedInterface1Handler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_list_vertx_gen")

    def method_with_handler_set_vertx_gen(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerSetVertxGen(SetRefedInterface1Handler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_set_vertx_gen")

    def method_with_handler_list_abstract_vertx_gen(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerListAbstractVertxGen(ListRefedInterface2Handler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_list_abstract_vertx_gen")

    def method_with_handler_set_abstract_vertx_gen(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerSetAbstractVertxGen(SetRefedInterface2Handler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_set_abstract_vertx_gen")

    def method_with_handler_list_json_object(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerListJsonObject(ListJsonObjectHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_list_json_object")

    def method_with_handler_list_null_json_object(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerListNullJsonObject(ListJsonObjectHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_list_null_json_object")

    def method_with_handler_list_complex_json_object(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerListComplexJsonObject(ListJsonObjectHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_list_complex_json_object")

    def method_with_handler_set_json_object(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerSetJsonObject(SetJsonObjectHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_set_json_object")

    def method_with_handler_set_null_json_object(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerSetNullJsonObject(SetJsonObjectHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_set_null_json_object")

    def method_with_handler_set_complex_json_object(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerSetComplexJsonObject(SetJsonObjectHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_set_complex_json_object")

    def method_with_handler_list_json_array(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerListJsonArray(ListJsonArrayHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_list_json_array")

    def method_with_handler_list_null_json_array(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerListNullJsonArray(ListJsonArrayHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_list_null_json_array")

    def method_with_handler_list_complex_json_array(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerListComplexJsonArray(ListJsonArrayHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_list_complex_json_array")

    def method_with_handler_set_json_array(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerSetJsonArray(SetJsonArrayHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_set_json_array")

    def method_with_handler_set_null_json_array(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerSetNullJsonArray(SetJsonArrayHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_set_null_json_array")

    def method_with_handler_set_complex_json_array(self, set_handler):
        """"""
        if set_handler is not None and callable(set_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerSetComplexJsonArray(SetJsonArrayHandler(set_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_set_complex_json_array")

    def method_with_handler_list_data_object(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerListDataObject(ListTestDataObjectHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_list_data_object")

    def method_with_handler_list_null_data_object(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerListNullDataObject(ListTestDataObjectHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_list_null_data_object")

    def method_with_handler_set_data_object(self, set_handler):
        """"""
        if set_handler is not None and callable(set_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerSetDataObject(SetTestDataObjectHandler(set_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_set_data_object")

    def method_with_handler_set_null_data_object(self, set_handler):
        """"""
        if set_handler is not None and callable(set_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerSetNullDataObject(SetTestDataObjectHandler(set_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_set_null_data_object")

    def method_with_handler_async_result_list_vertx_gen(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultListVertxGen(AsyncListRefedInterface1Handler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_list_vertx_gen")

    def method_with_handler_async_result_set_vertx_gen(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultSetVertxGen(AsyncSetRefedInterface1Handler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_set_vertx_gen")

    def method_with_handler_async_result_list_abstract_vertx_gen(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultListAbstractVertxGen(AsyncListRefedInterface2Handler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_list_abstract_vertx_gen")

    def method_with_handler_async_result_set_abstract_vertx_gen(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultSetAbstractVertxGen(AsyncSetRefedInterface2Handler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_set_abstract_vertx_gen")

    def method_with_handler_async_result_list_json_object(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultListJsonObject(AsyncListJsonObjectHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_list_json_object")

    def method_with_handler_async_result_list_null_json_object(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultListNullJsonObject(AsyncListJsonObjectHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_list_null_json_object")

    def method_with_handler_async_result_list_complex_json_object(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultListComplexJsonObject(AsyncListJsonObjectHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_list_complex_json_object")

    def method_with_handler_async_result_set_json_object(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultSetJsonObject(AsyncSetJsonObjectHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_set_json_object")

    def method_with_handler_async_result_set_null_json_object(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultSetNullJsonObject(AsyncSetJsonObjectHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_set_null_json_object")

    def method_with_handler_async_result_set_complex_json_object(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultSetComplexJsonObject(AsyncSetJsonObjectHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_set_complex_json_object")

    def method_with_handler_async_result_list_json_array(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultListJsonArray(AsyncListJsonArrayHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_list_json_array")

    def method_with_handler_async_result_list_null_json_array(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultListNullJsonArray(AsyncListJsonArrayHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_list_null_json_array")

    def method_with_handler_async_result_list_complex_json_array(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultListComplexJsonArray(AsyncListJsonArrayHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_list_complex_json_array")

    def method_with_handler_async_result_set_json_array(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultSetJsonArray(AsyncSetJsonArrayHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_set_json_array")

    def method_with_handler_async_result_set_null_json_array(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultSetNullJsonArray(AsyncSetJsonArrayHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_set_null_json_array")

    def method_with_handler_async_result_set_complex_json_array(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultSetComplexJsonArray(AsyncSetJsonArrayHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_set_complex_json_array")

    def method_with_handler_async_result_list_data_object(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultListDataObject(AsyncListTestDataObjectHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_list_data_object")

    def method_with_handler_async_result_list_null_data_object(self, list_handler):
        """"""
        if list_handler is not None and callable(list_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultListNullDataObject(AsyncListTestDataObjectHandler(list_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_list_null_data_object")

    def method_with_handler_async_result_set_data_object(self, set_handler):
        """"""
        if set_handler is not None and callable(set_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultSetDataObject(AsyncSetTestDataObjectHandler(set_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_set_data_object")

    def method_with_handler_async_result_set_null_data_object(self, set_handler):
        """"""
        if set_handler is not None and callable(set_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultSetNullDataObject(AsyncSetTestDataObjectHandler(set_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_set_null_data_object")

    def method_with_handler_user_types(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerUserTypes(RefedInterface1Handler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_user_types")

    def method_with_handler_async_result_user_types(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultUserTypes(AsyncRefedInterface1Handler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_user_types")

    def method_with_concrete_handler_user_type_subtype(self, handler):
        """"""
        return util.java_to_python(self.jtestInterface.methodWithConcreteHandlerUserTypeSubtype(handler._jdel), hashable=False)

    def method_with_abstract_handler_user_type_subtype(self, handler):
        """"""
        return util.java_to_python(self.jtestInterface.methodWithAbstractHandlerUserTypeSubtype(handler._jdel), hashable=False)

    def method_with_concrete_handler_user_type_subtype_extension(self, handler):
        """"""
        return util.java_to_python(self.jtestInterface.methodWithConcreteHandlerUserTypeSubtypeExtension(handler._jdel), hashable=False)

    def method_with_handler_void(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerVoid(VoidHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_void")

    def method_with_handler_async_result_void(self, send_failure, handler):
        """"""
        if send_failure is not None and isinstance(send_failure, bool) and handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultVoid(util.convert_boolean_to_java(send_failure), AsyncVoidHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_void")

    def method_with_handler_throwable(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerThrowable(ThrowableHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_throwable")

    def method_with_handler_data_object(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerDataObject(TestDataObjectHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_data_object")

    def method_with_handler_generic_user_type(self, value, handler):
        """"""
        if True and handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerGenericUserType(util.python_to_java(value), GenericRefedInterfaceHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_generic_user_type")

    def method_with_handler_async_result_generic_user_type(self, value, handler):
        """"""
        if True and handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultGenericUserType(util.python_to_java(value), AsyncGenericRefedInterfaceHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_generic_user_type")

    def method_with_byte_return(self):
        """"""
        return self.jtestInterface.methodWithByteReturn()

    def method_with_short_return(self):
        """"""
        return self.jtestInterface.methodWithShortReturn()

    def method_with_int_return(self):
        """"""
        return self.jtestInterface.methodWithIntReturn()

    def method_with_long_return(self):
        """"""
        return self.jtestInterface.methodWithLongReturn()

    def method_with_float_return(self):
        """"""
        return self.jtestInterface.methodWithFloatReturn()

    def method_with_double_return(self):
        """"""
        return self.jtestInterface.methodWithDoubleReturn()

    def method_with_boolean_return(self):
        """"""
        return self.jtestInterface.methodWithBooleanReturn()

    def method_with_char_return(self):
        """"""
        return self.jtestInterface.methodWithCharReturn()

    def method_with_string_return(self):
        """"""
        return self.jtestInterface.methodWithStringReturn()

    def method_with_vertx_gen_return(self):
        """"""
        return util.handle_none(self.jtestInterface.methodWithVertxGenReturn(), RefedInterface1)

    def method_with_vertx_gen_null_return(self):
        """"""
        return util.handle_none(self.jtestInterface.methodWithVertxGenNullReturn(), RefedInterface1)

    def method_with_abstract_vertx_gen_return(self):
        """"""
        return util.handle_none(self.jtestInterface.methodWithAbstractVertxGenReturn(), RefedInterface2)

    def method_with_data_object_return(self):
        """"""
        return util.data_object_to_json(self.jtestInterface.methodWithDataObjectReturn(), hashable=False)

    def method_with_data_object_null_return(self):
        """"""
        return util.data_object_to_json(self.jtestInterface.methodWithDataObjectNullReturn(), hashable=False)

    def overloaded_method(self, _str, refed=None, handler=None, period=None):
        """"""
        if handler is None and period is None and _str is not None and isinstance(_str, basestring) and refed is not None:
            return self.jtestInterface.overloadedMethod(_str, refed._jdel)
        elif period is None and _str is not None and isinstance(_str, basestring) and refed is not None and handler is not None and callable(handler):
            return self.jtestInterface.overloadedMethod(_str, refed._jdel, StringHandler(handler))
        elif _str is not None and isinstance(_str, basestring) and refed is not None and period is not None and isinstance(period, int) and handler is not None and callable(handler):
            return self.jtestInterface.overloadedMethod(_str, refed._jdel, util.convert_long_to_java(period), StringHandler(handler))
        elif refed is None and period is None and _str is not None and isinstance(_str, basestring) and handler is not None and callable(handler):
            return self.jtestInterface.overloadedMethod(_str, StringHandler(handler))
        else:
            raise TypeError("Invalid arguments for overloaded_method")

    def method_with_generic_return(self, type):
        """"""
        if type is not None and isinstance(type, basestring):
            return util.java_to_python(self.jtestInterface.methodWithGenericReturn(type), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_generic_return")

    def method_with_generic_param(self, type, u):
        """"""
        if type is not None and isinstance(type, basestring) and True:
            return util.java_to_python(self.jtestInterface.methodWithGenericParam(type, util.python_to_java(u)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_generic_param")

    def method_with_generic_handler(self, type, handler):
        """"""
        if type is not None and isinstance(type, basestring) and handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithGenericHandler(type, UHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_generic_handler")

    def method_with_generic_handler_async_result(self, type, async_result_handler):
        """"""
        if type is not None and isinstance(type, basestring) and async_result_handler is not None and callable(async_result_handler):
            return util.java_to_python(self.jtestInterface.methodWithGenericHandlerAsyncResult(type, AsyncUHandler(async_result_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_generic_handler_async_result")

    def fluent_method(self, _str):
        """"""
        if _str is not None and isinstance(_str, basestring):
            self.jtestInterface.fluentMethod(_str)
        else:
            raise TypeError("Invalid arguments for fluent_method")
        return self

    @util.cached
    def method_with_cached_return(self, foo):
        """"""
        if foo is not None and isinstance(foo, basestring):
            return util.handle_none(self.jtestInterface.methodWithCachedReturn(foo), RefedInterface1)
        else:
            raise TypeError("Invalid arguments for method_with_cached_return")

    @util.cached
    def method_with_cached_return_primitive(self, arg):
        """"""
        if arg is not None and isinstance(arg, int):
            return self.jtestInterface.methodWithCachedReturnPrimitive(arg)
        else:
            raise TypeError("Invalid arguments for method_with_cached_return_primitive")

    def method_with_json_object_return(self):
        """"""
        return util.java_to_python(self.jtestInterface.methodWithJsonObjectReturn(), hashable=False)

    def method_with_null_json_object_return(self):
        """"""
        return util.java_to_python(self.jtestInterface.methodWithNullJsonObjectReturn(), hashable=False)

    def method_with_complex_json_object_return(self):
        """"""
        return util.java_to_python(self.jtestInterface.methodWithComplexJsonObjectReturn(), hashable=False)

    def method_with_json_array_return(self):
        """"""
        return util.java_to_python(self.jtestInterface.methodWithJsonArrayReturn(), hashable=False)

    def method_with_null_json_array_return(self):
        """"""
        return util.java_to_python(self.jtestInterface.methodWithNullJsonArrayReturn(), hashable=False)

    def method_with_complex_json_array_return(self):
        """"""
        return util.java_to_python(self.jtestInterface.methodWithComplexJsonArrayReturn(), hashable=False)

    def method_with_json_params(self, json_object, json_array):
        """"""
        if json_object is not None and isinstance(json_object, dict) and json_array is not None and isinstance(json_array, (list, tuple)):
            return util.java_to_python(self.jtestInterface.methodWithJsonParams(util.dict_to_json(json_object), util.list_to_json(json_array)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_json_params")

    def method_with_null_json_params(self, json_object, json_array):
        """"""
        if json_object is not None and isinstance(json_object, dict) and json_array is not None and isinstance(json_array, (list, tuple)):
            return util.java_to_python(self.jtestInterface.methodWithNullJsonParams(util.dict_to_json(json_object), util.list_to_json(json_array)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_null_json_params")

    def method_with_handler_json(self, json_object_handler, json_array_handler):
        """"""
        if json_object_handler is not None and callable(json_object_handler) and json_array_handler is not None and callable(json_array_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerJson(JsonObjectHandler(json_object_handler), JsonArrayHandler(json_array_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_json")

    def method_with_handler_null_json(self, json_object_handler, json_array_handler):
        """"""
        if json_object_handler is not None and callable(json_object_handler) and json_array_handler is not None and callable(json_array_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerNullJson(JsonObjectHandler(json_object_handler), JsonArrayHandler(json_array_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_null_json")

    def method_with_handler_complex_json(self, json_object_handler, json_array_handler):
        """"""
        if json_object_handler is not None and callable(json_object_handler) and json_array_handler is not None and callable(json_array_handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerComplexJson(JsonObjectHandler(json_object_handler), JsonArrayHandler(json_array_handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_complex_json")

    def method_with_handler_async_result_json_object(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultJsonObject(AsyncJsonObjectHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_json_object")

    def method_with_handler_async_result_null_json_object(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultNullJsonObject(AsyncJsonObjectHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_null_json_object")

    def method_with_handler_async_result_complex_json_object(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultComplexJsonObject(AsyncJsonObjectHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_complex_json_object")

    def method_with_handler_async_result_json_array(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultJsonArray(AsyncJsonArrayHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_json_array")

    def method_with_handler_async_result_null_json_array(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultNullJsonArray(AsyncJsonArrayHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_null_json_array")

    def method_with_handler_async_result_complex_json_array(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_to_python(self.jtestInterface.methodWithHandlerAsyncResultComplexJsonArray(AsyncJsonArrayHandler(handler)), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_handler_async_result_complex_json_array")

    def method_with_map_return(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_map_to_python(self.jtestInterface.methodWithMapReturn(StringHandler(handler)), lambda x:x, lambda y:y)
        else:
            raise TypeError("Invalid arguments for method_with_map_return")

    def method_with_map_string_return(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_map_to_python(self.jtestInterface.methodWithMapStringReturn(StringHandler(handler)), lambda x:x, lambda y:y)
        else:
            raise TypeError("Invalid arguments for method_with_map_string_return")

    def method_with_map_long_return(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_map_to_python(self.jtestInterface.methodWithMapLongReturn(StringHandler(handler)), lambda x:x, lambda y:util.convert_long_to_java(y))
        else:
            raise TypeError("Invalid arguments for method_with_map_long_return")

    def method_with_map_integer_return(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_map_to_python(self.jtestInterface.methodWithMapIntegerReturn(StringHandler(handler)), lambda x:x, lambda y:y)
        else:
            raise TypeError("Invalid arguments for method_with_map_integer_return")

    def method_with_map_short_return(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_map_to_python(self.jtestInterface.methodWithMapShortReturn(StringHandler(handler)), lambda x:x, lambda y:util.convert_short_to_java(y))
        else:
            raise TypeError("Invalid arguments for method_with_map_short_return")

    def method_with_map_byte_return(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_map_to_python(self.jtestInterface.methodWithMapByteReturn(StringHandler(handler)), lambda x:x, lambda y:util.convert_byte_to_java(y))
        else:
            raise TypeError("Invalid arguments for method_with_map_byte_return")

    def method_with_map_character_return(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_map_to_python(self.jtestInterface.methodWithMapCharacterReturn(StringHandler(handler)), lambda x:x, lambda y:util.convert_char_to_java(y))
        else:
            raise TypeError("Invalid arguments for method_with_map_character_return")

    def method_with_map_boolean_return(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_map_to_python(self.jtestInterface.methodWithMapBooleanReturn(StringHandler(handler)), lambda x:x, lambda y:util.convert_boolean_to_java(y))
        else:
            raise TypeError("Invalid arguments for method_with_map_boolean_return")

    def method_with_map_float_return(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_map_to_python(self.jtestInterface.methodWithMapFloatReturn(StringHandler(handler)), lambda x:x, lambda y:util.convert_float_to_java(y))
        else:
            raise TypeError("Invalid arguments for method_with_map_float_return")

    def method_with_map_double_return(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_map_to_python(self.jtestInterface.methodWithMapDoubleReturn(StringHandler(handler)), lambda x:x, lambda y:util.convert_double_to_java(y))
        else:
            raise TypeError("Invalid arguments for method_with_map_double_return")

    def method_with_map_json_object_return(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_map_to_python(self.jtestInterface.methodWithMapJsonObjectReturn(StringHandler(handler)), lambda x:util.java_to_python(x, hashable=False), lambda y:util.dict_to_json(y))
        else:
            raise TypeError("Invalid arguments for method_with_map_json_object_return")

    def method_with_map_complex_json_object_return(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_map_to_python(self.jtestInterface.methodWithMapComplexJsonObjectReturn(StringHandler(handler)), lambda x:util.java_to_python(x, hashable=False), lambda y:util.dict_to_json(y))
        else:
            raise TypeError("Invalid arguments for method_with_map_complex_json_object_return")

    def method_with_map_json_array_return(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_map_to_python(self.jtestInterface.methodWithMapJsonArrayReturn(StringHandler(handler)), lambda x:util.java_to_python(x, hashable=False), lambda y:util.list_to_json(y))
        else:
            raise TypeError("Invalid arguments for method_with_map_json_array_return")

    def method_with_map_complex_json_array_return(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.java_map_to_python(self.jtestInterface.methodWithMapComplexJsonArrayReturn(StringHandler(handler)), lambda x:util.java_to_python(x, hashable=False), lambda y:util.list_to_json(y))
        else:
            raise TypeError("Invalid arguments for method_with_map_complex_json_array_return")

    def method_with_null_map_return(self):
        """"""
        return util.java_map_to_python(self.jtestInterface.methodWithNullMapReturn(), lambda x:x, lambda y:y)

    def method_with_list_string_return(self):
        """"""
        return list([elt for elt in self.jtestInterface.methodWithListStringReturn()])

    def method_with_list_long_return(self):
        """"""
        return list([elt for elt in self.jtestInterface.methodWithListLongReturn()])

    def method_with_list_vertx_gen_return(self):
        """"""
        return list([util.handle_none(elt, RefedInterface1) for elt in self.jtestInterface.methodWithListVertxGenReturn()])

    def method_with_list_json_object_return(self):
        """"""
        return list([util.java_to_python(elt, hashable=False) for elt in self.jtestInterface.methodWithListJsonObjectReturn()])

    def method_with_list_complex_json_object_return(self):
        """"""
        return list([util.java_to_python(elt, hashable=False) for elt in self.jtestInterface.methodWithListComplexJsonObjectReturn()])

    def method_with_list_json_array_return(self):
        """"""
        return list([util.java_to_python(elt, hashable=False) for elt in self.jtestInterface.methodWithListJsonArrayReturn()])

    def method_with_list_complex_json_array_return(self):
        """"""
        return list([util.java_to_python(elt, hashable=False) for elt in self.jtestInterface.methodWithListComplexJsonArrayReturn()])

    def method_with_list_data_object_return(self):
        """"""
        return list([util.data_object_to_json(elt, hashable=False) for elt in self.jtestInterface.methodWithListDataObjectReturn()])

    def method_with_null_list_return(self):
        """"""
        return list([elt for elt in self.jtestInterface.methodWithNullListReturn()])

    def method_with_set_string_return(self):
        """"""
        return set([elt for elt in self.jtestInterface.methodWithSetStringReturn()])

    def method_with_set_long_return(self):
        """"""
        return set([elt for elt in self.jtestInterface.methodWithSetLongReturn()])

    def method_with_set_vertx_gen_return(self):
        """"""
        return set([util.handle_none(elt, RefedInterface1) for elt in self.jtestInterface.methodWithSetVertxGenReturn()])

    def method_with_set_json_object_return(self):
        """"""
        return set([util.java_to_python(elt, hashable=True) for elt in self.jtestInterface.methodWithSetJsonObjectReturn()])

    def method_with_set_complex_json_object_return(self):
        """"""
        return set([util.java_to_python(elt, hashable=True) for elt in self.jtestInterface.methodWithSetComplexJsonObjectReturn()])

    def method_with_set_json_array_return(self):
        """"""
        return set([util.java_to_python(elt, hashable=True) for elt in self.jtestInterface.methodWithSetJsonArrayReturn()])

    def method_with_set_complex_json_array_return(self):
        """"""
        return set([util.java_to_python(elt, hashable=True) for elt in self.jtestInterface.methodWithSetComplexJsonArrayReturn()])

    def method_with_set_data_object_return(self):
        """"""
        return set([util.data_object_to_json(elt, hashable=True) for elt in self.jtestInterface.methodWithSetDataObjectReturn()])

    def method_with_null_set_return(self):
        """"""
        return set([elt for elt in self.jtestInterface.methodWithNullSetReturn()])

    def method_with_enum_param(self, str_val, weirdo):
        """"""
        if str_val is not None and isinstance(str_val, basestring) and True:
            return self.jtestInterface.methodWithEnumParam(str_val, util.jvm.io.vertx.codegen.testmodel.TestEnum.valueOf(weirdo))
        else:
            raise TypeError("Invalid arguments for method_with_enum_param")

    def method_with_enum_return(self, str_val):
        """"""
        if str_val is not None and isinstance(str_val, basestring):
            return self.jtestInterface.methodWithEnumReturn(str_val).toString()
        else:
            raise TypeError("Invalid arguments for method_with_enum_return")

    def method_with_throwable_return(self, str_val):
        """"""
        if str_val is not None and isinstance(str_val, basestring):
            return util.java_to_python(self.jtestInterface.methodWithThrowableReturn(str_val), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_throwable_return")

    def method_with_throwable_param(self, t):
        """"""
        return self.jtestInterface.methodWithThrowableParam(t._jdel)

    @property
    def _jdel(self):
        return self.jtestInterface

    @classmethod
    def static_factory_method(self, foo):
        """"""
        if foo is not None and isinstance(foo, basestring):
            return util.handle_none(util.jvm.io.vertx.codegen.testmodel.TestInterface.staticFactoryMethod(foo), RefedInterface1)
        else:
            raise TypeError("Invalid arguments for static_factory_method")

class ByteHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(result)
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class ShortHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(result)
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class IntegerHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(result)
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class LongHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(result)
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class FloatHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(result)
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class DoubleHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(result)
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class BooleanHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(result)
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class CharacterHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(result)
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class StringHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(result)
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncByteHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(result.result(), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncShortHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(result.result(), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncIntegerHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(result.result(), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncLongHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(result.result(), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncFloatHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(result.result(), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncDoubleHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(result.result(), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncBooleanHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(result.result(), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncCharacterHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(result.result(), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncStringHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(result.result(), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncTestDataObjectHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(util.data_object_to_json(result.result(), hashable=False), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class ListStringHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(list([elt for elt in result]))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class ListIntegerHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(list([elt for elt in result]))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class SetStringHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(set([elt for elt in result]))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class SetIntegerHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(set([elt for elt in result]))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncListStringHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(list([elt for elt in result.result()]), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncListIntegerHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(list([elt for elt in result.result()]), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncSetStringHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(set([elt for elt in result.result()]), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncSetIntegerHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(set([elt for elt in result.result()]), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class ListRefedInterface1Handler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(list([util.handle_none(elt, RefedInterface1) for elt in result]))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class SetRefedInterface1Handler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(set([util.handle_none(elt, RefedInterface1) for elt in result]))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class ListRefedInterface2Handler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(list([util.handle_none(elt, RefedInterface2) for elt in result]))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class SetRefedInterface2Handler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(set([util.handle_none(elt, RefedInterface2) for elt in result]))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class ListJsonObjectHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(list([util.java_to_python(elt, hashable=False) for elt in result]))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class SetJsonObjectHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(set([util.java_to_python(elt, hashable=True) for elt in result]))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class ListJsonArrayHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(list([util.java_to_python(elt, hashable=False) for elt in result]))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class SetJsonArrayHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(set([util.java_to_python(elt, hashable=True) for elt in result]))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class ListTestDataObjectHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(list([util.data_object_to_json(elt, hashable=False) for elt in result]))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class SetTestDataObjectHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(set([util.data_object_to_json(elt, hashable=True) for elt in result]))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncListRefedInterface1Handler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(list([util.handle_none(elt, RefedInterface1) for elt in result.result()]), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncSetRefedInterface1Handler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(set([util.handle_none(elt, RefedInterface1) for elt in result.result()]), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncListRefedInterface2Handler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(list([util.handle_none(elt, RefedInterface2) for elt in result.result()]), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncSetRefedInterface2Handler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(set([util.handle_none(elt, RefedInterface2) for elt in result.result()]), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncListJsonObjectHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(list([util.java_to_python(elt, hashable=False) for elt in result.result()]), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncSetJsonObjectHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(set([util.java_to_python(elt, hashable=True) for elt in result.result()]), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncListJsonArrayHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(list([util.java_to_python(elt, hashable=False) for elt in result.result()]), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncSetJsonArrayHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(set([util.java_to_python(elt, hashable=True) for elt in result.result()]), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncListTestDataObjectHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(list([util.data_object_to_json(elt, hashable=False) for elt in result.result()]), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncSetTestDataObjectHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(set([util.data_object_to_json(elt, hashable=True) for elt in result.result()]), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class RefedInterface1Handler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(util.handle_none(result, RefedInterface1))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncRefedInterface1Handler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(util.handle_none(result.result(), RefedInterface1), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class VoidHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(None)
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncVoidHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(None, None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class ThrowableHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(util.java_to_python(result, hashable=False))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class TestDataObjectHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(util.data_object_to_json(result, hashable=False))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class GenericRefedInterfaceHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(util.handle_none(result, GenericRefedInterface))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncGenericRefedInterfaceHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(util.handle_none(result.result(), GenericRefedInterface), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class UHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(util.java_to_python(result, hashable=False))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncUHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(util.java_to_python(result.result(), hashable=False), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class JsonObjectHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(util.java_to_python(result, hashable=False))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class JsonArrayHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            self.handler(util.java_to_python(result, hashable=False))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncJsonObjectHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(util.java_to_python(result.result(), hashable=False), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

class AsyncJsonArrayHandler(object):
    class Java:
        implements = ['io.vertx.core.Handler']
    def __init__(self, handler):
        self.handler = handler
    def handle(self, result):
        try:
            if result.succeeded():
                self.handler(util.java_to_python(result.result(), hashable=False), None)
            else:
                self.handler(None, util.VertxException(result.cause().getMessage()))
        except Exception:
            import traceback
            traceback.print_exc()
            raise

