import random


class Sheep:

    def __init__(self, spawn_limit, speed):
        self.position = [random.uniform(-spawn_limit, spawn_limit), random.uniform(-spawn_limit, spawn_limit)]
        self.speed = speed

    def move(self):
        x = random.randint(1, 4)
        match x:
            case 1:
                self.position[0] += self.speed
            case 2:
                self.position[0] -= self.speed
            case 3:
                self.position[1] += self.speed
            case 4:
                self.position[1] -= self.speed
