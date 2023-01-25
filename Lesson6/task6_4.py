# 3. Еще немного о друзьях
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст)
# своих N друзей. Создайте список friends и добавьте в него N словарей с ключами
# name и age. Выведите средний возраст всех друзей и самое длинное имя.

# from statistics import mean
#
# friends = {}
# new_dict= ()
# lenght = int(input('Введите кол-во друзей: '))
#
# for name in range(lenght):
#     name = input('Введите имя друга: ')
#     friends[name] = int(input('Введите возраст друга: '))
# dict_mean = mean(friends.values())
# max_name = max(friends, key=len)
# print(dict_mean)
# print(max_name)

# Teacher solved
N = int(input('Введи число друзей: '))
dict_list = []
for _ in range(N):
    name = input('Введи имя друга: ')
    age = int(input('Введи возраст друга: '))
    dict_list.append({'name': name, 'age': age})
print(dict_list)
summ = 0
max_name = dict_list[0]['name']
for i in dict_list:
    summ += i['age']
    if len(i['name']) > len(max_name):
        max_name = i['name']
print(summ / N)
print(max_name)


