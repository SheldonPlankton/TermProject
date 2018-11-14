#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Experiment 4: Game Shell
# Created 11/11/2018

# Version 0.2
# Updated 11/12/2018
# Changes:
# o Added functioning player representation to game that reads controller input

# Planned features / updates:
#   o Make it possible to obtain items.
#       - Subdescription

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]        Classes         [~~~~~~~~~~~~#
                #==========================================#

from Class_TextPrint import TextPrint
from Class_PlayerInputManager import PlayerInputManager
from Class_Player import Player

                #==========================================#
            #~~~~~~~~~~~~]        Functions        [~~~~~~~~~~~~#
                #==========================================#

from Function_playerControlPortion import playerControlPortion
from Function_displayPortion import displayPortion

                #==========================================#
            #~~~~~~~~~~~~]         Modules         [~~~~~~~~~~~~#
                #==========================================#

import pygame
from math import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Game Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Define some colors

# Control game and initialize
done = False
pygame.init()

# Define a controller and a player state
contManager = PlayerInputManager(1)
players = [Player("GAMEPAD", 1, 0, 0, .1, pi, 0, 10, 10),
           Player("KEYBOARD", 1, 20, 20, .1, pi, 0, 10, 10)]

# Defines a screen to print player data
text = TextPrint()
screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption("My Game")

contManager.addConts(1)
contManager.startCont(1)



while not done:

                #==========================================#
            #~~~~~~~~~~~~]      Control Phase      [~~~~~~~~~~~~#
                #==========================================#

    done = playerControlPortion(contManager, players)

                #==========================================#
            #~~~~~~~~~~~~]      Display Phase      [~~~~~~~~~~~~#
                #==========================================#

    displayPortion(screen, text, players)

pygame.quit()
