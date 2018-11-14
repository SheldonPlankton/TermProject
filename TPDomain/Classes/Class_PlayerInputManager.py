#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Class: ControllerManager
# Created 11/10/2018

# Version 0.3

# Planned features / updates:
#   o Add listeners and event handlers for different controllers.
#   o Optimize methods
#       - Subdescription

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Changelog:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Updated to v0.3 on 11/14/2018
#   o Added automatic keyboard labelling and use of Class_KeyboardManager.

# Updated to v0.2 on 11/11/2018
#   o Added numerous methods to the controller manager class.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Overview:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    This class is specifically created to ease the coding behind handling
multiple controllers in a multiplayer game environment. It includes methods
for adding and removing controllers from a game and centralizes all of the
controllers.

    I liken it to a central point that bundles and can act on all of the
controllers in the game, like a bin. This does not control anything like
movement, as it is intended exclusively for easier handling of input
information and uses logic to avoid crash errors. Effectively, it
ensures that all attempts to get controller information are valid.

"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import pygame
from Classes.Class_KeyboardManager import KeyboardManager

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Class Def:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class PlayerInputManager():

    #DocString:

    """A class for managing controllers in PyGame"""

                #==========================================#
            #~~~~~~~~~~~~]       Metafuncts       [~~~~~~~~~~~~#
                #==========================================#

    def __init__(self):
        self.maxCont = pygame.joystick.get_count() + 1
        self.conts = {}
        self.conts[self.maxCont] = KeyboardManager
        pygame.joystick.init()
        self.validConts = [pygame.joystick.Joystick(x)
                             for x in range(pygame.joystick.get_count())]


                #==========================================#
            #~~~~~~~~~~~~]      Initializers      [~~~~~~~~~~~~#
                #==========================================#

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



# Method to activate a given controller.
    def startCont(self, playNum):

        if not self.isInit(playNum):
            self.conts[playNum].init()


                #==========================================#
            #~~~~~~~~~~~~]     Gamepad methods    [~~~~~~~~~~~~#
                #==========================================#


# Prints the name of a given controller for debugging.
    def getCont(self, playNum):

        if playNum in self.conts.keys():
            if type(self.conts[playNum]) == pygame.joystick.Joystick:
                print(self.conts[playNum].get_name())

            else:
                print("Player " + str(playNum) + " does not exist!")



# Method to see if an indicated controller is active.
    def isInit(self, playNum):

        if playNum in self.conts.keys():
            return bool(self.conts[playNum].get_init())



# Returns all events associated to the specified controller.
    def getEvents(self, playNum):

        if playNum in self.conts.keys() and self.isInit(playNum):
            for event in pygame.event.get():
                yield event



# Gets information about whether a specific button is pressed.
    def getButton(self, playNum, buttonNum):
        pygame.event.get()

        if playNum in self.conts.keys() and self.isInit(playNum):
            if buttonNum in range(self.conts[playNum].get_numbuttons()):
                return self.conts[playNum].get_button(buttonNum)

            else:
                print("No such button!")

        else:
            print("Not a valid controller!")

# Gets information about the joystick movement is pressed.
    def getAxis(self, playNum, stickNum):
        pygame.event.get()

        if playNum in self.conts.keys() and self.isInit(playNum):
            if stickNum in range(self.conts[playNum].get_numaxes()):
                return self.conts[playNum].get_axis(stickNum)

            else:
                print("No such joystick!")

        else:
            print("Not a valid controller!")
