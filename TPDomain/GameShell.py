#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Experiment 4: Game Shell
# Created 11/11/2018

# Version 0.4

# Planned features / updates:
#   o Make it possible to obtain items.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Changelog:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Updated to v0.4 on 11/17/2018
# Changes:
# o Reshuffled code in accordance with changes to structure of classes

# Updated to v0.3 on 11/17/2018
# Changes:
# o Modified intialiazations to reflect restructuring of player

# Updated to v0.3 on 11/14/2018
# Changes:
# o Segregated the actual player logic and draw step into a function
#       exterior to this file

# Updated to v0.2 on 11/12/2018
# Changes:
# o Added functioning player representation to game that reads controller input

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]        Functions        [~~~~~~~~~~~~#
                #==========================================#

from Functions.Function_runPVPGame import runPVPGame

                #==========================================#
            #~~~~~~~~~~~~]         Modules         [~~~~~~~~~~~~#
                #==========================================#

import pygame
from math import inf

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Game Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pygame.init()
screen = pygame.display.set_mode([1200, 800])
pygame.display.set_caption("Term Project")
done = False
while not done:

    if runPVPGame(screen, inf):
        done = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
