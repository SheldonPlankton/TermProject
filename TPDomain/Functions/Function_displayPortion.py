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

    for collectible in collectibles:
        collectible.draw(screen)


    for projectile in projectiles:
        projectile.draw(screen)

    for obst in scenery:
        if hasattr(obst, "draw"): obst.draw(screen)

    for player in players:
        player.draw(screen)

    pygame.draw.rect(screen, (150, 150, 150), pygame.Rect(0, 0, 1200, 100))
    for box in gui:
        box.draw(screen)

    pygame.draw.rect(screen, (120, 120, 120), pygame.Rect(530, 100, 120, 20))
    time.printS(screen, 'Time left:' + str(length // 600) + ':' +
                ("0" if len(str(length // 10 % 60)) < 2 else "") +
                str(length // 10 % 60))
    pygame.display.flip()
