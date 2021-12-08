actions = []
element = '2'
while element != '=':
    element = input()
    if element == '=':
        break
    actions.append(element)


operator = '+'
result = 0
for i in actions:
    if i.isdigit():
        i = int(i)
        if operator == '+':
            result = result + i
        elif operator == '-':
            result = result - i
        elif operator == '*':
            result = result * i
        else:
            result = result / i
    else:
        operator = i
print(result)
