""" 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(a, b, c):
    for number in range(3):
        temp = float('inf')
        if temp > number:
            temp = number
    result = a + b + c - temp
    return result


print(my_func(5, 7, 3))
