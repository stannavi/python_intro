# Задача 1.
# Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать.

# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

from fractions import Fraction

a = Fraction(input("Введите число: "))
digit_sum = 0
while a > 0:
    if a % 1 == 0:
        digit_sum = digit_sum + a % 10
        a = a // 10
    else:
        while a % 1 != 0:
            a = a * 10

print("Сумма цифр числа a: ", digit_sum)

