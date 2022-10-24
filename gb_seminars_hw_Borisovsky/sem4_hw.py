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


# задача 2 . Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся
# элементов исходной последовательности.

numbers = [2, 3, 45, 4, 2, 1, 1, 10, 3, 2, 15, 1]

def unique_numbers_list(numbers):
    unique = []
    for i in numbers:
        if i in unique:
            continue
        else:
            unique.append(i)
    return unique

print(unique_numbers_list(numbers))
