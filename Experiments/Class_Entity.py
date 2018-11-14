#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# "Project Name"
# Created

# Version #
# Updated "Date"
# Changes:
# o Change

# Planned features / updates:
#   o Main feature description
#       - Subdescription

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from math import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Class Def:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Entity():

    #DocString:

    """A base class for a player object in the game"""

                #==========================================#
            #~~~~~~~~~~~~]       Metafuncts       [~~~~~~~~~~~~#
                #==========================================#

    def __init__(self, xArg, yArg, spdArg, dirArg):
        self.x = xArg
        self.y = yArg
        self.spd = spdArg
        self.dir = dirArg

                #==========================================#
            #~~~~~~~~~~~~]     Control Methods    [~~~~~~~~~~~~#
                #==========================================#

    def move(self, dir = None):
        self.dir = self.dir if dir == None else dir
        self.x += self.spd * cos(self.dir)
        self.y += self.spd * sin(self.dir)
