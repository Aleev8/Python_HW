"""Реализуйте алгоритм перемешивания списка."""
from random import Random, randint

n = int(input('Введите длинну задаваемого списка: '))
numbers = []
for i in range(n):
    numbers.append(randint(-n, n + 1))
print(numbers)
list = numbers[:]
numbers_length = len(list)
for i in range(numbers_length):
    index = randint(0, numbers_length - 1)
    temp = list[i]
    list[i] = list[index]
    list[index] = temp
print(list)