my_lists = [[31, 22], [37, 43], [51, 86]]


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


m_1 = Matrix(my_lists)
print(m_1)
