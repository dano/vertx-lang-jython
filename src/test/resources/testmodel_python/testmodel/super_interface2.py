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



class SuperInterface2(object):
    """
    
    """
    def __init__(self, jval):
        self.jsuperInterface2 = jval

    def other_super_method_with_basic_params(self, b, s, i, l, f, d, _bool, ch, _str):
        """"""
        if b is not None and isinstance(b, int) and s is not None and isinstance(s, int) and i is not None and isinstance(i, int) and l is not None and isinstance(l, int) and f is not None and isinstance(f, float) and d is not None and isinstance(d, float) and _bool is not None and isinstance(_bool, bool) and ch is not None and isinstance(ch, (basestring, int)) and _str is not None and isinstance(_str, basestring):
            return util.java_to_python(self.jsuperInterface2.otherSuperMethodWithBasicParams(util.convert_byte_to_java(b), util.convert_short_to_java(s), i, util.convert_long_to_java(l), util.convert_float_to_java(f), util.convert_double_to_java(d), util.convert_boolean_to_java(_bool), util.convert_char_to_java(ch), _str), hashable=False)
        else:
            raise TypeError("Invalid arguments for other_super_method_with_basic_params")

    @property
    def _jdel(self):
        return self.jsuperInterface2

