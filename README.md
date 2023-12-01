# Wolf and sheep simulation
## This program performs a simple simulation of wolf chasing sheep around the map not limited by boundaries.
The simulation consists of rounds divided into two phases:
- In the first phase sheep move in one of four directions (up, down, left right) chosen randomly
- In the second phase wolf chooses his target by searching for the closes sheep. If the chosen target is within the wolf's range the sheep is eaten otherwise the wolf closes the distance between him and the target by set distance.

The program takes command lines argument allowing user to set amount of sheep and round, distance that each animal in the simulation can move set in .ini file, whether the simulation should be logged to a logs.log file, and whether the simulation should wait before each round is performed for user input
