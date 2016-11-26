package io.vertx.test.lang.jython;

import io.vertx.core.DeploymentOptions;
import io.vertx.core.json.JsonObject;
import io.vertx.test.core.VertxTestBase;
import org.junit.Test;

import java.io.File;

import static org.junit.Assert.assertEquals;

/**
 * @author <a href="mailto:julien@julienviet.com">Julien Viet</a>
 */
public class DeployTest extends VertxTestBase {

  private static volatile int deployedCount;
  private static volatile int startedCount;
  private static volatile int stoppedCount;

  public static void deployed() {
    deployedCount++;
  }
  public static void started() {
    startedCount++;
  }
  public static void stopped() {
    stoppedCount++;
  }

  @Override
  public void setUp() throws Exception {
    super.setUp();
    deployedCount = 0;
    startedCount = 0;
    stoppedCount = 0;
  }

  @Test
  public void testDeployRubyVerticle() {
    vertx.deployVerticle("simple_verticle.py", ar -> {
      assertTrue(ar.succeeded());
      assertEquals(1, deployedCount);
      testComplete();
    });
    await();
  }

  @Test
  public void testDeployAbsentVerticle() {
    vertx.deployVerticle("doesnotexists.py", ar -> {
      assertTrue(ar.failed());
      testComplete();
    });
    await();
  }

  @Test
  public void testVerticleLifecycle() {
    vertx.deployVerticle("lifecycle_verticle.py", ar -> {
      assertTrue(ar.succeeded());
      assertEquals(1, deployedCount);
      assertEquals(1, startedCount);
      assertEquals(0, stoppedCount);
      vertx.undeploy(ar.result(), ar2 -> {
        assertTrue(ar2.succeeded());
        assertEquals(1, deployedCount);
        assertEquals(1, startedCount);
        assertEquals(1, stoppedCount);
        testComplete();
      });
    });
    await();
  }

  @Test
  public void testAsyncVerticleLifecycle() {
    vertx.deployVerticle("async_lifecycle_verticle.py", ar -> {
      assertTrue(ar.succeeded());
      assertEquals(1, deployedCount);
      assertEquals(1, startedCount);
      assertEquals(0, stoppedCount);
      vertx.undeploy(ar.result(), ar2 -> {
        assertTrue(ar2.succeeded());
        assertEquals(1, deployedCount);
        assertEquals(1, startedCount);
        assertEquals(1, stoppedCount);
        testComplete();
      });
    });
    await();
  }

  @Test
  public void testVerticleRaisingErrorInRun() {
    vertx.deployVerticle("verticle_raising_error_in_run.py", ar -> {
      assertFalse(ar.succeeded());
      assertEquals(1, deployedCount);
      assertEquals(0, startedCount);
      assertEquals(0, stoppedCount);
      testComplete();
    });
    await();
  }

  @Test
  public void testVerticleRaisingErrorInStart() {
    vertx.deployVerticle("verticle_raising_error_in_start.py", ar -> {
      assertFalse(ar.succeeded());
      assertEquals(1, deployedCount);
      assertEquals(1, startedCount);
      assertEquals(0, stoppedCount);
      testComplete();
    });
    await();
  }

  @Test
  public void testVerticleRaisingErrorInStop() {
    vertx.deployVerticle("verticle_raising_error_in_stop.py", ar -> {
      assertTrue(ar.succeeded());
      assertEquals(1, deployedCount);
      assertEquals(1, startedCount);
      assertEquals(0, stoppedCount);
      vertx.undeploy(ar.result(), ar2 -> {
        assertTrue(ar.succeeded());
        assertEquals(1, deployedCount);
        assertEquals(1, startedCount);
        assertEquals(1, stoppedCount);
        testComplete();
      });
    });
    await();
  }

  @Test
  public void testVerticleRaisingErrorInAsyncStart() {
    vertx.deployVerticle("verticle_raising_error_in_async_start.py", ar -> {
      assertFalse(ar.succeeded());
      assertEquals(1, deployedCount);
      assertEquals(1, startedCount);
      assertEquals(0, stoppedCount);
      testComplete();
    });
    await();
  }

  @Test
  public void testVerticleRaisingErrorInAsyncStop() {
    vertx.deployVerticle("verticle_raising_error_in_async_stop.py", ar -> {
      assertTrue(ar.succeeded());
      assertEquals(1, deployedCount);
      assertEquals(1, startedCount);
      assertEquals(0, stoppedCount);
      vertx.undeploy(ar.result(), ar2 -> {
        assertTrue(ar.succeeded());
        assertEquals(1, deployedCount);
        assertEquals(1, startedCount);
        assertEquals(1, stoppedCount);
        testComplete();
      });
    });
    await();
  }
}
