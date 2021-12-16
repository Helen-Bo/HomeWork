input_data = [(1, 'cm'), (2, 'ft'), (4, 'inch'), (0.5, 'cm'), (9, 'fathom')]


def converter_func(data_in):
    meter = data_in[0]
    convert_to = data_in[1]
    result = 0
    if convert_to == 'cm':
        result = meter * 100
    elif convert_to == 'inch':
        result = meter * 39.37
    elif convert_to == 'ft':
        result = meter * 3.28
    elif convert_to == 'fathom':
        result = meter * 0.46869
    else:
        result = 'unknown'
    return result


result = map(converter_func, filter(lambda itm_in: True if itm_in[0] >= 1 else False, input_data))
for element in result:
    print(element)
