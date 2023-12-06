import logging
import math


class Wolf:

    def __init__(self, speed):
        self.position = [0.0, 0.0]
        self.speed = speed
        self.target = None
        self.distance = float(math.inf)

    def move(self, possible_targets):
        self.distance = float(math.inf)

        for target in possible_targets:
            if target.position == [None, None]:
                continue
            currentDistance = math.dist(target.position, self.position)
            if self.distance > currentDistance:
                self.distance = currentDistance
                self.target = target
        logging.debug("wolf determined that sheep %i is the closest, distance is: %f"
                      % (self.target.number, self.distance))
        if self.distance < self.speed:
            self.position = self.target.position
        else:
            self.position[0] = (self.position[0] - self.speed *
                                (self.position[0] - self.target.position[0]) / self.distance)
            self.position[1] = (self.position[1] - self.speed *
                                (self.position[1] - self.target.position[1]) / self.distance)
        logging.debug("wolf made its move to: %s" % self.position)
        return self.target