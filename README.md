# MemTrack
module for tracking memory usage in Python

# Installation
Download the file mem_usage.py and copy it into your project folder.

# Usage
- Import the function get_memory_usage() from mem_usage
- decorate function whose memory usage you want to monitor with get_memory_usage
- execute the decorated function
- a graph showing the peak memory usage over time will be saved into the current working directory

from mem_usage import get_memory_usage
from time import sleep

@get_memory_usage
def dummy_func():
    u = []
    for k in range(0, 1000):
        u.append([1])
        sleep(0.00001)

dummy_func()