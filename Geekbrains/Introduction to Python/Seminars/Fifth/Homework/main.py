# Задача 26:  Напишите программу, которая на вход принимает два
# числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

# x = int(input('Введите первое число A: '))
# y = int(input('Введите второе число B: '))

# def pow(a ,n):
#     if (n == 1):
#         return (a)
#     if (n !=1):
#         return(a * pow(a, n-1))
# print(pow(x,y))





# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4


# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# def sum(a,b):
#     if (a == 0):
#       return b
#     else:
#         return sum(a-1,b+1)
# print(sum(a,b))