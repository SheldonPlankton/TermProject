#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Class: Player
# Created 11/10/2018

# Version 0.3

# Planned features / updates:
#   o Generalize draw function

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Changelog:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Updated to v0.3 on 11/14/2018
#   o Internalized all input handling for ease of editing by passing the
#     controller manager into the function.
#   o Modified initialization to determine the controller for a given player.

# Updated to v0.2 on 11/12/2018
#   o Added a debug method.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Overview:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    This class is effectively a representation of a player object in game.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import pygame
from math import *
from Classes.Class_Entity import Entity

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Class Def:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Player(Entity):

    #DocString:

    """A base class for a player object in the game"""

                #==========================================#
            #~~~~~~~~~~~~]       Metafuncts       [~~~~~~~~~~~~#
                #==========================================#

    def __init__(self, controlArg, pNumArg, xArg, yArg, spdArg,
                 dirArg, lookDirArg, dfnArg, atkArg):

        super().__init__(xArg, yArg, spdArg, dirArg)
        self.control = controlArg
        self.pNum = pNumArg
        self.lookDir = lookDirArg
        self.atk = atkArg
        self.dfn = dfnArg
        self.equips = {"Armor" : None, "Tool" : None}

                #==========================================#
            #~~~~~~~~~~~~]     Control Methods    [~~~~~~~~~~~~#
                #==========================================#

    def equip(self, tool):
        self.equips["Tool"] = tool




    def look(self, contManager):
        if self.control == "GAMEPAD":
            self.lookDir = atan2(contManager.getAxis(self.pNum, 3),
                                 contManager.getAxis(self.pNum, 4))

        elif self.control == "KEYBOARD":
            mousePos = contManager.conts[self.pNum].mousePos()
            xDif = mousePos[0] - self.x
            yDif = mousePos[1] - self.y
            self.lookDir = atan2(yDif, xDif)


    def move(self, contManager):
        if self.control == "GAMEPAD":
            if sqrt(contManager.getAxis(self.pNum, 1)**2 +
                    contManager.getAxis(self.pNum, 0)**2) > .1:
                    super().move(atan2(contManager.getAxis(self.pNum, 1),
                                       contManager.getAxis(self.pNum, 0)))

        elif self.control == "KEYBOARD":
            x, y = contManager.conts[self.pNum].dirKeys()
            if not x == y == 0: super().move(atan2(x, y))



    def draw(self, screen):
        pygame.draw.circle(screen, (0, 0, 0), (floor(self.x), floor(self.y)), 10)




    def getStats(self):
        return (self.x, self.y, self.dir, self.lookDir)


                #==========================================#
            #~~~~~~~~~~~~]     Debug Methods      [~~~~~~~~~~~~#
                #==========================================#

    def _debug_lookDirCheck(self, screen):
        pygame.draw.line(screen, (0, 0, 0), (floor(self.x), floor(self.y)),
                         (floor(self.x) + 100 * cos(self.lookDir),
                          floor(self.y) + 100 * sin(self.lookDir)))
