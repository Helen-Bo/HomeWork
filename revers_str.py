my_string = input()


def revers_func(string1):
    splited_word = string1.split(' ')
    splited_word.reverse()
    new_str = ' '.join(splited_word)
    # string1 = my_string[::-1]
    # if string1 == my_string:
    #     print('It`s palindrome', string1)
    # else:
    #     print('It`s not palindrome', string1)
    return new_str

print(revers_func(my_string))

