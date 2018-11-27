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

# Updated to v0.3 on 11/17/2018
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

"""
import module_manager
module_manager.ignore_module(Classes.Class_TextPrint)
module_manager.review()
"""

                #==========================================#
            #~~~~~~~~~~~~]        Classes         [~~~~~~~~~~~~#
                #==========================================#

from Classes.Class_TextPrint import TextPrint
from Classes.Class_PlayerInputManager import PlayerInputManager
from Classes.Class_Player import Player
from Classes.Class_Collectible import Collectible
from Classes.Class_Item import Item
from Classes.Items.Item_Wep import BaseWeapon
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
from random import *
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Game Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Define some colors

# Control game and initialdize
done = False
pygame.init()

# Define a controller and a player state
contManager = PlayerInputManager()

collectibles = [Collectible(10 * i * 5, 10 * i + 200, 10,
                            BaseWeapon("Item" + str(i), 20, 200, .5, 100, 20,
                            (randint(0,255), randint(0,255), randint(0,255)))) \
                            for i in range(20)]

projectiles = []
# Defines a screen to print player data
text = TextPrint()
screen = pygame.display.set_mode([800, 800])
pygame.display.set_caption("My Game")

players = [Player("KEYBOARD", pygame.joystick.get_count() + 1,
           200, 200, 10, .5, pi, 0, 10, 10)]

# Initializes even if no joystick (only adds joystick if controller plugged in)
if pygame.joystick.get_count() > 0:
    players = [Player("GAMEPAD", 1, 0, 200, 10, .5, pi, 0, 10, 10)] + players
    contManager.addConts(1)
    contManager.startCont(1)



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

                #==========================================#
            #~~~~~~~~~~~~]      Control Phase      [~~~~~~~~~~~~#
                #==========================================#

    done = playerControlPortion(contManager, players, collectibles, projectiles)

                #==========================================#
            #~~~~~~~~~~~~]      Display Phase      [~~~~~~~~~~~~#
                #==========================================#

    displayPortion(screen, text, players, collectibles, projectiles)

pygame.quit()
