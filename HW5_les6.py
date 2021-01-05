class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f"Запуск отрисовки {self.title}"
class Pen(Stationery):
    def __init__(self, title):
        super(). __init__(title)
    def draw(self):
        return f"Отрисовка {self.title}"
class Pensil(Stationery):
    def __init__(self, title):
        super(). __init__(title)
    def draw(self):
        return f"Отрисовка {self.title}"
class Handle(Stationery):
    def __init__(self, title):
        super(). __init__(title)
    def draw(self):
        return f"Отрисовка {self.title}"
Pen = Pen("Ручкой")
Pensil = Pensil("Карандашом")
Handle = Handle("Маркером")
print(Pen.draw())
print(Pensil.draw())
print(Handle.draw())
