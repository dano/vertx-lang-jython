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

from acme_python.sub.sub_interface import SubInterface
from testmodel_python.testmodel.test_interface import TestInterface


class MyInterface(object):
    """
    
    """
    def __init__(self, jval):
        self.jmyInterface = jval

    def sub(self):
        """"""
        return util.handle_none(self.jmyInterface.sub(), SubInterface)

    def method(self):
        """"""
        return util.handle_none(self.jmyInterface.method(), TestInterface)

    @property
    def _jdel(self):
        return self.jmyInterface

    @classmethod
    def create(self):
        """"""
        return util.handle_none(util.jvm.com.acme.pkg.MyInterface.create(), MyInterface)

