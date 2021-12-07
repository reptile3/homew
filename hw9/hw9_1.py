"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5),
стоп (сброс скорости на 0), отображение скорости, задния ход (изменение знака скорости).
"""


class Car:
    def __init__(self, mark, model, age, speed = 0):
        self.mark = mark
        self.model = model
        self.age = age
        self.speed = speed

    def speed_up(self):
        speedup = speed + 5
        print(f"Ur speed now {self.speed}")

    def speed_low(self):
        speedlow = speed - 5
        print(f"Ur speed now {self.speed}")

    def stop(self):
        speed = 0
        print(f"Ur speed now {self.speed}")

    def show_speed(self):
        print(f"Ur speed now {self.speed}")

    def show_speed(self):
        speedshow = speed * -1
        print(f"Ur speed now {self.speed}")


if __name__ == "__main__":
    first_car = Car("Toyota", "f45", 6)
    first_car.speed_up()


    print(first_car.mark)
    print(first_car.model)
    print(first_car.age)
    print(first_car.speed)