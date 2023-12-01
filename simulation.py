import sheep
import wolf
import logger


class Simulation:

    def __init__(self, wolf_speed, sheep_spawn_limit, sheep_speed, sheep_amount, do_wait, log_level):
        self.noRound = 0
        self.sheep_alive = []
        self.wolf = wolf.Wolf(wolf_speed)
        self.json_data = None
        self.do_wait = do_wait
        self.log_level = log_level

        for i in range(sheep_amount):
            self.sheep_alive.append(sheep.Sheep(sheep_spawn_limit, sheep_speed))
        self.sheep_status = self.sheep_alive.copy()

        logger.overwrite_csv()

        self.json_data = logger.overwrite_json()

    def simulate_round(self):
        for animal in self.sheep_alive:
            animal.move()
        val = self.wolf.move(self.sheep_alive)
        if self.wolf.position == val.position:
            self.sheep_alive.remove(val)
            val.position = [None, None]
        self.noRound += 1
        print("round:", self.noRound,
              "wolf x:", round(self.wolf.position[0], 3),
              "wolf y:", round(self.wolf.position[1], 3),
              "sheep alive:", len(self.sheep_alive),
              "eaten: " if val.position == [None, None]
              else "chasing:", self.sheep_status.index(val))
        logger.log_to_csv([self.noRound, len(self.sheep_alive)])

        sheep_data = []
        for s in self.sheep_status:
            sheep_data.append((s.position[0], s.position[1]))
        no_round = {"no_round": self.noRound}
        wolf_pos = {"wolf_pos": (self.wolf.position[0], self.wolf.position[1])}
        sheep_pos = {"sheep_pos": sheep_data}
        data = [no_round, wolf_pos, sheep_pos]

        self.json_data.append(data)
        logger.log_to_json(self.json_data)

        if len(self.sheep_alive) == 0:
            quit("All sheep were slaughtered! " + str(self.noRound) + " rounds were performed")
        if self.do_wait:
            input("waiting for input")
