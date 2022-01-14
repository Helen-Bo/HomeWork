class MyTemperature:

    def __init__(self, input_temp, measure):
        self.C = input_temp * 1
        if measure == 'K':
            self.C = self.C + 273.15
        elif measure == 'F':
            self.C = (self.C * 9/5) + 32
        else:
            self.C = f' {measure} is undefined value'
            print('Unknown measure')

    @staticmethod
    def to_kelvin(my_temp, measure):
        if measure == 'C':
            temp_in_kelvin = my_temp + 273.15
        elif measure == 'F':
            temp_in_kelvin = (my_temp - 32) * (5/9) + 273.15
        elif measure == 'K':
            temp_in_kelvin = f'{my_temp} {measure} in kelvin = {my_temp}'
        else:
            temp_in_kelvin = f'{measure} is undefined value'
        return temp_in_kelvin

    @staticmethod
    def to_fahrenheit(my_temp, measure):
        if measure == 'K':
            temp_in_fahrenheit = (my_temp - 273.15) * (9/5) + 32
        elif measure == 'C':
            temp_in_fahrenheit = (my_temp * 9/5) + 32
        elif measure == 'F':
            temp_in_fahrenheit = f'{my_temp} {measure} in fahrenheit = {my_temp}'
        else:
            temp_in_fahrenheit = f'{measure} is undefined value'
        return temp_in_fahrenheit

    def __gt__(self, other):
        if self.C > other.C:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.C < other.C:
            return True
        else:
            return False

    def __le__(self, other):
        if self.C <= other.C:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.C >= other.C:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.C == other.C:
            return True
        else:
            return False

    def __add__(self, other):
        return MyTemperature(self.C + other.C)

    def __sub__(self, other):
        return MyTemperature(self.C - other.C)


print(MyTemperature.to_kelvin(889, 'D'))
print(MyTemperature.to_fahrenheit(7, 'F'))
print(MyTemperature.to_kelvin(145, 'F'))
print(MyTemperature.to_fahrenheit(2, 'C'))
print('************')
temp1 = MyTemperature.to_fahrenheit(5, 'K')
print(temp1)
temp2 = MyTemperature.to_fahrenheit(1, 'K')
print(temp2)
print(temp2 == temp1)
print(temp2 <= temp1)
print(temp2 >= temp1)
print(temp2 < temp1)
print(temp2 > temp1)
print(temp2 + temp1)
print(temp2 - temp1)
print('***********')
temp3 = (MyTemperature.to_kelvin(8, 'F'))
temp4 = (MyTemperature.to_kelvin(2, 'F'))
print(MyTemperature.to_kelvin(8, 'F'))
print(MyTemperature.to_kelvin(2, 'F'))
print(temp3 == temp4)
print(temp3 <= temp4)
print(temp3 >= temp4)
print(temp3 < temp4)
print(temp3 > temp4)
print(temp3 + temp4)
print(temp3 - temp4)
