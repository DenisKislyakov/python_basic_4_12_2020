import time
class TrafficLight:
    colors = ["Красный", "Желтый", "Зеленый"]
    def running(self):
        color = 0
        while color < 3:
            if color == 0:
                time.sleep(7)
            if color == 1:
                time.sleep(2)
            if color == 2:
                time.sleep(30)
            print(f'{TrafficLight.colors[color]}')
            color += 1
TrafficLight = TrafficLight()
TrafficLight.running()
