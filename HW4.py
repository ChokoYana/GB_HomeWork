# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# n = int(input('введите колличество элемнтов 1 множества: '))
# first_list = input('Введите элементы: ').split()[:n]
# m = int(input('введите колличество элемнтов 2 множества: '))
# second_list = input('Введите элементы: ').split()[:m]
#
# def find_elem(a_list, b_list):
#     find_list = []
#     for i in a_list:
#         if i in b_list:
#             find_list.append(i)
#     print(sorted(set(map(int, find_list))))
#
#
# find_elem(first_list, second_list)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9


# def print_user():
#     n = int(input('Введите колличество кустов: '))
#     a = []
#     for i in range(n):
#         new_element = int(input(f'Ведите колличество ягод на {i+1} кусте: '))
#         a.append(new_element)
#
#     return a, n
#
#
# def max_sum(num, n):
#     max_berries = 0
#     for i in range(n):
#         sum_berries = num[i] + num[i-1] + num[i-2]
#         if max_berries < sum_berries:
#             max_berries = sum_berries
#     print(f'Максимальная сумма ягод на 3 кустах {max_berries}')
#
# berries, bushes = print_user()
# print(berries, bushes)
# max_sum(berries, bushes)
