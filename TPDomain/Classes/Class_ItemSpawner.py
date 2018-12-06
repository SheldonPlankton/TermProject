#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Class: Item Spawner

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Description
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    This is an object that preloads a dictionary of JSON data, and then calls
the createWeaponFromData function in order to make templating easier. It has
collision but no draw function. Basically, it defines an invisible region in
which to spawn items in the game. It is programmed with collision so that the
spawning regions will be seen by the random scenery generator.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from Functions.Function_utilitiesJSON import *
from Classes.Class_PyGameObj import PyGameObj
from Classes.Package_Geometry import Polygon
from Classes.Class_Collectible import Collectible
from Classes.Items.Item_Heal import HealItem
from Classes.Items import *
from random import randint, choice

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Define the item spawner class
class ItemSpawner:
    def __init__(self, xArg, yArg, wArg, hArg, spawnTimeArg, itemsArg = None):
        self.x = xArg # Left x anchor
        self.y = yArg # Top y anchor
        self.w = wArg # width of spawning zone
        self.h = hArg # height of spawning zone

        # Only preload if this will be a weapon spawner. If not, it will
        #default to spawning potions
        self.items = preloadList(itemsArg) if itemsArg != None else None

        # the current time in the spawner's clock. It is set this way so
        #that the spawner generates on the first tick of the game.
        self.spawnClock = spawnTimeArg - 1
        self.spawnTime = spawnTimeArg

        # Defines the hidden shape of the spawning region.
        self.shape = Polygon([(self.x, self.y),
                              (self.x, self.y + self.h),
                              (self.x + self.w, self.y + self.h),
                              (self.x + self.w, self.y)])

    # Uses its shape's collision
    def collision(self, other):
        return self.shape.collision(other)

    # Spawn an item at a random position within its bounds
    def spawn(self, collectibles):
        self.spawnClock += 1
        if self.spawnClock == self.spawnTime:
            self.spawnClock = 0

            # Spawn a weapon if this object preloaded.
            if self.items != None:
                collectibles += [Collectible(randint(self.x, self.x + self.w),
                                         randint(self.y, self.y + self.h), 10,
                                         createWepFromData(self.items,
                                         choice(list(self.items.keys()))))]

            # Otherwise spawn a potion
            else:
                collectbles += [Collectible(randint(0, 800),
                                             randint(100, 800), 10,
                                             HealItem("Potion", 4, 50, 50,
                                             (0, 255, 240), 'Potion'))]
