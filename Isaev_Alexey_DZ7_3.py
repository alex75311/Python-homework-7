'''
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
количеству ячеек клетки (целое число). В классе должны быть реализованы методы
© geekbrains.ru 20перегрузки арифметических операторов: сложение (​ __add__()​ ), вычитание (​ __sub__()​ ),
умножение (​ __mul__()​ ), деление (​ __truediv__()​ ). Данные методы должны применяться ​ только
к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное)
деление клеток, соответственно. В методе деления должно осуществляться округление
значения до целого числа.
Сложение​ . Объединение двух клеток. При этом число ячеек общей клетки должно равняться
сумме ячеек исходных двух клеток.
Вычитание​ . Участвуют две клетки. Операцию необходимо выполнять только если разность
количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение​ . Создается общая клетка из двух. Число ячеек общей клетки определяется как
произведение количества ячеек этих двух клеток.
Деление​ . Создается общая клетка из двух. Число ячеек общей клетки определяется как
целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод ​ make_order()​ , принимающий экземпляр класса и
количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида ​ *****\n*****\n*****​ ..., где количество ячеек между ​ \n
равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
make_order() ​ вернет строку: ​ *****\n*****\n**​ .
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
make_order() ​ вернет строку: ​ *****\n*****\n*****​ .
'''


class Cell:
    def __init__(self, counts=0):
        self.counts = int(counts)

    def __add__(self, other):
        return sum([self.counts, other.counts])

    def __sub__(self, other):
        res = self.counts - other.counts
        return res if res >= 0 else 'Невозможно провести вычитание'

    def __mul__(self, other):
        return Cell(self.counts * other.counts)

    def __truediv__(self, other):
        return Cell(self.counts // other.counts)

    def __str__(self):
        return str(self.counts)

    def make_order(self, n):
        res = ''
        for i in range(self.counts // n):
            res += '*' * n + '\\n'
        res += '*' * (self.counts % n)
        return res


a = Cell(5)
b = Cell(32)
print(a + b, type(a + b))
print(b - a, type(b - a))
print(a - b, type(a - b))
print(a * b, type(a * b))
print(b / a, type(b / a))
print(b.make_order(5), type(b.make_order(5)))
