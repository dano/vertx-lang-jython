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


DataObjectWithMaps = util.jvm.io.vertx.codegen.testmodel.DataObjectWithMaps
DataObjectWithOnlyJsonObjectConstructor = util.jvm.io.vertx.codegen.testmodel.DataObjectWithOnlyJsonObjectConstructor
DataObjectWithLists = util.jvm.io.vertx.codegen.testmodel.DataObjectWithLists
DataObjectWithValues = util.jvm.io.vertx.codegen.testmodel.DataObjectWithValues

class DataObjectTCK(object):
    """
     todo:
     - Buffer support
    
    """
    def __init__(self, jval):
        self.jdataObjectTCK = jval

    def get_data_object_with_values(self):
        """"""
        return util.data_object_to_json(self.jdataObjectTCK.getDataObjectWithValues(), hashable=False)

    def set_data_object_with_values(self, **data_object):
        """"""
        if True:
            return util.java_to_python(self.jdataObjectTCK.setDataObjectWithValues(DataObjectWithValues(util.dict_to_json(data_object)) if data_object is not None else None), hashable=False)
        else:
            raise TypeError("Invalid arguments for set_data_object_with_values")

    def get_data_object_with_lists(self):
        """"""
        return util.data_object_to_json(self.jdataObjectTCK.getDataObjectWithLists(), hashable=False)

    def set_data_object_with_lists(self, **data_object):
        """"""
        if True:
            return util.java_to_python(self.jdataObjectTCK.setDataObjectWithLists(DataObjectWithLists(util.dict_to_json(data_object)) if data_object is not None else None), hashable=False)
        else:
            raise TypeError("Invalid arguments for set_data_object_with_lists")

    def get_data_object_with_maps(self):
        """"""
        return util.data_object_to_json(self.jdataObjectTCK.getDataObjectWithMaps(), hashable=False)

    def set_data_object_with_maps(self, **data_object):
        """"""
        if True:
            return util.java_to_python(self.jdataObjectTCK.setDataObjectWithMaps(DataObjectWithMaps(util.dict_to_json(data_object)) if data_object is not None else None), hashable=False)
        else:
            raise TypeError("Invalid arguments for set_data_object_with_maps")

    def method_with_only_json_object_constructor_data_object(self, **data_object):
        """"""
        if True:
            return util.java_to_python(self.jdataObjectTCK.methodWithOnlyJsonObjectConstructorDataObject(DataObjectWithOnlyJsonObjectConstructor(util.dict_to_json(data_object)) if data_object is not None else None), hashable=False)
        else:
            raise TypeError("Invalid arguments for method_with_only_json_object_constructor_data_object")

    @property
    def _jdel(self):
        return self.jdataObjectTCK

