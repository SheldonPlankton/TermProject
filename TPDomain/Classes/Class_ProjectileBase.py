#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Class: Projectile Base
# Created 11/15/2018

# Version 0.2

# Planned features / updates:
#   o Main feature description
#       - Subdescription

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Changelog:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Updated to v0.2 on 11/17/2018
# Changes:
#   o Added projectile update method

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from Classes.Class_Entity import Entity
from Classes.Class_PyGameObj import PyGameObj
import pygame

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Class Def:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ProjectileBase(Entity):

    def __init__(self, dirArg, spdArg, lifeArg, dmgArg,
                 shapeArg, colorArg, ownerArg):
        super().__init__(shapeArg, spdArg, dirArg)
        self.life = lifeArg
        self.dmg = dmgArg
        self.color = colorArg
        self.owner = ownerArg

    def draw(self, screen):
        self.shape.draw(screen, self.color)

    def collision(self, otherShape):
        return self.shape.collision(otherShape)

    def update(self, projectiles, scenery, players):
        if 0 > self.shape.c[0] or self.shape.c[0] > 1200: return True
        if 100 > self.shape.c[1] or self.shape.c[1] > 800: return True

        if self.life:
            for player in players:
                if player != self.owner and self.collision(player.shape):
                    player.life -= self.dmg
                    player.lastHit = self.owner
                    return True

        if self.life:
            for obst in scenery:
                if type(obst) != PyGameObj:
                    continue
                col = self.collision(obst.shape)
                if col[0]:
                    return True

        self.move()
        self.life -= 1

        return not self.life
