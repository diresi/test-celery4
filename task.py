from celery import Celery

POOL_METHOD = "prefork"
DEFAULT_BACKEND = "rpc://"
DEFAULT_BROKER = "amqp://guest:guest@rabbitmq//"
name = "test-app"

SERIALIZER = "pickle"
SERIALIZER = "yaml"

app = Celery(name, backend=DEFAULT_BACKEND, broker=DEFAULT_BROKER)
#app.conf.worker_pool = POOL_METHOD
#app.conf.task_serializer = SERIALIZER
#app.conf.result_serializer = SERIALIZER
#app.conf.accept_content = {SERIALIZER}
#app.conf.worker_redirect_stdouts = False
#app.conf.task_default_queue = name
#app.conf.task_default_exchange = name
#app.conf.task_default_routing_key = name
#app.conf.worker_hijack_root_logger = False

import datetime
@app.task
def echo():
    return datetime.datetime.now()

def test_echo():
    s = datetime.datetime.now()
    t = echo.delay().get()
    e = datetime.datetime.now()
    return s, t, e
