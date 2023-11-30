import random


class Sheep:

    def __init__(self):
        self.position = [random.uniform(-10, 10), random.uniform(-10, 10)]

    def move(self):
        x = random.randint(1, 4)
        match x:
            case 1:
                self.position[0] += 0.5
            case 2:
                self.position[0] -= 0.5
            case 3:
                self.position[1] += 0.5
            case 4:
                self.position[1] -= 0.5
