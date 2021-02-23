class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def calculation(self):
        results = self._lenght * self._width * 25 * 5 / 1000
        return f"Необходимая масса асфальта: {results} тонн"


reckoner = Road(4000, 6)
print(reckoner.calculation())