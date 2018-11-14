#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Function: Control Portion
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
import pygame

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function Def:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]         Helpers         [~~~~~~~~~~~~#
                #==========================================#

def playerControlPortion(contManager, players):

    for player in players:
        if player.control == "GAMEPAD":
            if sqrt(contManager.getAxis(player.pNum, 1)**2 +
                    contManager.getAxis(player.pNum, 0)**2) > .1:

                player.move(atan2(contManager.getAxis(player.pNum, 1),
                              contManager.getAxis(player.pNum, 0)))

            player.look(atan2(contManager.getAxis(player.pNum, 3),
                          contManager.getAxis(player.pNum, 4)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

    # Testing exit via button command
    if contManager.getButton(1, 2):
        print("Exiting")
        return True
