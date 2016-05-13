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

from testmodel_python.testmodel.refed_interface1 import RefedInterface1
from testmodel_python.testmodel.concrete_handler_user_type import ConcreteHandlerUserType
from testmodel_python.testmodel.abstract_handler_user_type import AbstractHandlerUserType
from testmodel_python.testmodel.concrete_handler_user_type_extension import ConcreteHandlerUserTypeExtension


class Factory(object):
    """
    
    """
    def __init__(self, jval):
        self.jfactory = jval

    @property
    def _jdel(self):
        return self.jfactory

    @classmethod
    def create_concrete_handler_user_type(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.handle_none(util.jvm.io.vertx.codegen.testmodel.Factory.createConcreteHandlerUserType(RefedInterface1Handler(handler)), ConcreteHandlerUserType)
        else:
            raise TypeError("Invalid arguments for create_concrete_handler_user_type")

    @classmethod
    def create_abstract_handler_user_type(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.handle_none(util.jvm.io.vertx.codegen.testmodel.Factory.createAbstractHandlerUserType(RefedInterface1Handler(handler)), AbstractHandlerUserType)
        else:
            raise TypeError("Invalid arguments for create_abstract_handler_user_type")

    @classmethod
    def create_concrete_handler_user_type_extension(self, handler):
        """"""
        if handler is not None and callable(handler):
            return util.handle_none(util.jvm.io.vertx.codegen.testmodel.Factory.createConcreteHandlerUserTypeExtension(RefedInterface1Handler(handler)), ConcreteHandlerUserTypeExtension)
        else:
            raise TypeError("Invalid arguments for create_concrete_handler_user_type_extension")

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

