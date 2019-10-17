# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Shape:
    def _length(self, p1: Point, p2: Point):
        """
        Длина стороны по 2 точкам
        """
        return math.sqrt(math.pow(p1.x - p2.x, 2) + math.pow(p1.y - p2.y, 2))

    def area(self):
        raise NotImplementedError

    def perimeter(self):
        raise NotImplementedError


class Triangle(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self._a = self._length(p1, p2)  #
        self._b = self._length(p2, p3)  # длины сторон
        self._c = self._length(p3, p1)  #
        self._p = 0.5 * (self._a + self._b + self._c)  # переменные, которая используется в
        self._hp = None  # формуле расчета высоты

    def _get_hp(self):
        if not self._hp:
            self._hp = 2 * math.sqrt(self._p * (self._p - self._a) * (self._p - self._b) * (self._p - self._c))

        return self._hp

    def area(self):
        return abs(0.5 * ((self.p1.x - self.p3.x) * (self.p2.y - self.p3.y) - (self.p2.x - self.p3.x) * (
                self.p1.y - self.p3.y)))

    def perimeter(self):
        return self._a + self._b + self._c

    def heigth_a(self):
        return self._get_hp() / self._a

    def heigth_b(self):
        return self._get_hp() / self._b

    def heigth_c(self):
        return self._get_hp() / self._c

a = Point(0, 0)
b = Point(2, 4)
c = Point(5, 1)

t = Triangle(a, b, c)

print("area:", t.area())
print("perimeter:", t.perimeter())
print("heigth_a:", t.heigth_a())
print("heigth_b:", t.heigth_b())
print("heigth_c:", t.heigth_c())

exit(0)

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class IsoscelesTrapezoid(Shape):
    def __init__(self, p1: Point, p2: Point, p3: Point, p4: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self._a = self._length(p1, p2)  #
        self._b = self._length(p2, p3)  # длины сторон
        self._c = self._length(p3, p4)  #
        self._d = self._length(p4, p1)  #
        self._h = None # высота трапеции

    def is_osceles(self) -> bool:
        return bool(self._a == self._c and (self.p4.x - self.p1.x) / self._d == (self.p3.x - self.p2.x) / self._b or (
                self._b == self._d and (self.p2.x - self.p1) / self._a == (self.p3.x - self.p4.x) / self._c) or (
                            self._a == self._c and self._b == self._d))

    def get_leght_a(self):
        return self._a

    def get_leght_b(self):
        return self._b

    def get_leght_c(self):
        return self._c

    def get_leght_d(self):
        return self._d

    def perimeter(self):
        return self._a + self._b + self._c + self._d

    def _get_h(self): # Высота трапеции
        if not self._h:
            if self._a == self._c:
                self._h = self.p2.y - self.p1.y
            else:
                self._h = self.p3.y - self.p2.y

        return self._h


    def area(self):
        if self._a == self._c:
            s = self._get_h() * (self._b + self._d)/2
        else:
            s = self._get_h() * (self._a + self._c)/2