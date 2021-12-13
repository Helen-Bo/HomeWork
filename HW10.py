def my_function(meter, convert_to):
    if convert_to == 'cm':
        result = meter * 100
        return result
    elif convert_to == 'ft':
        result = round(meter * 3.28, 2)
        return result
    elif convert_to == 'inch':
        result = round(meter * 39.27, 2)
        return result
    elif convert_to == 'fathom':
        result = round(meter / 1.829, 2)
        return result


while True:
    value1 = input('Введите значение -> ')
    value2 = input('Введите меру длинны -> ')
    if value1.isdigit() and value2 in ['cm', 'ft', 'inch', 'fathom']:
        value1 = int(value1)
        print(my_function(value1, value2))
        print(f'{value1} meter in {value2} = {my_function(value1, value2)} {value2}')
    elif value1 or value2 == 'exit':
        break
    else:
        print('Error')
