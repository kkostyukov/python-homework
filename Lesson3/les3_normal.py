# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
import math

def fibonacci(n, m):
    if n > m:
        return "Не корректные входные данные"
    fibonacci_list = [1, 1]
    i = 2
    while i < m:
        fibonacci_list.append(fibonacci_list[i - 1] + fibonacci_list[i - 2])
        i += 1
    return fibonacci_list[n - 1:m]


print(fibonacci(2, 9))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    i = 0
    while i < len(origin_list):
        ii = i + 1
        while ii < len(origin_list):
            if origin_list[i] > origin_list[ii]:
                origin_list[i], origin_list[ii] = origin_list[ii], origin_list[i]
            ii += 1
        i += 1
    print(origin_list)


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(filter_func, origin_list):
    result = []
    for i in origin_list:
        if filter_func(i):
            result.append(i)
    return result
print(my_filter(lambda x: x >= 5, [1, 2, 3, 4, 5, 6, 7]))
print(my_filter(len, ['q', '', 'c', '']))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def lenght(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

def paralel(a, b, c, d):
    ab = lenght(a[0], a[1], b[0], b[1])
    bc = lenght(b[0], b[1], c[0], c[1])
    cd = lenght(c[0], c[1], d[0], d[1])
    da = lenght(d[0], d[1], a[0], a[1])
    print(ab, bc, cd, da)
    if ab == cd and bc == da:
        return "Это вершины парралелограмма"
    else:
        return "Это не вершины парралелограмма"

a = [0, 0]
b = [1, 5]
c = [3, 5]
d = [2, 0]

print(paralel(a, b, c, d))