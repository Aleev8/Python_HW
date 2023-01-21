#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
#     этого абв текста все вабвс слова, содерабващие содержащие "абв"'
#
# def del_some_words(my_text):
#     my_text = list(filter(lambda word: 'абв' not in word, my_text.split()))
#     return " ".join(my_text)
#
# my_text = del_some_words(my_text)
# print(my_text)

## Решение преподавателя
text = input().split()
res_text = list(filter(lambda word: 'а' not in word and 'б' not in word and 'в' not in word, text))
print(res_text)