# 4. Английский словарь
# "Пора учить английский язык", - сказал себе Степа и решил написать программу
# для изучения английского языка. Программа получает на вход слово на английском
# языке и несколько его переводов на русском языке. Составьте словарь, в котором
# ключ - это английское слово, а значение - это список русских слов.
# В этой задаче нужно использовать строчный метод split().


# eng_dict = {}
# lenght = int(input('Введите кол-во слов: '))
#
# for word in range(lenght):
#     word = input('Введите слово на английском: ')
#     eng_dict[word] = input('Введите перевод: ').split()
# print(eng_dict)

# Teacher solved
# count = int(input('Введите кол-во слов: '))
# translate_dict = {}
# for _ in range(count):
#     eng_rus_str = input()
#     some_list = eng_rus_str.split(' - ')
#     translate_dict[some_list[0]] = some_list[1].split(', ')
# print(translate_dict)
# # Рабочий словарь с выводом по запросу
# eng_word = input('Введите слово для перевода: ')
# if translate_dict.get(eng_word):
#     print(', '.join(translate_dict.get(eng_word)))
# else:
#     print('Такого слова нет')

#Крестики нолики с 2 игроками

def check_win_draw(some_field):
    a1 = some_field[0][0]
    a2 = some_field[0][1]
    a3 = some_field[0][2]

    b1 = some_field[1][0]
    b2 = some_field[1][1]
    b3 = some_field[1][2]

    c1 = some_field[2][0]
    c2 = some_field[2][1]
    c3 = some_field[2][2]

    if a1 == a2 == a3 != '-':
        return f'Победа {a1}'
    elif b1 == b2 == b3 != '-':
        return f'Победа {b1}'
    elif c1 == c2 == c3 != '-':
        return f'Победа {c1}'
    elif a1 == b1 == c1 != '-':
        return f'Победа {a1}'
    elif a2 == b2 == c2 != '-':
        return f'Победа {a2}'
    elif a3 == b3 == c3 != '-':
        return f'Победа {a3}'
    elif a1 == b2 == c3 != '-':
        return f'Победа {a1}'
    elif a3 == b2 == c1 != '-':
        return f'Победа {a3}'
    elif field[0].count('-') == 0 and field[1].count('-') == 0 and field[2].count('-') == 0:
        return 'Ничья'
    else:
        return False

field = [['-' for _ in range(3)] for _ in range(3)]
print(*field, sep='\n')
letter_number = {'a': 0, 'b': 1, 'c': 2}
while True:
    x = input('Ходит Х. Введите номер клетки в формате "букву строки : номер столбца": ')
    if field[letter_number[x[0]]][int(x[-1]) - 1] != '-':
        print('Эта клетка уже занята')
        continue
    field[letter_number[x[0]]][int(x[-1]) - 1] = 'X'
    if check_win_draw(field):
        print(check_win_draw(field))
        break
    o = input('Ходит 0. Введите номер клетки в формате "букву строки : номер столбца": ')
    while field[letter_number[o[0]]][int(o[-1]) - 1] != '-':
        print('Эта клетка уже занята')
        o = input('Ходит 0. Введите номер клетки в формате "букву строки : номер столбца": ')
    field[letter_number[o[0]]][int(o[-1]) - 1] = '0'
    if check_win_draw(field):
        print(check_win_draw(field))
        break
    print(*field, sep='\n')
    print('Играем дальше')

