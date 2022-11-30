# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

SEPARATOR = '.'

def digits_sum(value):
    result = 0
    value_str = str(value)
    for digit in value_str:
        result += int(0 if digit == SEPARATOR else digit)
    return result

user_input = float(input('Введите число: '))
print(f'Сумма цифр числа равна {digits_sum(user_input)}')