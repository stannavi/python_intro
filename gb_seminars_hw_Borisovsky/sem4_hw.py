# задача 1. Задайте натуральное число N.
# Напишите программу, которая составит список простых
# множителей числа N.

n = int(input("Введите число: "))
print("Сисок простых множителей числа N:")
simple_mult = 2
list_simple_mult = []
while simple_mult <= n:
    if n % simple_mult == 0:
        list_simple_mult.append(simple_mult)
        n //= simple_mult
        simple_mult = 2
    else:
        simple_mult += 1

print(list_simple_mult)