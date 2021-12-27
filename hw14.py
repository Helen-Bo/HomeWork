first_number = int(input('Input first value '))
second_number = int(input('Input second value '))


def greatest_common_factor(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


GCF = greatest_common_factor(first_number, second_number)
print(f'Greatest common factor {first_number} and {second_number} is equal to {GCF}')