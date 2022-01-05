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
        print(f'Класс : Лучеперые рыбы \nВнутренний {self.skeleton} парных плавников не имеет центральной оси')


class DetachmentCarps(ClassClass):
    weber_apparatus = 'Веберов Апарат'
    swimming_bladder = 'плавательный пузырь'

    def carps(self):
        print(f'Отряд : Карпообразные  \nЕсть {self.weber_apparatus}; {self.swimming_bladder} соединён с кишечником')


class DetachmentHerring(ClassClass):
    fins = 'плавники'

    def herring(self):
        print(f'Оряд : Сельдеобразные\nГрудные {self.fins} расположены ближе к брюху,'
              f' брюшные {self.fins} находятся в средней части брюха')


class FamilyCarp(DetachmentCarps):
    mustache = 'усы'

    def family_carp(self):
        print(f'Семейство : Карповые \nУ некоторых видов по уголкам рта есть короткие {self.mustache}, выполняющие роль вкусовых рецепторов')


class FamilyHerring(DetachmentHerring):
    teeth = 'зубы'

    def family_herring(self):
        print(f'Семейство : Сельдевые \n{self.teeth} — необычно малого размера или вообще отсутствуют')


class GenusCarp(FamilyCarp):
    body = 'Тело'
    scale = 'Чешуя'

    def bream(self):
        print(f'Род : Лещи\nУ представителей рода лещей {self.body} сильно сжатое с боков, высокое или удлинённое. '
              f'{self.scale} умеренной величины. ')


class GenusHerring(FamilyHerring):
    body = 'Тело'
    scale = 'Чешуя'

    def fish_herring(self):
        print(f'Род : Сельди\n{self.body} сжатое с боков, с зазубренным краем брюха. '
              f'{self.scale} умеренная или крупная, редко мелкая.')


class KindCarp(GenusCarp):
    body_length = 'длина тела'

    def __init__(self, name):
        print(name)
        self.name = name

    def kind_of_bream(self):
        print(f'Вид : Лещ\nПресноводная рыба, единственный представитель '
              f'рода лещей из семейства карповых, отряда карпообразных'
              f'\nМаксимальная {self.body_length} — 82 см')


class KindHerring(GenusHerring):
    body_length = 'длина тела'

    def __init__(self, name):
        print(name)
        self.name = name

    def kind_of_herring(self):
        print(f'Вид : Атлантическая сельдь\nСредняя {self.body_length} атлантической сельди — 20—25 см'
              f'\nМаксимальная {self.body_length} 45 см')


lala = KindCarp('Лещ Валера')
lala.eukaryotes()
lala.animal()
lala.chordates()
lala.ray_finned_fish()
lala.carps()
lala.family_carp()
lala.bream()
lala.kind_of_bream()
print('------------')
mila = KindHerring('Сельдь Семен')
mila.eukaryotes()
mila.animal()
mila.chordates()
mila.ray_finned_fish()
mila.fish_herring()
mila.herring()
mila.fish_herring()
mila.kind_of_herring()
