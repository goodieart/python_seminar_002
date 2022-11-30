# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

def generate_seq(n):
    return [(1 + 1 / n) ** n for n in range(1, n + 1)] # простите за listcomp

user_input = int(input('Введите число n: '))
print(f'Результирующая последовательность: {generate_seq(user_input)}')