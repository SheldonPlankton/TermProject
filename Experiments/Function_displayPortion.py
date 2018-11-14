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

import pygame

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function Def:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

def displayPortion(screen, text, players, **objs):
    screen.fill(WHITE)

    for player in players:
        player.draw(screen)
        player._debug_lookDirCheck(screen)

    text.reset()
    text.printS(screen, "Player x:{:>6.2f}".format(player.x))
    text.printS(screen, "Player y:{:>6.2f}".format(player.y))

    pygame.display.flip()
