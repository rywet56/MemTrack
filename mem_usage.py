import resource
import sys
from time import sleep
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt


class MemoryMonitor:
    def __init__(self):
        self.keep_measuring = True

    def measure_usage(self):
        """
        Recording peak memory usage of current process at inverals of 0.0001 seconds until instance variable
        _keeep_measuring is False.
        Saving those results in list memory_use.
        :return: list of peak memory usages with interval of 0.0001 seconds in MB
        """
        basal_memory_use = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000000
        memory_use = []
        while self.keep_measuring:
            # print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            # yield resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            # print(str(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss) + " -- " + str(sys.getsizeof(memory_use)))

            # get current usage in megabyte
            memory_use.append(((resource.getrusage(resource.RUSAGE_SELF).ru_maxrss - sys.getsizeof(memory_use))/1000000)
                              - basal_memory_use)
            sleep(0.00001)

        return memory_use


def create_graph(interval, mem_usage_list):
    """
    creates a graph using matplotlib by plotting memory usage in MB against time axis in seconds
    :param interval: expected interval for x-axis
    :param mem_usage_list: list containing memory usage in MB
    """
    # create timepoints
    time_points = [i*interval for i in range(len(mem_usage_list))]

    # create plot
    fig, axes = plt.subplots(1, 1, figsize=(8, 3))

    axes.set_title("memory usage over time", size=22, pad=20)
    axes.plot(time_points, mem_usage_list, color="orange")
    axes.set_ylabel("memory usage (MB)", size=14)
    axes.set_xlabel("time (seconds)", size=14)

    # save plot
    plt.savefig('/Users/manuel/Desktop/plot.png', dpi=500, bbox_inches='tight')


def get_memory_usage(func):
    def measured_func(*args, **kwargs):
        with ThreadPoolExecutor() as executor:
            monitor = MemoryMonitor()
            mem_thread = executor.submit(monitor.measure_usage)

            fn_thread = executor.submit(func, *args, **kwargs)
            fn_result = fn_thread.result()

            monitor.keep_measuring = False
            mem_result = mem_thread.result()

            create_graph(interval=0.00001, mem_usage_list=mem_result)

        return fn_result
    return measured_func


