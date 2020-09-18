"""2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""

while True:
    user_list = (input('Вводите целые числа через запятую: ')).split(',')
    try:
        for ind, number in enumerate(user_list):
            user_list[ind] = int(number)
        break
    except ValueError:
        print('Введены не числа')
        continue


def list_changer(some_list: list) -> list:
    """
    Функция, создающая список из элементов исходного списка, значения которых больше предыдущего элемента
    :param some_list: list
    :return: list
    """
    result_list = [num for i, num in enumerate(some_list) if some_list[i] > some_list[i - 1] and i != 0]
    return result_list


print(list_changer(user_list))

assert list_changer([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]) == [12, 44, 4, 10, 78, 123], 'Ошибка функции'
