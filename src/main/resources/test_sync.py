import java
from vertx_jython.core.vertx import Vertx
from vertx_jython.futures import coroutine, VertxRunner

#def handler(result, err):
    #if err:
        #print("deploy verticle failed: {}".format(err))
        #v.close()
    #else:
        #print("got result {}".format(result))


@coroutine
def main():
    v = Vertx.vertx()
    print("got result {}".format(v))
    try:
        vid = yield v.deploy_verticle("madeup")
        print("got {}".format(vid))
    except (Exception, java.lang.Exception) as e:
        print("Caught ya {}".format(e))

if __name__ == "__main__":
    #v = Vertx.vertx()
    #v.deploy_verticle("madeup", handler)
    VertxRunner().run_until_complete(main())
