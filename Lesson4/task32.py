"""Задайте последовательность чисел. Напишите программу, которая выведет список
неповторяющихся элементов исходной последовательности."""

import random
list_len = random.randint(8, 18)
test_list = [random.randint(66, 99) for i in range(list_len)]
print(f"Исходный список: {test_list}")
new_list = []
[new_list.append(i) for i in test_list if i not in new_list]
print(f"Список из неповторяющихся элементов: {new_list}")