# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

import sys
import os

def parse_file(filename = 'file.txt'):
    with open(os.path.join(sys.path[0], filename), 'r') as f:
        return list(map(int, f.read().split(',')))

def generate_seq(n):
    return [n for n in range(-n, n + 1)]

result = 1
user_input = int(input('Введите число N: '))
seq = generate_seq(user_input)
seq_len = len(seq)
idx = []

print(f'Результирующий список: {seq}')
for i in parse_file():
    if -1 < i < seq_len:
        result *= seq[i]
        idx.append(i)
    else:
        print(f'[!] Индекс {i} выходит за границы списка')

print(f'Произведение элементов на позициях {idx} равно: {result}')