import logging
import random


class Sheep:

    def __init__(self, spawn_limit, speed, number):
        self.position = [random.uniform(-spawn_limit, spawn_limit), random.uniform(-spawn_limit, spawn_limit)]
        self.speed = speed
        self.number = number
        logging.debug("sheep %i initial position was established: %s"
                      % (self.number, self.position))
        self.direction = None

    def move(self):
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
        logging.debug("sheep %i chose its direction: %s" % (self.number, self.direction))
        match self.direction:
            case "right":
                self.position[0] += self.speed
            case "left":
                self.position[0] -= self.speed
            case "up":
                self.position[1] += self.speed
            case "down":
                self.position[1] -= self.speed
        logging.debug("sheep %i made its move to: %s" % (self.number, self.position))

