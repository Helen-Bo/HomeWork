import itertools
import datetime
import time
from math import factorial


my_list = ['a', 'f', 'g', '1', '4', 'y', 'r']
y = len(my_list)


def combinations(text, *length):
    text = my_list
    length = len(my_list)
    for x in itertools.combinations_with_replacement(text, length):
        print(list(x))
    return list(x)


def work_time(func, *args, **kwargs):
    start_time = datetime.datetime.now()

    result_func = func(*args, **kwargs)
    result_func = my_list
    time.sleep(1)

    end_time = datetime.datetime.now()
    wrk_time = end_time - start_time
    print(wrk_time)
    return result_func


value = work_time(combinations, my_list)
print(value)

