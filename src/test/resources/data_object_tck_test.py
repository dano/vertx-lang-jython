import unittest

from testmodel_jython.testmodel.data_object_tck import DataObjectTCK

import io.vertx.codegen.testmodel.DataObjectTCKImpl

dobj_tck = DataObjectTCK(io.vertx.codegen.testmodel.DataObjectTCKImpl())


class TestDataObjTCKAPI(unittest.TestCase):

    def testMethodWithOnlyJsonObjectConstructorDataObject(self):
        data_object = {'foo':  'bar'}
        dobj_tck.method_with_only_json_object_constructor_data_object(**data_object)
