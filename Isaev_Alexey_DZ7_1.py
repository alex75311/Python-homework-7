'''
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()​ ), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — ​ система некоторых математических величин, расположенных в виде
прямоугольной схемы.

Следующий шаг — реализовать перегрузку метода ​ __str__() для вывода матрицы в
привычном виде.

Далее реализовать перегрузку метода ​ __add__() для реализации операции сложения двух
объектов класса ​ Matrix ​ (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д
'''

my_list1 = [[1, 2], [3, 4], [5, 6]]
my_list2 = [[10, 122], [27, 13], [31, 88]]


class Matrix:
    def __init__(self, arr):
        self.arr = arr

    def __str__(self):
        res = ''
        for els in self.arr:
            el_str = ''
            for el in els:
                el_str += str(el) + ' '
            res += el_str + '\n'
        return res

    def __add__(self, other):
        res = []
        x = len(self.arr)
        y = len(self.arr[0])

        for els in range(x):
            el_str = []
            for el in range(y):
                summ = self.arr[els][el] + other.arr[els][el]
                el_str.append(summ)
            res.append(el_str)
        return Matrix(res)

    def __sub__(self, other):
        res = []
        x = len(self.arr)
        y = len(self.arr[0])

        for els in range(x):
            el_str = []
            for el in range(y):
                razn = self.arr[els][el] - other.arr[els][el]
                el_str.append(razn)
            res.append(el_str)
        return Matrix(res)


m_1 = Matrix(my_list1)
m_2 = Matrix(my_list2)
print(m_1)
print(m_2)
print(m_1 + m_2)
print(m_2 - m_1)
