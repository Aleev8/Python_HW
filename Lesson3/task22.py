"""Задайте список из нескольких чисел. Напишите программу, которая найдёт
 сумму элементов списка, стоящих на нечётной позиции.
Пример:
- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12"""

import random
list_len = random.randint(5, 12)
test_list = []
sum = 0
for i in range(list_len):
    test_list.append(random.randint(1, 100))
for i in range(list_len):
    if i % 2 == 1:
        sum += test_list[i]
print(test_list)
print(sum)

# Решение преподавателя
# sum = 0
# some_list = input().split()
# for i in range(1, len(some_list), 2):
#     sum += int(some_list[i])
# print(sum)
