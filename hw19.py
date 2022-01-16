def fibonacci_numbers(n):
    if n <= 1:
        return 1
    else:
        return (fibonacci_numbers(n-1) + fibonacci_numbers(n-2))


num = int(input('Введите число'))

if num <= 0:
    print(f'{num} is not positive')
else:
    for itm in range(num):
        print(fibonacci_numbers(itm))


#Это изначальный вариан решения домашки, но после занятия поняла, что опять получилось сложно
def fibonacci_numbers1(m):
    if m <= 0:
        print('Error')
    else:
        if m == 1:
            return 1
        else:
            f1 = 1
            f2 = 1
            print(f1, f2, end=' ')
            for i in range(2, m):
                f1, f2 = f2, f1 + f2
                print(f2, end=' ')
    return ''


print(fibonacci_numbers1(-10))
print(fibonacci_numbers1(1))
print(fibonacci_numbers1(2))
print(fibonacci_numbers1(5))
print(fibonacci_numbers1(10))
print(fibonacci_numbers1(55))

