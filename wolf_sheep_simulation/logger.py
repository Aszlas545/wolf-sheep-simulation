import csv
import json
import logging


def overwrite_csv():
    with open("alive.csv", "w", newline=""):
        pass


def overwrite_json():
    with open("pos.json", "w+", newline="") as jsonfile:
        json.dump([], jsonfile, indent=4)
        jsonfile.seek(0)
        return json.load(jsonfile)


def overwrite_log(log_level):
    with open("chase.log", "w", newline=""):
        logging.basicConfig(filename="chase.log",
                            level=log_level,
                            format="%(levelname)-8s :: %(filename)-13s :: %(asctime)s :: ""%(message)s")


def log_to_csv(message):
    with open("alive.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(message)


def log_to_json(list_of_dicts):
    with open("pos.json", "w", newline="") as jsonfile:
        jsonfile.seek(0)
        json.dump(list_of_dicts, jsonfile, indent=4)
