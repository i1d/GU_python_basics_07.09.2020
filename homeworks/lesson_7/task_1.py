"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д."""
import random

random.seed()


class Matrix:
    def __init__(self, matr):
        self.matr = matr

    def __str__(self):
        s = ""
        for i in range(len(self.matr)):
            s += f'{" ".join(list(map(str, self.matr[i])))}\n'
        return s[:-1]

    def __add__(self, other):
        matr_sum = []
        self.size = (len(self.matr), len(self.matr[0]))
        other.size = (len(other.matr), len(other.matr[0]))
        if self.size != other.size:
            print(f"Sizes of matrices are different!\n"
                  f"First  matrix size = {self.size[0]}x{self.size[1]},\n"
                  f"Second matrix size = {other.size[0]}x{other.size[1]}.\n")
        else:
          #  for i in range(self.size[0]):
          #      r = []
          #      for k in range(self.size[1]):
          #          r.append(self.matr[i][k] + other.matr[i][k])
       #     matr_sum = [[self.matr[i][k] + other.matr[i][k] for k in range(self.size[1])] for i in range(self.size[0])]
         #       matr_sum.append(r)
            return Matrix([[self.matr[i][k] + other.matr[i][k] for k in range(self.size[1])]
                           for i in range(self.size[0])]) #if len(matr_sum) > 0 else None


def gen_matrix(size):
    row = size[0]
    col = size[1]
    matr = [[random.randint(-9, 9) for _ in range(row)] for _ in range(col)]
    return matr


size = (random.randint(2, 5), random.randint(2, 5))
size2 = (random.randint(2, 5), random.randint(2, 5))

m1 = Matrix(gen_matrix(size))
m2 = Matrix(gen_matrix(size))
m3 = m1 + m2
print("-" * 20)
print(f"Matrix 1. id={id(m1)}\n{m1}")
print("-" * 20)
print(f"Matrix 2. id={id(m2)}\n{m2}")
print("-" * 20)
if len(str(m3)) > 0:
    print(f"Sum of matrices. id={id(m3)}\n{m3}")
print("=" * 40)

print("Try with different sizes:")
m4 = Matrix(gen_matrix(size))
m5 = Matrix(gen_matrix(size2))
m6 = m4 + m5
print("-" * 20)
print(f"Matrix 4. id={id(m4)}\n{m4}")
print("-" * 20)
print(f"Matrix 5. id={id(m5)}\n{m5}")
print("-" * 20)
if len(str(m6)) > 0:
    print(f"Sum of matrices. id={id(m6)}\n{m6}")

