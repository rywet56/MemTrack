from mem_usage import get_memory_usage
from time import sleep


@get_memory_usage
def dummy_func():
    u = []
    for k in range(0, 1000):
        u.append([1])
        sleep(0.00001)


dummy_func()
