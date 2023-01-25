# 2. Старший и младший
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст)
# своих N друзей. Создайте список friends и добавьте в него N словарей с ключами
# name и age. Найдите самого младшего из друзей и выведите его имя.

# n = int(input('Введи число друзей: '))
# friends = []
# for i in range(n):
#     name = input('Введи имя друга: ')
#     age = int(input('Введи возраст друга: '))
#     friends.append(dict(name=name, age=age))
# print(friends)
# min_age = min(friends, key=lambda x: x['age'])
# print('Младшего друга зовут - ', min_age['name'])

# Решение преподавателя
N = int(input())
dict_list = []
for _ in range(N):
    name = input('Введи имя друга: ')
    age = int(input('Введи возраст друга: '))
    dict_list.append({'name': name, 'age': age})
print(dict_list)
min_age = dict_list[0]['age']
for some_dict in dict_list:
    if some_dict['age'] < min_age:
        min_age = some_dict['age']
for some_dict in dict_list:
    if some_dict['age'] == min_age:
        print(some_dict['name'])
        break



