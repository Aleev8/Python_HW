"""Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран
их сумму.
Пример:
-Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
Сумма 9.06 """

# n = int(input('Введите количество чисел в списке:  '))
# sum = 0
# for i in range(n):
#     a = int(input(f'Введи число {i + 1}: '))
#     a = (1+1/a)**a
#     sum += a
#     i += 1
# print('Сумма чисел равна', round(sum, 2))

n = int(input('Введите число: '))
some_dict = {}
for i in range (1, n + 1):
    some_dict[i] = (1 + 1 / i) ** i
print(some_dict, round(sum(some_dict.values()), 2))