""" 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    temp = float('inf')
    for number in (a, b, c):
        if temp > number:
            temp = number
    result = a + b + c - temp
    return result


print(my_func(-22, 13, -2))
