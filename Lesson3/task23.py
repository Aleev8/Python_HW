"""Напишите программу, которая найдёт произведение пар чисел
списка. Парой считаем первый и последний элемент, второй и предпоследний
и т.д.
Пример:
- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]"""

import random
list_len = random.randint(5, 12)
test_list = []
multiplier_list = []
middle_of_list = int(list_len / 2)
j = len(test_list) - 1

for i in range(list_len):
    test_list.append(random.randint(1, 100))

for i in range(middle_of_list):
    multiplier_list.append(test_list[i] * test_list[j])
    j -= 1
print(test_list, '=>', multiplier_list)
