import math


class Wolf:

    def __init__(self):
        self.position = [0.0, 0.0]
        self.target = None

    def move(self, targets):
        self.target = targets[0]
        distance = math.dist(self.target.position, self.position)
        for target in targets:
            currentDistance = math.dist(target.position, self.position)
            if distance > currentDistance:
                distance = currentDistance
                self.target = target
        if distance < 1.0:
            self.position = self.target.position
        else:
            self.position[0] = self.position[0] - 1*(self.position[0] - self.target.position[0]) / distance
            self.position[1] = self.position[1] - 1*(self.position[1] - self.target.position[1]) / distance
        return self.target
