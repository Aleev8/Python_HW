#Создайте список из случайных чисел. Найдите количество различных
# элементов в нем.

import random
list1 = [random.randint(1, 15) for i in range(random.randint(10, 18))]
print("Сгенерирован список: ", list1)
list_res = []
for i in range(len(list1)):
    if list1.count(list1[i]) == 1:
        list_res.append(list1[i])
print('Количество различающихся элементов=', len(list_res))

#Решение преподавателя
some_list = [random.randint(1, 15) for i in range(random.randint(10, 18))]
print("Сгенерирован список: ", some_list)
some_set = set(some_list)
print(len(some_set))
