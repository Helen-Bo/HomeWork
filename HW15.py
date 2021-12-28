from math import sqrt
from math import pow

fist = input('Введите координаты точки А  -> ')
second = input('Введите координаты точки В  -> ')

first_point = fist.split(',')
second_point = second.split(',')


def distance(*args) -> object:
    x1 = int(first_point[0])
    y1 = int(first_point[1])

    x2 = int(second_point[0])
    y2 = int(second_point[1])

    new_x = (x2-x1)
    new_y = (y2-y1)
    dist = sqrt(pow(new_x, 2) + pow(new_y, 2))
    dist_round = round(dist, 2)
    return dist_round


distance = distance(first_point, second_point)
print(distance)
