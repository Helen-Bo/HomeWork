import random
import datetime
import time
my_list = random.sample(range(100), 10)
print(f'Несортированный список {my_list}')


def work_time(func):
    def func_arg(*args, **kwargs):
        start_time = datetime.datetime.now()

        result_func = func(*args, **kwargs)
        time.sleep(1)

        end_time = datetime.datetime.now()
        wrk_time = end_time - start_time
        return wrk_time
    return func_arg


@work_time
def sort_function(sort_list):
    for i in range(len(sort_list)):
        min_element = i
        for element in range(i + 1, len(sort_list)):
            if sort_list[element] < sort_list[min_element]:
                min_element = element
        sort_list[i], sort_list[min_element] = sort_list[min_element], sort_list[i]
    print(sort_list)
    return sort_list


@work_time
def bubble_sort(s_list):
    for i in range(len(s_list)):
        for j in range(i+1, len(s_list)):
            if s_list[i] > s_list[j]:
                s_list[i], s_list[j] = s_list[j], s_list[i]
    print(s_list)
    return s_list


sorted_list = sort_function(my_list)
print(sorted_list)

sorter_list1 = bubble_sort(my_list)
print(sorter_list1)
