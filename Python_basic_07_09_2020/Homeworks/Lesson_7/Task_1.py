"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц)
Результатом сложения должна быть новая матрица.
"""


class Matrix:
    def __init__(self, *args):
        self.matrix_data = []

        for item in args:
            self.matrix_data.append(item)
        self.matrix_data = tuple(self.matrix_data)

    def __str__(self):
        return "\n".join(["|".join(map(str, item)) for item in self.matrix_data])

    def __add__(self, other):
        result = []
        for i in range(len(self.matrix_data)):
            row = []
            for j in range(len(self.matrix_data[0])):
                try:
                    row.append(self.matrix_data[i][j] + other.matrix_data[i][j])
                except IndexError:
                    print("Либо Вы ввели не матрицы, либо размерности матриц не совпадают!")
                    quit()
            result.append(row)
        print(result)
        return Matrix(result_item for result_item in result)


if __name__ == '__main__':
    matrix1 = Matrix([1, 2, 3], [2, 3, 4])
    matrix2 = Matrix([7, 9, 19], [4, 5, 22])
    print('#'*20)
    print(matrix1)
    print('#' * 20)
    print(matrix2)
    print('#' * 20)
    matrix3 = matrix1 + matrix2
    print(matrix3)
    print('#' * 20)
