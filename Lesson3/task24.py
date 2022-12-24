"""Задайте список из вещественных чисел. Напишите программу,
которая найдёт разницу между максимальным и минимальным значением
дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19"""

import random
list_len = random.randint(5, 12)
test_list = []
for i in range(list_len):
    test_list.append(round(random.uniform(0, 9), 2))
result_list = [round(i % 1, 2) for i in test_list]
print(test_list, '=>', round(max(result_list) - min(result_list), 2))

# Решение преподавателя через строки

# some_list = input().split()
# maxx = 0
# minn = 1
# for el in some_list:
#     if '.' in el:
#         number = el.split('.')[1]
#         if int(number) != 0:
#             if float('0.' + number) < minn:
#                 minn = float('0.' + number)
#             elif float('0.' + number) > maxx:
#                 maxx = float('0.' + number)
# print(maxx - minn)

# Решение через математику

# some_list = input().split()
# maxx = 0
# minn = 1
# for el in some_list:
#     if float(el) % 1 != 0:
#         if float(el) % 1 < minn:
#             minn = float(el) % 1
#         if float(el) % 1 > maxx:
#             maxx = float(el) % 1
# print(round(maxx - minn, 2))