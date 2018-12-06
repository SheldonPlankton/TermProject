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

def displayPortion(screen, gui, players, collectibles, projectiles, scenery,
                   time, length):
    screen.fill((255, 255, 150))

    # Draw collectibles
    for collectible in collectibles:
        collectible.draw(screen)

    # Only draw scenery with draw methods
    for obst in scenery:
        if hasattr(obst, "draw"): obst.draw(screen)

    # Draw projectiles
    for projectile in projectiles:
        projectile.draw(screen)

    # Draw the players
    for player in players:
        player.draw(screen)

    # Draw the top bar and each player GUI inventory
    pygame.draw.rect(screen, (150, 150, 150), pygame.Rect(0, 0, 1200, 100))
    for box in gui:
        box.draw(screen)

    # Draw the timer at the top of the screen. Made to look like minutes and
    #seconds but time is not exact.
    pygame.draw.rect(screen, (120, 120, 120), pygame.Rect(530, 100, 120, 20))
    time.printS(screen, 'Time left:' + str(length // 600) + ':' +
                ("0" if len(str(length // 10 % 60)) < 2 else "") +
                str(length // 10 % 60))

    # Take all of the pushed drawing information and actually draw it
    pygame.display.flip()
