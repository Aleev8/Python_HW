# 2. Старший и младший
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст)
# своих N друзей. Создайте список friends и добавьте в него N словарей с ключами
# name и age. Найдите самого младшего из друзей и выведите его имя.

n = int(input('Введи число друзей: '))
friends = []
for i in range(n):
    name = input('Введи имя друга: ')
    age = int(input('Введи возраст друга: '))
    new_friend = {'name': name, 'age' : age}
    friends.append(new_friend)
min_age = friends[0]['age']
count = 0
for i in range(len(friends)):
    if min_age > friends[i]['age']:
        min_age = friends[i]['age']
        count = i
print(friends[count]['name'])




