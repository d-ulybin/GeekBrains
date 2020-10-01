"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep
from itertools import cycle

class TrafficLight:
    def __init__(self):
        self.__color = {'Красный': 6, 'Желтый': 2, 'Зеленый': 6}

    def running(self, rounds):
        counter = 0
        for color, time in cycle(self.__color.items()):
            print(color)
            sleep(time)
            counter += 1/3
            if counter >= rounds:
                break


if __name__ == '__main__':
    tl1 = TrafficLight()
    tl1.running(2)
