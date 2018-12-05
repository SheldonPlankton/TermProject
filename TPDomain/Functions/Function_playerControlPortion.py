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

def playerControlPortion(contManager, players, collectibles, projectiles,
                         scenery):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

    # Player control loop
    for player in players:
        player.move(contManager)
        player.look(contManager)
        player.collect(contManager, collectibles)
        player.swap(contManager)
        player.useItem(contManager, players, projectiles)
        for obst in scenery:
            player.collision(obst.shape)
        player.update()

        if player.pNum < pygame.joystick.get_count():
            if contManager.getButton(player.pNum, 7):
                print("Exiting")
                return True
        else:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                return True

    for i in range(len(projectiles) - 1, -1, -1):
        if projectiles[i].update(projectiles, scenery, players):
            del projectiles[i]

    # Testing exit via button command
