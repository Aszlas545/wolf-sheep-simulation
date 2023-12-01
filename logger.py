import csv
import json
import logging

logger = logging.Logger("logger")
logging.basicConfig(filename="logs/chase.log", format="%(levelname)-8s :: %(asctime)s :: ""%(message)s")


def overwrite_csv():
    with open("logs/alive.csv", "w", newline=""):
        pass


def overwrite_json():
    with open("logs/pos.json", "w+", newline="") as jsonfile:
        json.dump([], jsonfile, indent=4)
        jsonfile.seek(0)
        return json.load(jsonfile)


def overwrite_log(log_level):
    with open("logs/chase.log", "w", newline=""):
        logger.setLevel(log_level)
        handler = logging.Handler()
        logger.addHandler(handler)


def log_to_csv(message):
    with open("logs/alive.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(message)


def log_to_json(list_of_dicts):
    with open("logs/pos.json", "w", newline="") as jsonfile:
        jsonfile.seek(0)
        json.dump(list_of_dicts, jsonfile, indent=4)


def log_to_log(message, intended_log_level):
    with open("logs/chase.log", "a", newline=""):
        print(logger.level)
        if logger.level > 0:
            match intended_log_level:
                case logging.DEBUG:
                    logging.debug(message)
                case logging.INFO:
                    logging.info(message)
                case logging.WARNING:
                    logging.error(message)
                case logging.ERROR:
                    logging.error(message)
                case logging.CRITICAL:
                    logging.critical(message)
