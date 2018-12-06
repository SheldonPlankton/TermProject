#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Class: Player
# Created 11/10/2018

# Version 0.5

# Planned features / updates:
#   o Generalize draw function

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Changelog:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Updated to v0.5 on 11/17/2018
#   o Updated player inventory structure, added item switch functionality

# Updated to v0.4 on 11/16/2018
#   o Added method to handle item acquisition.

# Updated to v0.3 on 11/14/2018
#   o Internalized all input handling for ease of editing by passing the
#     controller manager into the function.
#   o Modified initialization to determine the controller for a given player.

# Updated to v0.2 on 11/12/2018
#   o Added a debug method.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Overview:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    This class is effectively a representation of a player object in game.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import pygame
from math import *
from Classes.Class_Entity import Entity
from Classes.Class_Item import Item
from Classes.Class_Collectible import Collectible
from Classes.Package_Geometry import *


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Class Def:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Player(Entity):

    #DocString:

    """A base class for a player object in the game"""

                #==========================================#
            #~~~~~~~~~~~~]       Metafuncts       [~~~~~~~~~~~~#
                #==========================================#

    def __init__(self, controlArg, pNumArg, xArg, yArg, lifeArg,
                 spdArg, dirArg, lookDirArg, dfnArg, atkArg,
                 colorArg = (0,0,0)):

        super().__init__(Circle((xArg, yArg), 10), spdArg, dirArg)
        self.control = controlArg
        self.pNum = pNumArg
        self.lookDir = lookDirArg
        self.life = lifeArg
        self.maxLife = lifeArg
        self.atk = atkArg
        self.dfn = dfnArg
        self.armor = None
        self.inv = {}
        for i in range(1,6): self.inv[i] = Item(None, 0, 0)
        self.curItem = 1
        self.colCool = 0
        self.swapCool = 0
        self.lastHit = None
        self.wins = 0
        self.color = colorArg

    def setSpawn(self, spawner):
        self.spawn = (spawner.c[0], spawner.c[1])
        self.shape.c = list(self.spawn)
                #==========================================#
            #~~~~~~~~~~~~]     Control Methods    [~~~~~~~~~~~~#
                #==========================================#

    def equip(self, item, collectibles):
        if self.inv[self.curItem].name == None:
            self.inv[self.curItem] = item

        else:
            collectibles += [Collectible(self.shape.c[0], self.shape.c[1], 10,
                                         self.inv[self.curItem])]
            self.inv[self.curItem] = item



    def swap(self, contManager):
        pygame.event.get()
        if not self.swapCool:

            if self.control == "GAMEPAD":
                if contManager.getButton(self.pNum, 5):
                    self.curItem = (self.curItem % 5) + 1
                    self.swapCool = 50

            elif self.control == "KEYBOARD":
                if contManager.conts[self.pNum].mouseClick()[2]:
                    self.curItem = (self.curItem % 5) + 1
                    self.swapCool = 50



    def look(self, contManager):
        if self.control == "GAMEPAD":
            self.lookDir = atan2(contManager.getAxis(self.pNum, 3),
                                 contManager.getAxis(self.pNum, 4))



        elif self.control == "KEYBOARD":
            mousePos = contManager.conts[self.pNum].mousePos()
            xDif = mousePos[0] - self.shape.c[0]
            yDif = mousePos[1] - self.shape.c[1]
            self.lookDir = atan2(yDif, xDif)



# Handles player movement changes.
    def move(self, contManager):
        if self.control == "GAMEPAD":
            if sqrt(contManager.getAxis(self.pNum, 1)**2 +
                    contManager.getAxis(self.pNum, 0)**2) > .1:
                    super().move(atan2(contManager.getAxis(self.pNum, 1),
                                       contManager.getAxis(self.pNum, 0)))

        elif self.control == "KEYBOARD":
            x, y = contManager.conts[self.pNum].dirKeys()
            if not x == y == 0: super().move(atan2(x, y))




    def collect(self, contManager, collectibles):
        pygame.event.get()

        # Inner function for looping over collectibles
        def collectLoop(self, collectibles):
            for i in range(len(collectibles) - 1, -1, -1):
                if collectibles[i].collision(self.shape):
                    self.equip(collectibles[i].item, collectibles)
                    del collectibles[i]
                    self.colCool = 120
                    break

        if not self.colCool:
            if self.control == "GAMEPAD":
                if contManager.getButton(self.pNum, 2):
                    collectLoop(self, collectibles)


            elif self.control == "KEYBOARD":
                if contManager.conts[self.pNum].mouseClick()[1]:
                    collectLoop(self, collectibles)



    def collision(self, otherShape):
        collides = generalCollider(self.shape, otherShape, True)
        if collides[0]:
            self.shape.c[0] += collides[1][0]
            self.shape.c[1] += collides[1][1]

    def useItem(self, contManager, players, projectiles):

        def innerUseFunct(self, players, projectiles):
            if self.inv[self.curItem].use(self, players, projectiles):
                self.inv[self.curItem] = Item(None, 0, 0)

        if self.control == "GAMEPAD":
            if contManager.getButton(self.pNum, 4):
                innerUseFunct(self, players, projectiles)

        elif self.control == "KEYBOARD":
            if contManager.conts[self.pNum].mouseClick()[0]:
                innerUseFunct(self, players, projectiles)

    def heal(self, healAmount):
        self.life += healAmount if healAmount <= self.maxLife - self.life \
                     else max(self.maxLife - self.life, 0)

# Called in the update method if the player has died
    def death(self):
        self.shape.c = list(self.spawn)
        self.life = self.maxLife
        self.colCool = 0
        self.swapCool = 0
        self.curItem = 1
        for i in range(1,6): self.inv[i] = Item(None, 0, 0)
        self.lastHit.wins += 1

# Updates time based variables
    def update(self):
        if self.life <= 0:
            self.death()

        if self.colCool > 0:
            self.colCool -= 1

        if self.swapCool > 0:
            self.swapCool -= 1

        for item in self.inv:
            if self.inv[item].coolCurrent > 0:
                self.inv[item].coolCurrent -= 1



                #==========================================#
            #~~~~~~~~~~~~]       Draw Methods     [~~~~~~~~~~~~#
                #==========================================#

    def draw(self, screen):
        self.shape.draw(screen, self.color)
