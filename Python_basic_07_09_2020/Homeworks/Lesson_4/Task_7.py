"""
 Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
 При вызове функции должен создаваться объект-генератор.
 Функция должна вызываться следующим образом: for el in fact(n).
  Функция отвечает за получение факториала числа,
  а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
"""

while True:
    try:
        number = int(input('Введите целое число для получения факториала: '))
        break
    except ValueError:
        print('Введено не число')


def fact(n: int) -> object:
    """
    Функция, возвращающая факториал числа
    :param n: int
    :return: object
    """
    result = 1
    for num in range(1, n + 1):
        result *= num
        yield result


for ind, el in enumerate(fact(number)):
    print(f'Число:{ind + 1}, факториал: {el}')
