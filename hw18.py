class MyTemperature:

    dict = {'K': 273.15, 'F': 5/9, 'C': 1}

    def __init__(self, input_temp, measure):
        self.Kc = input_temp + MyTemperature.dict[measure]
        self.Kf = MyTemperature.kelvin_to_fahrenheit(input_temp, measure)
        self.Fc = MyTemperature.celsius_to_fahrenheit(input_temp, measure)
        self.Fk = MyTemperature.kelvin_to_fahrenheit(input_temp, measure)
        self.Ck = MyTemperature.celsius_to_kelvin(input_temp, measure)
        self.Cf = MyTemperature.celsius_to_fahrenheit(input_temp, measure)

    @staticmethod
    def kelvin_to_celsius(my_temp, measure):
        k_to_c = my_temp - MyTemperature.dict['K'] * MyTemperature.dict[measure]
        return k_to_c

    @staticmethod
    def kelvin_to_fahrenheit(my_temp, measure):
        k_to_f = (my_temp - MyTemperature.dict['K']) * (MyTemperature.dict[measure]**(-1)) + 32
        return k_to_f

    @staticmethod
    def celsius_to_kelvin(my_temp, measure):
        c_to_k = my_temp + MyTemperature.dict[measure]
        return c_to_k

    @staticmethod
    def celsius_to_fahrenheit(my_temp, measure):
        c_to_f = (my_temp * (MyTemperature.dict[measure]**(-1))) + 32
        return c_to_f

    @staticmethod
    def fahrenheit_to_kelvin(my_temp, measure):
        f_to_k = (my_temp - 32) * MyTemperature.dict['F'] + MyTemperature.dict[measure]
        return f_to_k

    @staticmethod
    def fahrenheit_to_celsius(my_temp, measure):
        f_to_c = ((my_temp - 32) * MyTemperature.dict['F']) * MyTemperature.dict[measure]
        return f_to_c

    def __gt__(self, other):
        if self.celsius_to_fahrenheit > other.celsius_to_fahrenheit or \
                self.celsius_to_kelvin > other.celsius_to_kelvin or \
                self.kelvin_to_fahrenheit > other.kelvin_to_fahrenheit or \
                self.kelvin_to_celsius > other.kelvin_to_celsius or \
                self.fahrenheit_to_celsius > other.fahrenheit_to_celsius or \
                self.fahrenheit_to_kelvin > other.fahrenheit_to_kelvin:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.celsius_to_fahrenheit < other.celsius_to_fahrenheit or \
                self.celsius_to_kelvin < other.celsius_to_kelvin or \
                self.kelvin_to_fahrenheit < other.kelvin_to_fahrenheit or \
                self.kelvin_to_celsius < other.kelvin_to_celsius or \
                self.fahrenheit_to_celsius < other.fahrenheit_to_celsius or \
                self.fahrenheit_to_kelvin < other.fahrenheit_to_kelvin:
            return True
        else:
            return False

    def __le__(self, other):
        if self.celsius_to_fahrenheit <= other.celsius_to_fahrenheit or \
                self.celsius_to_kelvin <= other.celsius_to_kelvin or \
                self.kelvin_to_fahrenheit <= other.kelvin_to_fahrenheit or \
                self.kelvin_to_celsius <= other.kelvin_to_celsius or \
                self.fahrenheit_to_celsius <= other.fahrenheit_to_celsius or \
                self.fahrenheit_to_kelvin <= other.fahrenheit_to_kelvin:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.celsius_to_fahrenheit >= other.celsius_to_fahrenheit or \
                self.celsius_to_kelvin >= other.celsius_to_kelvin or \
                self.kelvin_to_fahrenheit >= other.kelvin_to_fahrenheit or \
                self.kelvin_to_celsius >= other.kelvin_to_celsius or \
                self.fahrenheit_to_celsius >= other.fahrenheit_to_celsius or \
                self.fahrenheit_to_kelvin >= other.fahrenheit_to_kelvin:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.celsius_to_fahrenheit == other.celsius_to_fahrenheit or \
                self.celsius_to_kelvin == other.celsius_to_kelvin or \
                self.kelvin_to_fahrenheit == other.kelvin_to_fahrenheit or \
                self.kelvin_to_celsius == other.kelvin_to_celsius or \
                self.fahrenheit_to_celsius == other.fahrenheit_to_celsius or \
                self.fahrenheit_to_kelvin == other.fahrenheit_to_kelvin:
            return True
        else:
            return False

    def __add__(self, other):
        return MyTemperature(self.celsius_to_fahrenheit + other.celsius_to_fahrenheit or
                             self.celsius_to_kelvin + other.celsius_to_kelvin or
                             self.kelvin_to_fahrenheit + other.kelvin_to_fahrenheit or
                             self.kelvin_to_celsius + other.kelvin_to_celsius or
                             self.fahrenheit_to_celsius + other.fahrenheit_to_celsius or
                             self.fahrenheit_to_kelvin + other.fahrenheit_to_kelvin)

    def __sub__(self, other):
        return MyTemperature(self.celsius_to_fahrenheit - other.celsius_to_fahrenheit or
                             self.celsius_to_kelvin - other.celsius_to_kelvin or
                             self.kelvin_to_fahrenheit - other.kelvin_to_fahrenheit or
                             self.kelvin_to_celsius - other.kelvin_to_celsius or
                             self.fahrenheit_to_celsius - other.fahrenheit_to_celsius or
                             self.fahrenheit_to_kelvin - other.fahrenheit_to_kelvin)


print(MyTemperature.celsius_to_fahrenheit(10, 'F'))
print(MyTemperature.celsius_to_kelvin(10, 'K'))

print(MyTemperature.kelvin_to_fahrenheit(10, 'F'))
print(MyTemperature.kelvin_to_celsius(10, 'C'))

print(MyTemperature.fahrenheit_to_kelvin(10, 'K'))
print(MyTemperature.fahrenheit_to_celsius(10, 'C'))

temp1 = (MyTemperature.fahrenheit_to_kelvin(89, 'K'))
temp2 = (MyTemperature.fahrenheit_to_kelvin(90, 'K'))
print(temp2 == temp1)
print(temp2 <= temp1)
print(temp2 >= temp1)
print(temp2 < temp1)
print(temp2 > temp1)
print(temp2 + temp1)
print(temp2 - temp1)
