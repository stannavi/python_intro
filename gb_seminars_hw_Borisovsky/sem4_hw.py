# задача 1. Задайте натуральное число N.
# Напишите программу, которая составит список простых
# множителей числа N.

# n = int(input("Введите число: "))
# print("Сисок простых множителей числа N:")
# simple_mult = 2
# list_simple_mult = []
# while simple_mult <= n:
#     if n % simple_mult == 0:
#         list_simple_mult.append(simple_mult)
#         n //= simple_mult
#         simple_mult = 2
#     else:
#         simple_mult += 1
#
# print(list_simple_mult)


# задача 2 . Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

# numbers = [2, 3, 45, 4, 2, 1, 1, 10, 3, 2, 15, 1]
#
# def unique_numbers_list(numbers):
#     unique = []
#     for i in numbers:
#         if i in unique:
#             continue
#         else:
#             unique.append(i)
#     return unique
#
# print(unique_numbers_list(numbers))



# задача 3. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл
# многочлен степени k.

# *Пример:*
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random


def write_file(st):
    with open('polynomial.txt', 'w') as data:
        data.write(st)


def rnd():
    return random.randint(0, 101)


def create_mn(k):
    lst = [rnd() for i in range(k + 1)]
    return lst


def create_str(sp):
    lst = sp[::-1]
    wr = ''
    if len(lst) < 1:
        wr = 'x = 0'
    else:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                wr += f'{lst[i]}x^{len(lst) - i - 1}'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                wr += f'{lst[i]}x'
                if lst[i + 1] != 0:
                    wr += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                wr += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                wr += ' = 0'
    return wr


k = int(input("Введите натуральную степень k = "))
koef = create_mn(k)
write_file(create_str(koef))

