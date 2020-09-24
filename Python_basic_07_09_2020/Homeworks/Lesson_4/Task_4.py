"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.
Для выполнения задания обязательно использовать генератор.
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
    Функция, создающая новый список на основании исходного, но без повторения элементов
    :param some_list: list
    :return: list
    """
    result_list = [el for el in some_list if some_list.count(el) == 1]
    return result_list


print(list_changer(user_list))

assert list_changer([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]) == [23, 1, 3, 10, 4, 11], 'Ошибка функции'
