from __future__ import unicode_literals, print_function, absolute_import

import sys

if sys.version_info[0] < 3:
    long = long
    basestring = basestring
    unicode = unicode
    reduce = reduce
else:
    long = int
    basestring = str
    unicode = str
    from functools import reduce
