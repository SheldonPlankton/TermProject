#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Class: Player
# Created 11/10/2018

# Version 0.1
# 11/12/2018
#   o Added numerous methods to the controller manager class.

# Planned features / updates:

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
from Class_Entity import Entity

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

    def look(self, lookDir = None):
        self.lookDir = self.dir if lookDir == None else lookDir

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
