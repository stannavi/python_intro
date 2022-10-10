# типы данных и переменная
# int, float, boolean, str, list, None
# value = None
# print(type(value))
# a = 123
# b = 1.23
# print(a)
# print(b)
value = 12334
# print(type(value))
# s = 'hello nworld'

# print(s) # вывод строки
# print(a, ' - ', b, ' - ', s)
# print('{1} - {2} - {0}'.format(a, b, s)) # формат
# print(f'{a} - {b} - {s}') # интерполяция

# f = False
# print(f)

# list = ['1', '2', '3']
# print(list)

# Ввод-вывод данных
# print('Введите a')
# a = int(input())
# print('Введите b')
# b = int(input())
# print(a, ' + ', b, ' = ', a + b)


# АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ
# a = 1.31231223
# b = 3
# c = round(a * b, 7)
# print(c)

# a = 3
# a += 5
# print(a)


# ЛОГИЧЕСКИЕ ОПЕРАЦИИ
# a = [1, 2]
# b = [1, 2]
# print(a == b)

# a = 1 < 3 < 5 > 7
# print(a)

# func = 1
# T = 4
# x = 2
# print(func < T > x)

# f = [1, 2, 3, 4]
# print(f)
# print(not 2 in f)

# is_odd = f[0] % 2 == 0
# print(is_odd)


# if, if-else

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# while, do while
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10 # целочисленное деление на 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# for
# for i in range(1, 10, 2):
#     print(i)


# СТРОКИ
# text = 'съешь ещё этих мягких французских булок'
# print(text[0])
# print(len(text))


# help(int) # помощь

# ФУНКЦИИ
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return
arg = 2.3
print(f(arg))
print(type(f(arg)))
