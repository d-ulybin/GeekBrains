"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f'{self.name} повернула {direction}'

    def show_speed(self):
        return f'Скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name)
        self.is_police = False


    def show_speed(self):
        return f'Скорость {self.name} - {self.speed}' \
            if self.speed < 60 else f'Внимание! Превышение скорости! Скорость {self.name} - {self.speed}'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name)
        self.is_police = False



class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name)
        self.is_police = False

    def show_speed(self):
        return f'Скорость {self.name} - {self.speed}' \
            if self.speed < 40 else f'Внимание! Превышение скорости! Скорость {self.name} - {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name)
        self.is_police = True


if __name__ == '__main__':
    town_car = TownCar(80, 'Черный', 'Линкольн')
    work_car = WorkCar(30, 'Белый', 'Фургон')
    sport_car = SportCar(200, 'Красный', 'Ferrari')
    police_car = PoliceCar(100, 'Спецразметка', 'Додж')

    print(town_car.turn('направо'))
    print(police_car.stop())
    print(work_car.go())
    print(town_car.show_speed())
    print(work_car.show_speed())
    print(police_car.show_speed())
    print(police_car.is_police)
