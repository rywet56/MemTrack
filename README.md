# MemTrack
module for tracking memory usage in Python

# Installation
Download the file mem_usage.py and copy it into your project folder.

# Usage
- Import the function get_memory_usage() from mem_usage
- decorate function whose memory usage you want to monitor with get_memory_usage
- execute the decorated function
- a graph showing the peak memory usage over time will be saved into the current working directory

```python
from mem_usage import get_memory_usage
from time import sleep

@get_memory_usage
def dummy_func():
    u = []
    for k in range(0, 1000):
        u.append([1])
        sleep(0.00001)

dummy_func()
```
 <p align="center">
  <img src="https://user-images.githubusercontent.com/43107602/76205699-11b54780-61fb-11ea-9a80-aab52f152e58.png"  width="500">
 </p>
 
 # Remarks
 This implementation only provides a scaffold and is under developement.
 This version has not been tested thouroughly yet.
 
 # Credit
 Inspiration drawn from 
 - https://www.youtube.com/watch?v=IEEhzQoKtQU&t=1148s ([Corey M. Schafer](https://github.com/CoreyMSchafer?tab=repositories))
 - https://medium.com/survata-engineering-blog/monitoring-memory-usage-of-a-running-python-program-49f027e3d1ba ([Russell Keith-Magee](https://github.com/freakboy3742))
