import random


class Sheep:

    def __init__(self, spawn_limit, speed):
        self.position = [random.uniform(-spawn_limit, spawn_limit), random.uniform(-spawn_limit, spawn_limit)]
        self.speed = speed
        self.direction = None

    def chose_direction(self):
        x = random.randint(1, 4)
        match x:
            case 1:
                self.direction = "right"
            case 2:
                self.direction = "left"
            case 3:
                self.direction = "up"
            case 4:
                self.direction = "down"

    def move(self):
        x = random.randint(1, 4)
        match x:
            case "right":
                self.position[0] += self.speed
            case "left":
                self.position[0] -= self.speed
            case "up":
                self.position[1] += self.speed
            case "down":
                self.position[1] -= self.speed
