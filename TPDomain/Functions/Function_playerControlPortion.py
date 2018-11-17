#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Function: Player Control Portion
# Created 11/13/2018

# Version 0.3

# Planned features / updates:
#   o perhaps handle collision management by passing the map state into the
#     function.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Changelog:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Updated to v0.3 on 11/17/2018
# Changes:
#   o Included new player methods

# Updated to v0.2 on 11/14/2018
# Changes:
#   o Moved all of the input handling into the player class definition.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from math import *
import pygame

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function Def:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]         Helpers         [~~~~~~~~~~~~#
                #==========================================#

def playerControlPortion(contManager, players, collectibles):

    for player in players:
        player.move(contManager)
        player.look(contManager)
        player.collect(contManager, collectibles)
        player.swap(contManager)
        player.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

    # Testing exit via button command
    if contManager.getButton(1, 7):
        print("Exiting")
        return True
