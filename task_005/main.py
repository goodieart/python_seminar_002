# Реализуйте алгоритм перемешивания списка

import random

# Избегаем использования random.shuffle
def list_shuffle(value):
    value_len = len(value)
    for _ in range(value_len):
        rand = random.randint(0, value_len - 1)
        buffer = value.pop(rand)
        value.append(buffer)


user_input = list(
    map(int, input('Введите исходные числа через запятую: ').split(',')))

print(f'Исходный список: {user_input}')
list_shuffle(user_input)
print(f'Перемешанный список: {user_input}')
