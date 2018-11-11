#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Class: ControllerManager
# 11/10/2018

# Version 0.2
# 11/11/2018
#   o Added numerous methods to the controller manager class.

# Planned features / updates:
#   o Add listeners and event handlers for different controllers.
#   o Optimize methods
#       - Subdescription

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import pygame.joystick

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]         Helpers         [~~~~~~~~~~~~#
                #==========================================#

                #==========================================#
            #~~~~~~~~~~~~]        Class Def        [~~~~~~~~~~~~#
                #==========================================#

class ControllerManager():

    def __init__(self, maxContArg):
        self.maxCont = maxContArg
        self.conts = {}
        pygame.joystick.init()
        self.validConts = [pygame.joystick.Joystick(x)
                             for x in range(pygame.joystick.get_count())]



# Adds a given controller from the system's controllers to the dictionary
#of viable controllers.
    def addConts(self, playNum):
        if playNum <= pygame.joystick.get_count():

            if playNum <= len(self.validConts) \
               and playNum not in self.conts.keys():

                    self.conts[playNum] = self.validConts[playNum - 1]



# Removes the indicated controller from the dictionary of controllers.
    def removeCont(self, playNum):

        if playNum in self.conts.keys():
            self.conts[playNum].quit()
            del self.conts[playNum]
            print("Player %d may now remove the controller" % playNum)

        elif not len(self.conts):
            print("There are no controllers plugged in!")

        else:
            print("Player %d does not exist!" % playNum)



# Prints the name of a given controller for debugging.
    def getCont(self, playNum):

        if playNum in self.conts.keys():
            print(self.conts[playNum].get_name())

        else:
            print("Player " + str(playNum) + " does not exist!")



# Method to activate a given controller.
    def startCont(self, playNum):

        if not self.isInit(playNum):
            self.conts[playNum].init()



# Method to see if an indicated controller is active.
    def isInit(self, playNum):

        if playNum in self.conts.keys():
            return bool(self.conts[playNum].get_init())
