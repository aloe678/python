class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print(f"{self.name} начинает движение")

    def stop(self):
        print(f"{self.name} останавливается")

    def turn(self, direction):
        print(f"{self.name} поворачивает {direction}")

    def show_speed(self):
        print(f"{self.name} движется со скоростью {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        print(f"{self.speed} км/ч. Превышение скорости") if self.speed > 60 else print(f"{self.name} движется со скоростью {self.speed} км/ч")


class WorkCar(Car):
    def show_speed(self):
        print(f"{self.speed} км/ч. Превышение скорости") if self.speed > 40 else print(f"{self.name} движется со скоростью {self.speed} км/ч")


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


auto_1 = TownCar(70, "Чёрный", "Тойота", 0)
auto_1.go()
auto_1.turn("направо")
auto_1.show_speed()
auto_1.stop()