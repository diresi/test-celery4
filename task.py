from celery import Celery

SERIALIZER = "pickle"
SERIALIZER = "yaml"

app = Celery("task", broker="amqp://guest:guest@localhost//", backend="rpc://")

import datetime
@app.task
def echo():
    return datetime.datetime.now()

def test_echo():
    s = datetime.datetime.now()
    t = echo.delay().get()
    e = datetime.datetime.now()
    return s, t, e
