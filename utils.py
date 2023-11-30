c_help = ("Takes path to a INI file containing the configuration for the simulation including:\n"
          "-speed of sheep\n"
          "-maximum distance from center point (0, 0) at which sheep can be spawned\n"
          "-speed of wolf\n"
          "The file should be formatted in particular way:\n"
          "\n[Sheep]\n"
          "InitPosLimit = 10.0\n"
          "MoveDist = 0.5\n"
          "\n[Wolf]\n"
          "MoveDist = 1.0\n"
          "\nIf the argument is not supplied the configuration will be as in the example above.")

l_help = ("Takes INT value standing for that level of logging that the user wants to receive"
          "possible levels of logging are:\n"
          "DEBUG (10) - provides detailed information intended for a developer typically to help diagnose a problem\n"
          "INFO (20) - provides general information about the progress of program execution\n"
          "WARNING (30) - indicates that something unexpected happened, yet the program is working as expected\n"
          "ERROR (40) - indicates that a problem occurred and the program may not be able to perform some of its" 
          "functions\n"
          "CRITICAL (50) - indicates that a serious problem occurred and the program may not be able to continue" 
          "running\n"
          "If the argument is supplied all information of given or higher level will be logged to chase.log file.\n"
          "If the the argument is not supplied the file will not be created and no information will be logged.")

r_help = ("Takes INT value standing for amount rounds that the simulation will perform before ending.\n"
          "If the argument is not supplied the default value will be taken which is 50")

s_help = ("Takes INT value standing for amount of sheep that will be generated in the simulation.\n"
          "If the argument is not supplied the default value will be taken which is 15")

w_help = ("If supplied after each round of simulation the program will wait\n"
          "for any keyboard input from the user before the next round is preformed.\n"
          "If the argument is not supplied the simulation will be performed without any pauses.")

description = ("The program performs a simulation of wolf trying to catch sheep randomly"
               "spawned within starting borders. The map of simulation is not" 
               "limited with such borders itself. In the first part of the simulation" 
               "all sheep make a move in random direction. In the second part the wolf"
               "makes it's move to the closest sheep and if he manages to reach her the"
               "sheep is eliminated")
