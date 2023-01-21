# 3. Еще немного о друзьях
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст)
# своих N друзей. Создайте список friends и добавьте в него N словарей с ключами
# name и age. Выведите средний возраст всех друзей и самое длинное имя.

n = int(input('Введи число друзей: '))
friends = []
for i in range(n):
    name = input('Введи имя друга: ')
    age = int(input('Введи возраст друга: '))
    new_friend = {'name': name, 'age' : age}
    friends.append(new_friend)
ind = 0
name_len = 0
mid_age = 0
for i in range(len(friends)):
    mid_age += friends[i]['age']
    if name_len < len(friends[i]['name']):
        name_len = len(friends[i]['name'])
        ind = i
mid_age = round(mid_age / len(friends))
print(mid_age, friends[ind]['name'])