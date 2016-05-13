from futures import coroutine, VertxRunner, Future as _Future
import util
import io.vertx.core.Vertx as Vertx
import io.vertx.core.VertxOptions as VertxOptions

def clustered_vertx():
    fut = _Future()
    _method = util.make_handler(fut)
    Vertx.clusteredVertx(VertxOptions(), _method)
    return fut

def get_cluster_wide_map(shared_data, name):
    fut = _Future()
    _method = util.make_handler(fut)
    shared_data.getClusterWideMap(name, _method)
    return fut

@coroutine
def main():
    cv = yield clustered_vertx()
    print("got clustered vertx {}".format(cv))
    map1 = yield get_cluster_wide_map(cv.sharedData(), "mymap")
    print("got map {}".format(map1))

if __name__ == "__main__":
    VertxRunner().run_until_complete(main())
