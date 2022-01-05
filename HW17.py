class Domain:
    cell = 'Клетки'

    def eukaryotes(self):
        print(f'Домен: Эукариоты \n{self.cell} имеют ядро')


class Kingdom(Domain):
    nutrition = 'Питание'

    def animal(self):
        print(f'Царство: Животные \n{self.nutrition} готовыми органическими соединениями')


class Type(Kingdom):
    spine = 'Позвоничник'
    bilateral_symmetry = 'Двухсторонняя симметрия'

    def chordates(self):
        print(f'Тип : Хордовые \nХарактерно наличие таких признаков \n{self.spine} \n{self.bilateral_symmetry}')


class ClassClass(Type):
    skeleton = 'скелет'

    def ray_finned_fish(self):
        print(f'Класс: Лучеперые рыбы \nВнутренний {self.skeleton} парных плавников не имеет центральной оси')


class DetachmentCarps(ClassClass):
    weber_apparatus = 'Веберов Апарат'
    swimming_bladder = 'плавательный пузырь'

    def carps(self):
        print(f'Отряд:Карпообразные  \nЕсть {self.weber_apparatus}; {self.swimming_bladder} соединён с кишечником')


class DetachmentHerring(ClassClass):
    fins = 'плавники'

    def herring(self):
        print(f'Оряд:Сельдеобразные\nГрудные {self.fins} расположены ближе к брюху, брюшные {self.fins} находятся в средней части брюха')


class FamilyCarp(DetachmentCarps):
    pass


class FamilyHerring(DetachmentHerring):
    pass


class GenusCarp(FamilyCarp):
    pass


class GenusHerring(FamilyHerring):
    pass


class KindCarp(GenusCarp):

    def __init__(self, name):
        print(name)
        self.name = name


class KindHerring(GenusHerring):

    def __init__(self, name):
        print(name)
        self.name = name


lala = KindCarp('Лещ Валера')
lala.eukaryotes()
lala.animal()
lala.chordates()
lala.ray_finned_fish()
lala.carps()

