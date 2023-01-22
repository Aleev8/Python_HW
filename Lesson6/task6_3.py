# 2. Старший и младший
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст)
# своих N друзей. Создайте список friends и добавьте в него N словарей с ключами
# name и age. Найдите самого младшего из друзей и выведите его имя.

n = int(input('Введи число друзей: '))
friends = []
for i in range(n):
    name = input('Введи имя друга: ')
    age = int(input('Введи возраст друга: '))
    friends.append(dict(name=name, age=age))
print(friends)
min_age = min(friends, key=lambda x: x['age'])
print('Младшего друга зовут - ', min_age['name'])




