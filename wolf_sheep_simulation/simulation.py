import logging
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
            self.sheep_alive.append(sheep.Sheep(sheep_spawn_limit, sheep_speed, i))
        logging.info("position of all sheep was established")
        self.sheep_status = self.sheep_alive.copy()

        logger.overwrite_csv()

        self.json_data = logger.overwrite_json()

    def simulate_round(self):
        logging.info("round %i was started" % self.no_round)
        for animal in self.sheep_alive:
            animal.move()
        logging.info("all sheep moved")

        wolf_target = self.wolf.move(self.sheep_status)

        if self.wolf.position == wolf_target.position:
            self.sheep_alive.remove(wolf_target)
            wolf_target.position = [None, None]
            logging.info("sheep %i was eaten" % self.sheep_status.index(wolf_target))

        print("round:", self.no_round,
              "wolf x:", round(self.wolf.position[0], 3),
              "wolf y:", round(self.wolf.position[1], 3),
              "sheep alive:", len(self.sheep_alive),
              "eaten: " if wolf_target.position == [None, None]
              else "chasing:", self.sheep_status.index(wolf_target))

        logger.log_to_csv([self.no_round, len(self.sheep_alive)])
        logging.debug("data was logged to csv file")

        sheep_data = []
        for s in self.sheep_status:
            sheep_data.append((s.position[0], s.position[1]))
        dictionary = {"no_round": self.no_round,
                      "wolf_pos": (self.wolf.position[0], self.wolf.position[1]),
                      "sheep_pos": sheep_data}
        self.json_data.append(dictionary)
        logger.log_to_json(self.json_data)
        logging.debug("data was logged to json file")

        logging.info("the round %i is about to end, the number of sheep alive: %i"
                          % (self.no_round, len(self.sheep_alive)))
        if self.do_wait:
            input("waiting for input")

    def perform_simulation(self, rounds_amt):
        for i in range(rounds_amt):
            self.simulate_round()
            self.no_round += 1
            if len(self.sheep_alive) == 0:
                print("All sheep were eaten")
                logging.info("the simulation terminates due to all sheep being eaten")
                return
        logging.info("the simulation terminates due to maximum amount of rounds being reached")
        print("%i rounds passed" % rounds_amt)
