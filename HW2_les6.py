class Road:
    lenght = None
    width = None
    def __init__(self,lenght, width):
        self.lenght = lenght
        self.width = width

    def sum(self):
        self.weigth = 25
        self.tickness = 0.05
        sum = self.lenght * self.width * self.weigth * self.tickness
        print(f' {sum} ')
Road = Road(150000, 4)
Road.sum()
