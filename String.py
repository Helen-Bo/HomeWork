# Пусть пользователь вводит строку искомое слово и слово-замену
# заменить в строке искомое слово на слово-замену и вывески колличество замен
# пример:
# aaa bbb ccc ddd bbb rrr eee ddd
# bbb
# ccc
# вывод:
# aaa ccc ccc ddd ccc rrr eee ddd
# 2

text = input()

old = input('Введите слово,которое хотите заменить - ')
new = input('Введите слово для замены - ')


print(text)
text2 = text.replace(old, new)
print(text2)
print(text.count(old))