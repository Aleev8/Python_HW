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
result_list = [round(i%1,2) for i in test_list]
print(test_list, '=>', round(max(result_list) - min(result_list), 2))
