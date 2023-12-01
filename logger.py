import csv
import json
import logging

def overwrite_csv():
    with open("logs/alive.csv", "w", newline=""):
        pass

def overwrite_json():
    with open("logs/pos.json", "w+", newline="") as jsonfile:
        json.dump([], jsonfile, indent=4)
        jsonfile.seek(0)
        return json.load(jsonfile)
def overwrite_log():
    with open("logs/log.log", "w", newline=""):
        pass

def log_to_csv(message):
    with open("logs/alive.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(message)

def log_to_json(list_of_dicts):
    with open("logs/pos.json", "w", newline="") as jsonfile:
        jsonfile.seek(0)
        json.dump(list_of_dicts, jsonfile, indent=4)

def log_to_log(message, log_level, intended_log_level):
    with open("logs/log.log", "a", newline=""):
        if log_level is not None:
            logging.basicConfig(filename="logs/log.log", level=log_level)
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
