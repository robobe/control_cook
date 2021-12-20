import asyncio
import time
import threading

def foo():
    time.sleep(1)
    print("foo")


def bar():
    time.sleep(1)
    print("bar")


def put():
    loop.call_soon(foo)
    loop.call_soon(bar)
    print("put")

loop = asyncio.get_event_loop()
t = threading.Thread(target=put)
t.start()


loop.run_forever()