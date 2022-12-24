"""НЕОБЯЗАТЕЛЬНАЯ Задайте число. Составьте список чисел
Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так:
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] """

k = int(input())
some_list = [0] * (k * 2 + 1)
some_list[k + 1] = 1
some_list[k - 1] = 1
for ind in range(k + 2, k * 2 + 1):
    some_list[ind] = some_list[ind - 1] + some_list[ind - 2]
for ind in range(k - 2, -1, -1):
    some_list[ind] = some_list[ind + 2] - some_list[ind + 1]
print(some_list)