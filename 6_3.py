class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._wage = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._wage.values())


w_1 = Position("Viktor", "Kain", "Manager", 30000, 5000)
print(w_1.get_full_name())
print(w_1.get_total_income())