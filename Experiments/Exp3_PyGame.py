#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Experiment 3: PyGame events
# 11/10/2018

# Version 0.1
# No updates yet...
# No changes to report!

# Planned features / updates:
#   o Main feature description
#       - Subdescription

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import pygame.joystick

                #==========================================#
            #~~~~~~~~~~~~]        Versions        [~~~~~~~~~~~~#
                #==========================================#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]         Helpers         [~~~~~~~~~~~~#
                #==========================================#

                #==========================================#
            #~~~~~~~~~~~~]        Subheader        [~~~~~~~~~~~~#
                #==========================================#

class ControllerManager():

    def __init__(self, maxContArg):
        self.maxCont = maxContArg
        self.conts = {}
        pygame.joystick.init()
        self.validConts = [pygame.joystick.Joystick(x)
                             for x in range(pygame.joystick.get_count())]


    def addConts(self, playNum):
        if playNum <= pygame.joystick.get_count():

            if playNum <= len(self.validConts) \
               and playNum not in self.conts.keys():

                    self.conts[playNum] = self.validConts[playNum - 1]




    def removeCont(self, playNum):

        if playNum in self.conts.keys():
            self.conts[playNum].quit()
            del self.conts[playNum]
            del self.validConts[playNum-1]
            print("Player %d may now remove the controller" % playNum)

        elif not len(self.conts):
            print("There are no controllers plugged in!")

        else:
            print("Player %d does not exist!" % playNum)




    def getCont(self, playNum):

        if playNum in self.conts.keys():
            print(self.conts[playNum].get_name())

        else:
            print("Player " + str(playNum) + " does not exist!")

    def startCont(self, playNum):

        if not self.isInit(playNum):
            self.conts[playNum].init()

    def isInit(self, playNum):

        if playNum in self.conts.keys():
            return bool(self.conts[playNum].get_init())


manager = ControllerManager(3)
manager.addConts(1)
manager.getCont(1)
#manager.startCont(1)
print(manager.isInit(1))

manager.removeCont(1)
manager.getCont(1)
