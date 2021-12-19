import itertools
import datetime
import time
from math import factorial


my_list = ['a', 'f', 'g', '1', '4', 'y', 'r']
y = len(my_list)


def combinations(text, *length):
    text = my_list
    length = len(my_list)
    res = []
    for x in itertools.combinations_with_replacement(text, length):
        print(list(x))
    return x


def work_time(func, *args):
    start_time = datetime.datetime.now()

    result_func = func(*args)
    result_func = factorial(len(my_list))
    time.sleep(1)

    end_time = datetime.datetime.now()
    print(end_time - start_time)

    return result_func


value = work_time(combinations, my_list)
print(value)

