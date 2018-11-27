#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Function: displayPortion
# Created 11/13/2018

# Version 0.2

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Changelog:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Updated to v0.2 on 11/17/2018
# Changes:
#   o Added new text to display


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import pygame
from Classes.Package_Geometry import Polygon

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function Def:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255, 255,   0)

def displayPortion(screen, text, players, collectibles, projectiles):
    screen.fill(WHITE)
    for collectible in collectibles:

        collectible.draw(screen)

    text.reset()

    for player in players:

        player.draw(screen)
        player._debug_lookDirCheck(screen)

        text.printS(screen,
                    "Player{:d} x:{:>6.2f}".format(player.pNum,
                                                   player.shape.c[0]))

        text.printS(screen,
                    "Player{:d} y:{:>6.2f}".format(player.pNum,
                                                   player.shape.c[1]))

        text.printS(screen,
                    "Player{:d} Item {:d}:{}".format(player.pNum, player.curItem,
                    player.inv[player.curItem].name),
                    color = player.inv[player.curItem].color)
        text.printS(screen, "")

    for projectile in projectiles:
        projectile.draw(screen)

    pygame.display.flip()
