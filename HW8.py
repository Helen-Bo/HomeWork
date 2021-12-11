# Написать приложение которое будет находить первый повторяющийся элемент среди введённых пользователем
# например:
# 1 2 3 2 4 5 3 -> 2
# 2 3 5 3 5 6 -> 3
import re
import collections

list_a = input()



element = re.findall(r'[^\b,;:\-\'\"\+@#|\.()%\$!\s]', list_a)
# print(element)
new_list = []
for x in element:
    if element.count(x) > 1:
        new_list.append(x)


print(f'{list_a} -> {new_list[0]}')

#y = collections.Counter(element).most_common(1)

#print(y)
#print(f'{list_a} -> {y}')