"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def divide(x, y):
    if y == 0:
        print('Деление на 0 невозможно!')
        return None
    return x / y


numbers = {'делимое': None, 'делитель': None}

for key in numbers.keys():
    while True:
        tmp = input(f'Введите {key}: ')
        try:
            tmp = int(tmp)
        except ValueError:
            print('Введено не число')
            continue
        numbers[key] = tmp
        break

print(divide(numbers['делимое'], numbers['делитель']))
