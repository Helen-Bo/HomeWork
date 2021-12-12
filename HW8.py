import re

while True:
    phone_number = input()
    phone_number1 = phone_number.replace('-', '')
    phone_number2 = phone_number1.replace('+', '')
    phone_number3 = phone_number2.replace('(', '')
    phone_number4 = phone_number3.replace(')', '')
    phone_number5 = phone_number4.replace(' ', '')
    #print(phone_number5)
    if True:
        print(bool(re.match(r'\d{10,14}', phone_number5)))


