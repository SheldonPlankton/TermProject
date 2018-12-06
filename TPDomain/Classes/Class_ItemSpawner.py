#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Class: Item Spawner
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

from Functions.Function_utilitiesJSON import *
from Classes.Class_PyGameObj import PyGameObj
from Classes.Package_Geometry import Polygon
from Classes.Class_Collectible import Collectible
from Classes.Items import *
from random import randint, choice
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ItemSpawner:
    def __init__(self, xArg, yArg, wArg, hArg, itemsArg):
        self.x = xArg
        self.y = yArg
        self.w = wArg
        self.h = hArg
        self.items = preloadList(itemsArg)
        self.spawnTimer = 0
        self.shape = Polygon([(self.x, self.y),
                              (self.x, self.y + self.h),
                              (self.x + self.w, self.y + self.h),
                              (self.x + self.w, self.y)])

    def collision(self, other):
        return self.shape.collision(other)

    def spawn(self, collectibles):
        self.spawnTimer += 1
        if self.spawnTimer == 5000:
            self.spawnTimer = 0
            collectibles += [Collectible(randint(self.x, self.x + self.w),
                                         randint(self.y, self.y + self.h), 10,
                                         createWepFromData(self.items,
                                                choice(
                                                    list(
                                                        self.items.keys()
                                                        )
                                                    )
                                                )
                                         )]
