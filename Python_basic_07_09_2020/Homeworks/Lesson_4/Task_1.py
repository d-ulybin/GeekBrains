"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv


def salary_counter(total_hours: float, hour_rate: float, bonus: float) -> float:
    """
    Функция для рассчета заработной платы
    :param total_hours: float
    :param hour_rate: float
    :param bonus: float
    :return: float
    """
    return float(total_hours) * float(hour_rate) + float(bonus)


_, total_hours, hour_rate, bonus = argv

print(f'Заработная плата сотрудника составляет: {salary_counter(total_hours, hour_rate, bonus)}')

# Проверка:
# python C:\Users\dvuly\PycharmProjects\GeekBrains\Python_basic_07_09_2020\Homeworks\Lesson_4\Task_1.py 160 100 5000
