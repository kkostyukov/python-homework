# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]
import math
import random

my_list = [2, -5, 8, 9, -25, 25, 4]
new_list = []
for i in my_list:
    if i >=0 and math.sqrt(i) % 1 == 0:
        new_list.append(int(math.sqrt(i)))
print(new_list)

# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)
test_date = "12.09.1999"

day = {'01':'первое','02':'второе','03':'третье','04':'четвертое','05':'пятое','06':'шестое','07':'седьмое',
       '08':'восьмое','09':'девятое','10':'десятое','11':'одинадцатое','12':'двенадцатое', '13':'тринадцатое',
       '14':'четырнадцатое','15':'пятьнадцатое','16':'шестьнадцатое','17':'семнадцатое','18':'восемнадцатое',
       '19':'девятнадцатое','20':'двадцатое','21':'двадцать первое','22':'двадцать второе','23':'двадцать третье',
       '24':'двадцать четвертое','25':'двадцать пятое','26':'двадцать шестое','27':'двадцать седьмое',
       '28':'двадцать восьмое','29':'двадцать девятое','30':'тридцатое','31':'тридцать первое'}
month = {'01':'января', '02':'февраля', '03':'марта', '04':'апреля', '05':'мая', '06':'июня','07':'июля',
         '08':'августа', '09':'сентября', '10':'октября', '11':'ноября', '12':'декабря'}
print("{} {} {} года".format(day[test_date[0:2]], month[test_date[3:5]], test_date[6:10]))


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

n = int(input('Введите количество элементов'))
my_list = []
while n > 0:
    my_list.append(random.randint(-100, 100))
    n -= 1
print("Случайный список", my_list)


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]
my_list = [1, 2, 4, 5, 6, 2, 5, 2]
new_list = []
print(set(my_list))

for i in set(my_list):
    new_list.append(i)
print(new_list)

for i in set(my_list):
    count = 0
    for ii in my_list:
        if i == ii:
            count += 1
    if count > 1:
        new_list.remove(i)

print(new_list)