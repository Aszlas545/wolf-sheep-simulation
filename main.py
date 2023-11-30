import simulation
from pathlib import Path
import animate
import utils
import argparse
from argparse import RawTextHelpFormatter
import configparser

arg_parser = argparse.ArgumentParser(prog="Wolf and sheep simulation",
                                     description=utils.description,
                                     formatter_class=RawTextHelpFormatter,
                                     exit_on_error=False)

arg_parser.add_argument('-c', '--config',
                        help="Takes path to an ini file containing the configuration for the simulation.",
                        type=str)
arg_parser.add_argument('-l', '--log',
                        help="Takes int value standing for that level of logging.",
                        type=int,
                        choices=[10, 20, 30, 40, 50],
                        default=0)
arg_parser.add_argument('-r', '--rounds',
                        help="Takes int value standing for amount rounds that the simulation will perform before ending.",
                        type=int,
                        default=50)
arg_parser.add_argument('-s', '--sheep',
                        help="Takes int value standing for amount of sheep that will be generated in the simulation.",
                        type=int,
                        default=15)
arg_parser.add_argument('-w', '--wait',
                        help="If supplied after each round of simulation the program will wait\n"
                             "for any keyboard input from the user before the next round is preformed.",
                        action='store_true')

args = arg_parser.parse_args()

config_file = args.config
log_level = args.log
rounds_amt = args.rounds
sheep_amt = args.sheep
do_wait = args.wait

if not Path.exists(config_file):
    arg_parser.error("The file %s does not exist!" % config_file)
if not Path.is_file(config_file):
    arg_parser.error("Given string %s does not lead to a file!" % config_file)
if not config_file.endswith('.ini'):
    arg_parser.error("The file %s is not an ini file!" % config_file)

# conf_parser = configparser.ConfigParser()
# conf_parser.read(config_file)
#
# wolf_move_dst = conf_parser['Wolf'].getfloat('MoveDist')
# sheep_move_dst = conf_parser['Sheep'].getfloat('MoveDist')
# spawn_border = conf_parser['Sheep'].getfloat('InitPosLimit')
# print(config_file, log_level, rounds_amt, sheep_amt, do_wait)
# print(wolf_move_dst, sheep_move_dst, spawn_border)

simulation = simulation.Simulation()
animate.animate(simulation, 50)
# for i in range(100):
#     simulation.simulate_round()
