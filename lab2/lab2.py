import random

import collections


class Matrix:

    def __init__(self, n):
        self.n = n
        self.matrix = [[random.randrange(0, 5) for a in range(n)] for b in range(n)]

    def print(self):
        matrix = self.matrix
        for im in range(len(matrix)):
            print(matrix[im])

    def sort_a(self):
        matrix = self.matrix
        for x in range(n):
            for i in range(n):
                buf = 0;
                for j in range(n - 1):
                    if (matrix[i][j] > matrix[i][j + 1]):
                        buf = matrix[i][j + 1]
                        matrix[i][j + 1] = matrix[i][j]
                        matrix[i][j] = buf

    def sort_b(self):
        matrix = self.matrix
        for x in range(n):
            for i in range(n - 1):
                buf = 0;
                for j in range(n):
                    if (matrix[i][j] > matrix[i + 1][j]):
                        buf = matrix[i + 1][j]
                        matrix[i + 1][j] = matrix[i][j]
                        matrix[i][j] = buf




def read_number():
    number = input("Размерность матрицы(n): ")
    while not (number.isdigit() and int(number) > 1):
        number = input("Введите целое положительное число больше 1: ")
    return int(number)

n = read_number() #размерность матрицы
m = Matrix(n)
m.print()
m.sort_a()
print('  ')
m.print()
m.sort_b()
print('  ')
m.print()
