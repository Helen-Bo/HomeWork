import re
while True:
    phone_number = input()
    if phone_number == 'exit':
        break
    print(bool(re.findall(r'^\+[\(\-]?(\d[\(\)\-]?){11}\d$' or
                         r'^\(?(\d[\-\(\)]?){9}\d$' and
                        r'[\+]?\d*(\(\d{3}\))?\d*\-?\d*\-?\d*\d$', phone_number)))







#^\+[\(\-]?(\d[\(\)\-]?){11}\d$
#если номер содержит + в начале,
# откр.скобочка
# и - которые встречается один раз (?),
# встречаются 11 раз цифры
# и  -
# и скобочки по одному разу
# и в конце 12-я цифра

