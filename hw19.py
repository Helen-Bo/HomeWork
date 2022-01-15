def fibonacci_numbers(n):
    if n in (1, 2):
        return 1
    else:
        f1 = 1
        f2 = 1
        print(f1, f2, end=' ')
        for i in range(2, n):
            f1, f2 = f2, f1 + f2
            print(f2, end=' ')
        return ''


print(fibonacci_numbers(1))
print(fibonacci_numbers(2))
print(fibonacci_numbers(3))
print(fibonacci_numbers(10))
print(fibonacci_numbers(55))

