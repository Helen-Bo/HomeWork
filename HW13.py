import itertools
import re
import datetime
import time

# my_list = ['a', 'f', 'g', '1', '4', 'y', 'r']
my_list = ['4', 'r']
y = len(my_list)

list_a = input('Введите значения для поиска повторяющегося элемента -> ')


def decorator_incoming_data(func_to_decorate):
    def wrap_args(*args, **kwargs):
        print('Входящие параметры', *args, **kwargs)
        func_to_decorate(*args, **kwargs)
        # return func_to_decorate(*args, **kwargs)
    return wrap_args


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
@decorator_incoming_data
def repeating_elements(str):
    str = list_a
    element = re.findall(r'[^\b,;:\-\'\"\+@#|\.()%\$!\s]', str)

    new_list = []
    for x in element:
        if element.count(x) > 1:
            new_list.append(x)
    print(f'{str} -> {new_list[0]}')



@work_time
@decorator_incoming_data
def combinations(text, *length):
    text = my_list
    length = len(my_list)
    for x in itertools.combinations_with_replacement(text, length):
        print(list(x))
    return x


print(repeating_elements(list_a))
print(combinations(my_list, y))

