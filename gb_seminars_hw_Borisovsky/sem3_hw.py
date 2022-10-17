# Задача 1 Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9,
# ответ: 12

import random

list_size = int(input("Введите размер списка: "))
list = []
sum = 0
for i in range(list_size):
    list.append(random.randint(0, 100))
    if i % 2 != 0:
        sum += list[i]

print(list)
print(sum)

# Задача 2. Напишите программу, которая найдёт произведение
# пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list_size = int(input("Введите размер списка: "))
list = []
list2 = []

for i in range(list_size):
    list.append(int(input("Введите число: ")))

for i in range(len(list)):
    while i < len(list) / 2 < list_size:
        list_size -= 1
        a = list[i] * list[list_size]
        list2.append(a)
        i += 1

print(list)
print(list2)

# Задача 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.

# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from decimal import Decimal

my_list = [1.6, 1.2, 3.1, 5.04, 10.06]
max = 0
min = 1

for i in my_list:
    if(i - int(i)) <= min:
        min = i - int(i)
    if(i - int(i)) >= max:
        max = i - int(i)
print(Decimal(max - min))




