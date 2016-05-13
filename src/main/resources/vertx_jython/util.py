from __future__ import unicode_literals, print_function, absolute_import

from functools import partial, wraps


class VertxException(Exception):
    pass


def make_handler(fut):
    def handler_wrapper(result):
        print("result is {}".format(result))
        if result.succeeded():
            fut.set_result(result.result())
        else:
            fut.set_exception(result.cause())
    return handler_wrapper


def parse_array(old_parse_array, *args, **kwargs):
    values, end = old_parse_array(*args, **kwargs)
    return frozenset(values), end


def handle_none(obj, type_):
    return type_(obj) if obj is not None else obj

def cached(func):
    ''' Decorator for methods that need to cache results. '''
    dct = dict(cached_ret=None)
    @wraps(func)
    def inner(*args, **kwargs):
        if dct['cached_ret'] is None:
            dct['cached_ret'] = func(*args, **kwargs)
        return dct['cached_ret']
    return inner

