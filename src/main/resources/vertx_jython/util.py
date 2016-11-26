from __future__ import unicode_literals, print_function, absolute_import

import json
from functools import partial, wraps

from io.vertx.core.json import JsonObject, JsonArray
from io.vertx.core import Future


class VertxException(Exception):
    pass


def make_handler(fut):
    def handler_wrapper(result):
        if result.succeeded():
            fut.set_result(result.result())
        else:
            fut.set_exception(result.cause())
    return handler_wrapper


def cb_wrapper(handler, converter):
    def cb(result):
        if result.succeeded():
            handler(converter(result.result()), None)
        else:
            handler(None, result.cause())
    return cb


def to_async_result(handler):
    def wrap(val, err=None):
        if err is not None:
            handler.handle(Future.failedFuture(err))
        else:
            handler.handle(Future.succeededFuture(val))
    return wrap


def to_handler(handler):
    def wrap(val):
        handler.handle(val)
    return wrap


def handle_none(obj, type_):
    return type_(obj) if obj is not None else obj


def obj_to_java(obj):
    if isinstance(obj, dict):
        return JsonObject(json.dumps(obj))
    if isinstance(obj, list):
        return JsonArray(json.dumps(obj))
    return obj



def cached(func):
    """ Decorator for methods that need to cache results. """
    dct = dict(cached_ret=None)
    @wraps(func)
    def inner(*args, **kwargs):
        if dct['cached_ret'] is None:
            dct['cached_ret'] = func(*args, **kwargs)
        return dct['cached_ret']
    return inner

