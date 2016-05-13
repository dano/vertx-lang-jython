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

TestDataObject = util.jvm.io.vertx.codegen.testmodel.TestDataObject

class FunctionParamTCK(object):
    """
    
    """
    def __init__(self, jval):
        self.jfunctionParamTCK = jval

    def method_with_basic_param(self, byte_func, short_func, integer_func, long_func, float_func, double_func, boolean_func, char_func, string_func):
        """"""
        return list([elt for elt in self.jfunctionParamTCK.methodWithBasicParam(byte_func._jdel, short_func._jdel, integer_func._jdel, long_func._jdel, float_func._jdel, double_func._jdel, boolean_func._jdel, char_func._jdel, string_func._jdel)])

    def method_with_json_param(self, object_func, array_func):
        """"""
        return list([elt for elt in self.jfunctionParamTCK.methodWithJsonParam(object_func._jdel, array_func._jdel)])

    def method_with_void_param(self, func):
        """"""
        return self.jfunctionParamTCK.methodWithVoidParam(func._jdel)

    def method_with_user_type_param(self, arg, func):
        """"""
        return self.jfunctionParamTCK.methodWithUserTypeParam(arg._jdel, func._jdel)

    def method_with_object_param(self, arg, func):
        """"""
        return self.jfunctionParamTCK.methodWithObjectParam(util.python_to_java(arg), func._jdel)

    def method_with_data_object_param(self, func):
        """"""
        return self.jfunctionParamTCK.methodWithDataObjectParam(func._jdel)

    def method_with_enum_param(self, func):
        """"""
        return self.jfunctionParamTCK.methodWithEnumParam(func._jdel)

    def method_with_list_param(self, string_func):
        """"""
        return self.jfunctionParamTCK.methodWithListParam(string_func._jdel)

    def method_with_set_param(self, func):
        """"""
        return self.jfunctionParamTCK.methodWithSetParam(func._jdel)

    def method_with_map_param(self, func):
        """"""
        return self.jfunctionParamTCK.methodWithMapParam(func._jdel)

    def method_with_generic_param(self, t, func):
        """"""
        return self.jfunctionParamTCK.methodWithGenericParam(util.python_to_java(t), func._jdel)

    def method_with_generic_user_type_param(self, t, func):
        """"""
        return self.jfunctionParamTCK.methodWithGenericUserTypeParam(util.python_to_java(t), func._jdel)

    def method_with_basic_return(self, byte_func, short_func, integer_func, long_func, float_func, double_func, boolean_func, char_func, string_func):
        """"""
        return self.jfunctionParamTCK.methodWithBasicReturn(byte_func._jdel, short_func._jdel, integer_func._jdel, long_func._jdel, float_func._jdel, double_func._jdel, boolean_func._jdel, char_func._jdel, string_func._jdel)

    def method_with_json_return(self, object_func, array_func):
        """"""
        return self.jfunctionParamTCK.methodWithJsonReturn(object_func._jdel, array_func._jdel)

    def method_with_object_return(self, func):
        """"""
        return self.jfunctionParamTCK.methodWithObjectReturn(func._jdel)

    def method_with_data_object_return(self, func):
        """"""
        return self.jfunctionParamTCK.methodWithDataObjectReturn(func._jdel)

    def method_with_enum_return(self, func):
        """"""
        return self.jfunctionParamTCK.methodWithEnumReturn(func._jdel)

    def method_with_list_return(self, func):
        """"""
        return self.jfunctionParamTCK.methodWithListReturn(func._jdel)

    def method_with_set_return(self, func):
        """"""
        return self.jfunctionParamTCK.methodWithSetReturn(func._jdel)

    def method_with_map_return(self, func):
        """"""
        return self.jfunctionParamTCK.methodWithMapReturn(func._jdel)

    def method_with_generic_return(self, func):
        """"""
        return self.jfunctionParamTCK.methodWithGenericReturn(func._jdel)

    def method_with_generic_user_type_return(self, func):
        """"""
        return self.jfunctionParamTCK.methodWithGenericUserTypeReturn(func._jdel)

    def method_with_nullable_list_param(self, func):
        """"""
        return self.jfunctionParamTCK.methodWithNullableListParam(func._jdel)

    def method_with_nullable_list_return(self, func):
        """"""
        return self.jfunctionParamTCK.methodWithNullableListReturn(func._jdel)

    @property
    def _jdel(self):
        return self.jfunctionParamTCK

