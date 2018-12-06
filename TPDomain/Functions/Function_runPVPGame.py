#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Function: Run PVP Game


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Changelog:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    This defines the main game loop called in the GameShell.py file.
"""

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
from Classes.Class_PlayerSpawner import PlayerSpawner
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

# A small internal helper function to simplify adding multiple randomly
#placed item spawners.
def addRandomSpawners(min, max, xRange, yRange, w, h, timer, items = None):
    spawners = []
    for i in range(randint(min, max)):
        spawners += [ItemSpawner(randint(xRange[0], xRange[1]),
                                 randint(yRange[0], yRange[1]),
                                 w, h, timer, items)]
    return spawners

def runPVPGame(screen, length):

    # Control game and initialize
    done = False


    # Define a controller and a player state
    contManager = PlayerInputManager()

    # Create empty collectibles list
    collectibles = []

    # Create empty projectiles list
    projectiles = []

    # Initialize the keyboard and mouse player
    players = [Player("KEYBOARD", pygame.joystick.get_count() + 1,
               200, 200, 400, 2, pi, 0, (randint(100, 255),
                                         randint(100, 255),
                                         randint(100, 255)))]

    # Initializes even if no joystick. only adds joystick if controllers
    #are available.
    if pygame.joystick.get_count() > 0:
        for i in range(pygame.joystick.get_count(), 0, -1):
            players = [Player("GAMEPAD", i, 10, 200,
                              400, 2, pi, 0, (randint(100, 255),
                                              randint(100, 255),
                                              randint(100, 255)))] + players
            contManager.addConts(i)
            contManager.startCont(i)

    # Creates map boundaries to prevent players from leaving map
    scenery = [PyGameObj(Polygon([(0, 100), (600, 125), (1200, 100)])),
               PyGameObj(Polygon([(1200, 100), (1194, 450), (1200, 800)])),
               PyGameObj(Polygon([(1200, 800), (600, 794), (0, 800)])),
               PyGameObj(Polygon([(0, 800), (6, 450), (0, 100)]))]

    # Generates player spawners for each player
    for player in players:
        scenery += [PlayerSpawner([randint(100, 1100), randint(200, 700)],
                                  player)]

    # Generate item spawners before scenery so that nothing spawns inside of
    #scenery. The random scenery generator will need to consider these. We add
    #the length of scenery on the random generation call so that we don't
    #consider the pre-formed and special scenery objects when we generate.
    #Additionally, we call addRandomSpawner to get a few random spawners.
    scenery += addRandomSpawners(4, 6, (20, 1180), (120, 780), 30, 30, 5000)
    scenery += addRandomSpawners(2, 4, (20, 1180), (120, 780), 30, 30, 9000,
                                 ["Stynger"])
    scenery += addRandomSpawners(3, 5, (20, 1180), (120, 780), 30, 30, 9000,
                                 ["Rhyno"])
    scenery += addRandomSpawners(0, 2, (20, 1180), (120, 780), 30, 30, 9000,
                                 ["Valhalla"])
    scenery += randomSceneryGen((1200, 800),
                                randint(15, 30) + len(scenery), scenery)

    # Initialize GUI boxes
    gui = []
    for player in players:

        # Create a Player info box and point it to a player
        gui += [GUIBoxPlayerInfo(player)]

    # Game loop, only terminates when time runs out or player escapes.
    timeDisp = TextObj(20, 535, 105)
    resetLength = length
    while not done and length:

        pygame.event.pump()
        length -= 1
        if pygame.key.get_pressed()[pygame.K_r]:
            length = resetLength

                    #==========================================#
                #~~~~~~~~~~~~]      Control Phase      [~~~~~~~~~~~~#
                    #==========================================#

        # 'Controller' in MVC terms
        if playerControlPortion(contManager, players, collectibles,
                                projectiles, scenery):
            return True

                    #==========================================#
                #~~~~~~~~~~~~]      Display Phase      [~~~~~~~~~~~~#
                    #==========================================#

        # 'View' in MVC terms
        displayPortion(screen, gui, players, collectibles, projectiles, scenery,
                       timeDisp, length)
