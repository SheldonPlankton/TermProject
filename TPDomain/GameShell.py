#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Experiment 4: Game Shell
# Created 11/11/2018

# Version 0.3

# Planned features / updates:
#   o Make it possible to obtain items.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Changelog:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
            #~~~~~~~~~~~~]        Classes         [~~~~~~~~~~~~#
                #==========================================#

from Classes.Class_TextPrint import TextPrint
from Classes.Class_PlayerInputManager import PlayerInputManager
from Classes.Class_Player import Player
from Classes.Class_Collectible import Collectible

                #==========================================#
            #~~~~~~~~~~~~]        Functions        [~~~~~~~~~~~~#
                #==========================================#

from Functions.Function_playerControlPortion import playerControlPortion
from Functions.Function_displayPortion import displayPortion

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
contManager = PlayerInputManager()
players = [Player("GAMEPAD", 1, 0, 0, 15, .5, pi, 0, 10, 10),
           Player("KEYBOARD", 2, 20, 20, 40, .5, pi, 0, 10, 10)]
collectibles = [Collectible(10 * i * 2, 10 * i, 10, "Banana") for i in range(20)]

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
    print(players[0].equips["Tool"], players[1].equips["Tool"])
    done = playerControlPortion(contManager, players, collectibles)

                #==========================================#
            #~~~~~~~~~~~~]      Display Phase      [~~~~~~~~~~~~#
                #==========================================#

    displayPortion(screen, text, players, collectibles)

pygame.quit()
