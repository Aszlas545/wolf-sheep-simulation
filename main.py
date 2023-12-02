import simulation
from pathlib import Path
import argparse
from argparse import RawTextHelpFormatter
import configparser
import logger

# configuration of argument parser
arg_parser = argparse.ArgumentParser(prog="Wolf and sheep simulation",
                                     description="The program preforms a simple simulation that consists of rounds "
                                                 "where in the first phase of the each round "
                                                 "all the sheep move in one of four random directions "
                                                 "and in the second phase the wolf makes it's move to the closest one "
                                                 "trying to eliminate all sheep.",
                                     formatter_class=RawTextHelpFormatter,
                                     exit_on_error=False)

arg_parser.add_argument('-c', '--config',
                        metavar='FILE',
                        help="takes path to an ini file containing the configuration for the simulation",
                        type=str)
arg_parser.add_argument('-l', '--log',
                        help="takes int value standing for that level of logging",
                        metavar='LEVEL',
                        type=int,
                        choices=[10, 20, 30, 40, 50],
                        default=0)
arg_parser.add_argument('-r', '--rounds',
                        metavar='NUM',
                        help="takes int value standing for amount rounds that the simulation "
                             "will perform before ending",
                        type=int,
                        default=50)
arg_parser.add_argument('-s', '--sheep',
                        metavar='NUM',
                        help="takes int value standing for amount of sheep that will be generated in the simulation",
                        type=int,
                        default=15)
arg_parser.add_argument('-w', '--wait',
                        help="after each round program will wait for ant user input",
                        action='store_true')

# parsing arguments given in the command line execution
args = arg_parser.parse_args()

if not args.log == 0:
    logger.overwrite_log(args.log)

logger.log_to_log("args parsed %s" % args, 10)

wolf_move_dst = 1.0
sheep_move_dst = 0.5
spawn_border = 10

# checking --config argument and validating arguments passed in given file
if args.config is not None:
    # checking if the give path exists, leads to a file and if it does it is in ini format
    if not Path.exists(Path(args.config)):
        logger.log_to_log("ending program: %s does not exist" % args.config, 40)
        arg_parser.error("The file %s does not exist!" % args.config)
    if not Path.is_file(Path(args.config)):
        logger.log_to_log("ending program: %s Did not lead to a file" % args.config, 40)
        arg_parser.error("Given string %s does not lead to a file!" % args.config)
    if not args.config.endswith('.ini'):
        logger.log_to_log("ending program: %s is not an ini file" % args.config, 40)
        arg_parser.error("The file %s is not an ini file!" % args.config)

    # parsing configuration of file given in --config option
    conf_parser = configparser.ConfigParser()
    conf_parser.read(args.config)

    # checking if wolf moving distance exists in given file, and if it is a positive float
    if conf_parser.has_option('Wolf', 'MoveDist'):
        try:
            wolf_move_dst = conf_parser['Wolf'].getfloat('MoveDist')
            logger.log_to_log("wolf moving distance loaded from %s: %f" % (args.config, wolf_move_dst), 10)
        except:
            logger.log_to_log("ending program: %s was not a float" % wolf_move_dst, 40)
            raise TypeError("value at [Wolf].MoveDist was not a float")
        if not wolf_move_dst > 0:
            logger.log_to_log("ending program: %s was not positive" % wolf_move_dst, 40)
            raise ValueError("float at [Wolf].MoveDist must be positive")
    else:
        raise configparser.NoOptionError('MoveDist', 'Wolf')

    # checking if sheep initial spawn position limit exists in given file, and if it is a positive float

    if conf_parser.has_option('Sheep', 'InitPosLimit'):
        try:
            spawn_border = conf_parser['Sheep'].getfloat('InitPosLimit')
            logger.log_to_log("initial position limit loaded from %s: %s" % (args.config, spawn_border), 10)
        except:
            logger.log_to_log("ending program: %s was not a float" % spawn_border, 40)
            raise TypeError("value at [Sheep].InitPosLimit was not a float")
        if not spawn_border > 0:
            logger.log_to_log("ending program: %s was not positive" % spawn_border, 40)
            raise ValueError("float at [Sheep].InitPosLimit must be positive")
    else:
        raise configparser.NoOptionError('InitPosLimit', 'Sheep')

    # checking if sheep moving distance exists in given file, and if it is a positive float
    if conf_parser.has_option('Sheep', 'MoveDist'):
        try:
            sheep_move_dst = conf_parser['Sheep'].getfloat('MoveDist')
            logger.log_to_log("sheep moving distance loaded from %s: %s" % (args.config, sheep_move_dst), 10)
        except:
            logger.log_to_log("ending program: %s was not a float" % sheep_move_dst, 40)
            raise TypeError("value at [Sheep].MoveDist was not a float")
        if not sheep_move_dst > 0:
            logger.log_to_log("ending program: %s was not positive" % sheep_move_dst, 40)
            raise ValueError("float at [Sheep].MoveDist must be positive")
    else:
        raise configparser.NoOptionError('MoveDist', 'Sheep')

# --rounds argument check
if args.rounds < 1:
    logger.log_to_log("ending program: %s was lower than one" % args.rounds, 40)
    arg_parser.error("Amount of rounds must be a positive integer")
# --sheep argument check
if args.sheep < 1:
    logger.log_to_log("ending program: %s was lower than one" % args.sheep, 40)
    arg_parser.error("Amount of sheep must be a positive integer")

simulation = simulation.Simulation(wolf_move_dst, spawn_border, sheep_move_dst, args.sheep, args.wait)

simulation.perform_simulation(args.rounds)
