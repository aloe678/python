class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"{self.title} пишет")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title} рисует")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title} окрашивает")


s_1 = Pen("Ручка")
s_1.draw()

s_2 = Pencil("Карандаш")
s_2.draw()

s_3 = Handle("Маркер")
s_3.draw()
