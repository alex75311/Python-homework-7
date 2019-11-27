'''
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — ​ одежда​ , которая может иметь определенное название. К
типам одежды в этом проекте относятся ​ пальто ​ и ​ костюм​ . У этих типов одежды существуют
параметры: ​ размер ​ (для ​ пальто​ ) ​ и ​ рост ​ (для ​ костюма​ ). Это могут быть обычные числа: ​ V и
H​ , соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5)​ , для костюма ​ (2*H + 0.3)​ . Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
знания: реализовать абстрактные классы для основных классов проекта, проверить на
практике работу декоратора ​ @property​ .
'''

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.V = kwargs.get('V')
        self.H = kwargs.get('H')

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    @property
    def consumption(self):
        return f'Расход ткани составит {round(self.V / 6.5 + 0.5, 3)}'


class Suit(Clothes):
    @property
    def consumption(self):
        return f'Расход ткани составит {round(self.H * 2 + 0.3, 3)}'


coat_1 = Coat(name='Пальто', V=43)
suit_1 = Suit(name='Костюм', H=32)

print(coat_1.name, coat_1.consumption)
print(suit_1.name, suit_1.consumption)
