import sheep
import wolf
import logger


class Simulation:

    def __init__(self, wolf_speed, sheep_spawn_limit, sheep_speed, sheep_amount, do_wait):
        self.no_round = 1
        self.sheep_alive = []
        self.wolf = wolf.Wolf(wolf_speed)
        self.json_data = None
        self.do_wait = do_wait

        for i in range(sheep_amount):
            self.sheep_alive.append(sheep.Sheep(sheep_spawn_limit, sheep_speed))
            logger.log_to_log("sheep %i initial position was established: %s"
                              % (i, self.sheep_alive[i].position), 10)
        logger.log_to_log("position of all sheep was established", 20)
        self.sheep_status = self.sheep_alive.copy()

        logger.overwrite_csv()

        self.json_data = logger.overwrite_json()

    def simulate_round(self):
        logger.log_to_log("round %i was started" % self.no_round, 20)
        for animal in self.sheep_alive:
            animal.chose_direction()
            logger.log_to_log("sheep %i chose it's direction: %s"
                              % (self.sheep_status.index(animal), animal.direction), 10)
            animal.move()
            logger.log_to_log("sheep %i made it's move to: %s"
                              % (self.sheep_status.index(animal), animal.position), 10)
        logger.log_to_log("all sheep moved", 20)

        #wersja bardziej logiczna
        wolf_target, distance = self.wolf.estimate_target(self.sheep_alive)
        logger.log_to_log("wolf determined that sheep %i is the closest, distance is: %f"
                          % (self.sheep_status.index(wolf_target), distance), 10)
        self.wolf.move2()
        logger.log_to_log("wolf made its move to: %s" % self.wolf.position, 10)

        #wersja mniej logiczna
        #wolf_target = self.wolf.move(self.sheep_alive)
        if self.wolf.position == wolf_target.position:
            self.sheep_alive.remove(wolf_target)
            wolf_target.position = [None, None]
            logger.log_to_log("sheep %i was eaten" % self.sheep_status.index(wolf_target), 20)

        print("round:", self.no_round,
              "wolf x:", round(self.wolf.position[0], 3),
              "wolf y:", round(self.wolf.position[1], 3),
              "sheep alive:", len(self.sheep_alive),
              "eaten: " if wolf_target.position == [None, None]
              else "chasing:", self.sheep_status.index(wolf_target))

        logger.log_to_csv([self.no_round, len(self.sheep_alive)])
        logger.log_to_log("data was logged to csv file", 10)

        sheep_data = []
        for s in self.sheep_status:
            sheep_data.append((s.position[0], s.position[1]))
        no_round = {"no_round": self.no_round}
        wolf_pos = {"wolf_pos": (self.wolf.position[0], self.wolf.position[1])}
        sheep_pos = {"sheep_pos": sheep_data}
        data = [no_round, wolf_pos, sheep_pos]

        self.json_data.append(data)
        logger.log_to_json(self.json_data)
        logger.log_to_log("data was logged to json file", 10)

        logger.log_to_log("the round %i is about to end, the number of sheep alive: %i"
                          % (self.no_round, len(self.sheep_alive)), 20)
        if self.do_wait:
            input("waiting for input")

    def perform_simulation(self, rounds_amt):
        for i in range(rounds_amt):
            self.simulate_round()
            self.no_round += 1
            if len(self.sheep_alive) == 0:
                print("All sheep were eaten")
                logger.log_to_log("the simulation terminates due to all sheep being eaten", 20)
                return
        logger.log_to_log("the simulation terminates due to maximum amount of rounds being reached", 20)
        print("%i rounds passed" % rounds_amt)