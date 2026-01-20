import time, random
import matplotlib.pyplot as plt
import mplcyberpunk
from collections.abc import Callable

def generate_unsorted_list(size: int) -> list[int]:
    """Generates an unsorted list containing 
    integers ranging from 1 to 1,000,000
    """
    unsorted_list = []
    for i in range(size):
        unsorted_list.append(random.randint(1, 1000000))
    return unsorted_list

def timer(sorting_method: Callable[[list], list], lst: list) -> tuple[list, float]:
    """Times how long it takes for each sorting method to sort a list, if incorrectly
    ordered, and then return it. Returns the sorted list and elapsed time, in seconds, as a tuple.
    """
    copied_list = lst.copy()
    start = time.perf_counter_ns()
    sorted_list = sorting_method(copied_list) 
    end = time.perf_counter_ns()
    elapsed_time = (end - start) / 1_000_000_000  
    return sorted_list, elapsed_time

def graph_efficiency(element_count: list, **kwargs):
    """Plots a log-scaled comparison of execution times for two sorting algorithms 
    over varying input sizes.
    """
    plt.style.use('cyberpunk')
    plt.title('Sort Elapsed Time Comparison')
    plt.xlabel('Number of Elements')
    plt.ylabel('Time Taken (seconds)')
    plt.xticks(element_count, rotation=45)
    plt.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
    plt.grid(True)
    for arg in kwargs:
        plt.loglog(element_count, kwargs[arg], label=(arg.replace("_", " ")).title(), marker='o')
    plt.legend(loc="upper left")
    mplcyberpunk.add_glow_effects()
    plt.show()