import time
import functools


def measure_elapsed_time(func):
    """
    The function measures run time of another function
    """
    @functools.wraps(func)
    def timed(*args, **kwargs):
        t_start = time.time()
        result = func(*args, **kwargs)
        t_end = time.time()
        print("f: {} args: {}, {} trvala {:.4f} sekund".format
              (func.__name__, args, kwargs, t_end-t_start))
        return result

    return timed


@measure_elapsed_time
def double_numbers_for_cycle(num):
    """
    Generates a sequence of numbers from 0 to entered arg num then numbers
    from this list are multiplied by two. For cycle is used.
    """
    numbers_list = range(num)
    doubled_numbers = []
    for i in numbers_list:
        doubled_numbers.append(i*2)
    return doubled_numbers


@measure_elapsed_time
def double_numbers_comprehension(num):
    """
    Generates a sequence of numbers from 0 to enetered arg num then numbers
    from this list are multiplied by two. List comprehension is used.
    """
    numbers_list = range(num)
    doubled_numbers = [i*2 for i in numbers_list]
    return doubled_numbers


if __name__ == "__main__":
    double_numbers_for_cycle(100000)
    double_numbers_comprehension(100000)
