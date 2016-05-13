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



class SubInterface(object):
    """
    
    """
    def __init__(self, jval):
        self.jsubInterface = jval

    def reverse(self, s):
        """"""
        if s is not None and isinstance(s, basestring):
            return self.jsubInterface.reverse(s)
        else:
            raise TypeError("Invalid arguments for reverse")

    @property
    def _jdel(self):
        return self.jsubInterface

