# На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
#
#  5 -> 1 0 1 1 0
# 2

# n = int(input("Введите колличество монеток: "))
# n_reshka = int(input("Скоько монеток лежит решкой?: "))
# n_rebro = n - n_reshka
# if n_rebro < n_reshka:
#     print(f'Нужно перевернуть ребро монет {n_rebro} раз')
# else:
#     print(f'Нужно перевернуть решку {n_reshka} раз')


# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3
# summ = int(input('summ = '))
# mult = int(input('mult = '))
# x, y = 0, 0
# for i in (1, summ//2+1):
#     if i*(summ-i) == mult:
#         x = i
#         y = summ - i
# print(x, y)



# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

# n = int(input('N: '))
# count = 1
# while count < n:
#     print(count, end=' ')
#     count *= 2
