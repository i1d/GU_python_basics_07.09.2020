"""7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class Cmplx:
    def __init__(self, real_part, img_part):
        #self.cmplx_num = self.convert(input)# (real_part, img_part)
        self.cmplx_num = (real_part, img_part)

 #   def convert(self, input):
 #       if type(input) == str:
 #       #elif type(input) == tuple
 #           inp = input.split("+")
 #           return (int(inp[0]), int(inp[1][0]))

    @property
    def real_part(self):
        return self.cmplx_num[0]

    @property
    def img_part(self):
        return self.cmplx_num[1]

    def __add__(self, other):  # (a+bi) + (c+di) = (a+c) + (b+d)i
        return Cmplx(self.real_part + other.real_part, self.img_part + other.img_part)

    def __mul__(self, other):  # (a+bi) * (c+di) = (a*c - b*d) + (b*c + a*d)i
        return Cmplx((self.real_part * other.real_part - self.img_part * other.img_part),
                     (self.img_part * other.real_part + self.real_part * other.img_part))

    def __str__(self):
        return f'({self.cmplx_num[0]}+{self.cmplx_num[1]}j)'


a = Cmplx(1, 2)
_a = complex(1, 2)

b = Cmplx(3, 4)
_b = complex(3, 4)

a_b = a + b
_a_b = _a + _b

try:
    assert complex(str(a_b)) == _a_b, "Addition assert error"
except AssertionError as err:
    print(err)
print(a_b)

ab = a * b
_ab = _a * _b

try:
    assert complex(str(ab)) == _ab, "Multiplication assert error"
except AssertionError as err:
    print(err)
print(ab)
