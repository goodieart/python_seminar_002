# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def fib(n):
    result = []
    for i in range(1, n + 1):
        mul = 1
        for j in range(1, i + 1):
            mul *= j
        result.append(mul)
    return result

user_input = int(input('Введите число N: '))
print(f'Набор произведений чисел от 1 до N: {fib(user_input)}')