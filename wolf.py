import math
import logger


class Wolf:

    def __init__(self, speed):
        self.position = [0.0, 0.0]
        self.speed = speed
        self.target = None

    def move(self, simulation):
        self.target = simulation.sheep_alive[0]
        distance = math.dist(self.target.position, self.position)

        for target in simulation.sheep_alive:
            currentDistance = math.dist(target.position, self.position)
            if distance > currentDistance:
                distance = currentDistance
                self.target = target

        logger.log_to_log("wolf determined that sheep %i is the closest, distance is: %f"
                          % (simulation.sheep_status.index(self.target), distance), 10)

        if distance < self.speed:
            self.position = self.target.position
        else:
            self.position[0] = self.position[0] - self.speed * (self.position[0] - self.target.position[0]) / distance
            self.position[1] = self.position[1] - self.speed * (self.position[1] - self.target.position[1]) / distance

        logger.log_to_log("wolf made it's move to: %s" % self.position, 10)

        return self.target
