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
from Functions.Function_geometry import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function Def:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   255,   0)

def displayPortion(screen, text, players, collectibles):
    screen.fill(WHITE)
    if colCircCirc(players[0].x, players[0].y, players[0].r,
                   players[1].x, players[1].y, players[1].r):
            screen.fill(RED)
    for collectible in collectibles:

        collectible.draw(screen)

    text.reset()
    for player in players:

        player.draw(screen)
        player._debug_lookDirCheck(screen)

        text.printS(screen,
                    "Player{:d} x:{:>6.2f}".format(player.pNum, player.x))

        text.printS(screen,
                    "Player{:d} y:{:>6.2f}".format(player.pNum, player.y))

        text.printS(screen,
                    "Player{:d} Item {:d}:{}".format(player.pNum, player.curItem,
                    player.inv[player.curItem].name),
                    color = player.inv[player.curItem].color)
        text.printS(screen, "")


    pygame.display.flip()
