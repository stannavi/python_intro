# Задача 1.
# Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр.
# Через строку нельзя решать.

# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

from fractions import Fraction


# a = Fraction(input("Введите число: "))
# digit_sum = 0
# while a > 0:
#     if a % 1 == 0:
#         digit_sum = digit_sum + a % 10
#         a = a // 10
#     else:
#         while a % 1 != 0:
#             a = a * 10
#
# print("Сумма цифр числа a: ", digit_sum)

# Задача 2.
# Напишите программу, которая принимает на вход число N и выдает набор произведений
# чисел от 1 до N.

# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(number, count = 1):
    for i in range(1, number + 1):
        count *= i
    return count

N = int(input("Введите число: "))
print(f'Набор произведений чисел от 1 до {N} = ', end='')
for i in range(1, N + 1):
    if i == N:
        print(f'{factorial(i)}')
    else:
        print(f'{factorial(i)}', end=', ')


# Задача 3.
# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.
# Нельзя юзать find или count.
string1 = input('Введите строку, где ищем: ')
string2 = input('Введите строку, что ищем: ')

l2 = len(string2)
count = 0
for i in range(0, len(string1) - l2 + 1):
   temp = string1[i : i + l2]
   if(temp == string2): count += 1
print(count)