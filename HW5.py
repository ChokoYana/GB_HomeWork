# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# def num_stepen(a, b):
#     if b ==1:
#         return a
#     if b != 1:
#         return a * num_stepen(a, b - 1)
#
# a = int(input('Введите число А: '))
# b = int(input('Введите степень B: '))
# print(num_stepen(a, b))




# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# 2 2
# 4

# def recurse_sum(a, b):
#     if b == 0:
#         return a
#     if b != 0:
#         return a + recurse_sum(1, b - 1)
# a = int(input())
# b = int(input())
# print(recurse_sum(a, b))