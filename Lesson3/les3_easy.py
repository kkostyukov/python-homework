# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits=0):
    numbers = str(number).split(".")
    if len(numbers) == 1 or len(numbers[1]) <= ndigits:
        return number
    num1 = numbers[0]
    num2 = numbers[1][:ndigits]
    num3 = numbers[1][ndigits:]
    mod = 0
    for i in num3[::-1]:
        if int(i) + mod >= 6:
            mod = 1
        else:
            mod = 0
    if mod == 0:
        result = num1 + "." + num2
        return float(result)
    else:
        if num2 == '' or len(num2) != len(str(int(num2) + mod)):
            return int(num1) + 1
        else:
            num2 = int(num2) + mod
            result = num1 + "." + str(num2)
            return float(result)


print(my_round(2.1234567, 6))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(9.94567))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
def sum_numbres(number):
    sum_number = 0
    for i in str(number):
        sum_number += int(i)
    return sum_number


def lucky_ticket(ticket_number):
    if len(str(ticket_number)) != 6:
        return "Не шести значный номер билета"
    else:
        if sum_numbres(str(ticket_number)[:3]) == sum_numbres(str(ticket_number)[4:]):
            return "Счастливый билет"
        else:
            return "Билет не счастливый"
    pass


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))