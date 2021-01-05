class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f"{self.name} is going"
    def stop(self):
        return f"{self.name} is stop"
    def turn_right(self):
        return f"{self.name} turn on right"
    def turn_left(self):
        return f"{self.name} turn on left"
    def show_speed(self):
        return f"{self.name} - {self.speed}"
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super(). __init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60:
            return f"Speed is higher"
        else:
            return f"Speed is normal"
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super(). __init__(speed, color, name, is_police)
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super(). __init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40:
            return f"Speed is higher"
        else:
            return f"Speed is normal"
class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super(). __init__(speed, color, name, is_police)
total = TownCar(60, "Blue", "Mini", False)
total1 = SportCar(180, "Silver", "BMW", False)
total2 = WorkCar(50, "White", "VW", True)
total3 = PoliceCar(120, "Green", "Skoda", True)
print(total.go(),total.turn_left(), total.is_police, total.show_speed())
print(total1.go(),total1.turn_left(), total1.is_police, total1.show_speed())
print(total2.go(),total2.turn_left(), total2.is_police, total2.show_speed())
print(total3.go(),total3.turn_left(), total3.is_police, total3.show_speed())
