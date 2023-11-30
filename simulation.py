import sheep
import wolf
import json
import csv
import logging


class Simulation:

    def __init__(self):
        self.noRound = 0
        self.sheep_alive = []
        self.wolf = wolf.Wolf()
        self.json_data = None
        for i in range(50):
            self.sheep_alive.append(sheep.Sheep())
        self.sheep_status = self.sheep_alive.copy()
        with open("logs/alive.csv", "w", newline=""):
            pass
        with open("logs/pos.json", "w", newline="") as jsonfile:
            json.dump([], jsonfile, indent=4)
        with open("logs/pos.json", "r", newline="") as jsonfile:
            self.json_data = json.load(jsonfile)
        with open("logs/log.log", "w", newline=""):
            pass


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
        self.log_to_csv()
        self.log_to_json()
        self.log_to_txt()
        if len(self.sheep_alive) == 0:
            quit("All sheep were slaughtered! " + str(self.noRound) + " rounds were performed")

    def get_sheep_x(self):
        collection = []
        for s in self.sheep_alive:
            collection.append(s.position[0])
        return collection

    def get_sheep_y(self):
        collection = []
        for s in self.sheep_alive:
            collection.append(s.position[1])
        return collection

    def get_sheep_coords(self):
        collection = []
        for s in self.sheep_alive:
            collection.append(s.position)
        return collection

    def log_to_csv(self):
        with open("logs/alive.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=";")
            writer.writerow([self.noRound, self.sheep_alive.__len__()])

    def log_to_json(self):
        with open("logs/pos.json", "r+", newline="") as jsonfile:
            sheep_data = []
            for s in self.sheep_status:
                sheep_data.append((s.position[0], s.position[1]))
            no_round = {"no_round": self.noRound}
            wolf_pos = {"wolf_pos": (self.wolf.position[0], self.wolf.position[1])}
            sheep_pos = {"sheep_pos": sheep_data}
            data = [no_round, wolf_pos, sheep_pos]

            self.json_data.append(data)
            jsonfile.seek(0)
            json.dump(self.json_data, jsonfile, indent=4)

    def log_to_txt(self):
        with open("logs/log.log", "a", newline="") as logfile:
            logging.basicConfig(filename="logs/log.log", level=logging.DEBUG)
            logging.debug("test2")
            logging.info("test")
