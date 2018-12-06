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

# Planned features / updates:
#   o Main feature description
#       - Subdescription

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Changelog:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# No changes yet!

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]        Classes        [~~~~~~~~~~~~#
                #==========================================#

from Classes.Class_TextObj import TextObj
from Classes.Class_PlayerInputManager import PlayerInputManager
from Classes.Class_Player import Player
from Classes.Class_Collectible import Collectible
from Classes.Class_Item import Item
from Classes.Class_PyGameObj import PyGameObj
from Classes.Items.Item_Wep import BaseWeapon
from Classes.Items.Item_Heal import HealItem
from Classes.Class_GUIBoxPlayerInfo import GUIBoxPlayerInfo
from Classes.Class_ItemSpawner import ItemSpawner
from Classes.Package_Geometry import *

                #==========================================#
            #~~~~~~~~~~~~]        Functions        [~~~~~~~~~~~~#
                #==========================================#

from Functions.Function_playerControlPortion import playerControlPortion
from Functions.Function_displayPortion import displayPortion
from Functions.Function_randomScenery import randomSceneryGen

                #==========================================#
            #~~~~~~~~~~~~]        Modules         [~~~~~~~~~~~~#
                #==========================================#

from math import *
from random import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def runPVPGame(screen, length):

    # Control game and initialize
    done = False


    # Define a controller and a player state
    contManager = PlayerInputManager()
    """
    collectibles = [Collectible(randint(0, 10 * i * 5),
                                randint(0, 10 * i + 200), 10,
                                BaseWeapon("Item" + str(i), 200, 20, 6, 1000, 20,
                                5, (randint(0,255), randint(0,255), randint(0,255)),
                                (120, 0, 240), 'Test')) \
                                for i in range(20)]
    """
    collectibles = [Collectible(randint(0, 800),
                                 randint(100, 800), 10,
                                 HealItem("Potion", 4, 50, 50,
                                 (0, 255, 240), 'Potion'))]

    projectiles = []
    # Defines a screen to print player data



    players = [Player("KEYBOARD", pygame.joystick.get_count() + 1,
               200, 200, 400, 2, pi, 0, 10, 10)]

    # Initializes even if no joystick (only adds joystick if controller plugged in)
    if pygame.joystick.get_count() > 0:
        for i in range(pygame.joystick.get_count(), 0, -1):
            players = [Player("GAMEPAD", i, 10, 200,
                              400, 2, pi, 0, 10, 10)] + players
            contManager.addConts(i)
            contManager.startCont(i)

    scenery = [PyGameObj(Polygon([(0, 100), (600, 106), (1200, 100)])),
               PyGameObj(Polygon([(1200, 100), (1194, 450), (1200, 800)])),
               PyGameObj(Polygon([(1200, 800), (600, 794), (0, 800)])),
               PyGameObj(Polygon([(0, 800), (6, 450), (0, 100)]))]

    scenery += [ItemSpawner(50, 100, 200, 200, ['Stynger'])]
    scenery += randomSceneryGen((1200, 800), 30, scenery)

    gui = []
    for player in players:
        gui += [GUIBoxPlayerInfo(player)]

    while not done and length:
        pygame.event.pump()
        length -= 1



                    #==========================================#
                #~~~~~~~~~~~~]      Control Phase      [~~~~~~~~~~~~#
                    #==========================================#

        if playerControlPortion(contManager, players, collectibles,
                                projectiles, scenery):
            return True

                    #==========================================#
                #~~~~~~~~~~~~]      Display Phase      [~~~~~~~~~~~~#
                    #==========================================#

        displayPortion(screen, gui, players, collectibles, projectiles, scenery)
