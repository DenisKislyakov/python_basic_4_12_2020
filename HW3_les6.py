class Worker:
    name = None
    surname = None
    position = None
    income = None
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
    def full_name(self):
        return self.name + " " + self.surname
    def full_income(self):
        return self._income.get("wage") + self._income.get("bonus")
total = Position('Sam', 'Cook', 'Teacher', 70000, 12000)
print(total.full_name())
print(total.position)
print(total.full_income())
