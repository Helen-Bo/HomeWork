from PIL import Image


class Scale:
    @staticmethod
    def scale_resize(my_height, my_width):
        squid_image = Image.open('squid.jpg')
        squid_image.show()
        squid_image = squid_image.resize((my_width, my_height), Image.BICUBIC)
        squid_image.show()


try:
    My_height = int(input('Введите новое значение высоты '))
except ValueError as e:
    print(e)
    exit(1)

try:
    My_width = int(input('Введите новое значение ширины '))
except ValueError as e:
    print(e)
    exit(1)


try:
    Scale.scale_resize(My_height, My_width)
except ValueError as e:
    print(e)
    exit(1)






