"""Напишите программу, которая будет преобразовывать десятичное
число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10"""

import random
dec_num = random.randint(10, 999)
bin_num = ""
print('Десятичное число = ', dec_num)
while dec_num != 0:
    bin_num = str(dec_num % 2) + bin_num
    dec_num //=2
print('Двоичное число = ', bin_num)

# Лучше делать через списки, строки рабоатют дольше (пересоздаются в памяти)

# n = int(input())
# out_list = []
# while n > 0:
#     out_list.append(str(n % 2))
#     n //= 2
# out_list.reverse()
# print(*out_list, sep='')