#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# "Project Name"
# Created

# Version .1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Changelog:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# No changes yet!

# Updated to vx.x on mm/dd/yyyy
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import Classes.Class_Item
from Classes.Class_ProjectileBase import ProjectileBase
from Classes.Package_Geometry import Circle
from math import *
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class BaseWeapon(Classes.Class_Item.Item):

    def __init__(self, nameArg, usesArg, coolArg, spdArg, lifeArg, dmgArg,
                 pRadArg, pColArg, colorArg = (0, 0, 0), imgArg = None):
        super().__init__(nameArg, usesArg, coolArg, colorArg, imgArg)
        self.spd = spdArg
        self.life = lifeArg
        self.dmg = dmgArg
        self.pRad = pRadArg
        self.pCol = pColArg

    def use(self, user, players, projectiles):
        if not self.coolCurrent:
            self.uses -= 1
            self.coolCurrent = self.cool
            projectiles += [
                            ProjectileBase(
                            user.lookDir, self.spd, self.life, self.dmg,
                            Circle((
                            user.shape.c[0] + user.shape.r * cos(user.lookDir),
                            user.shape.c[1] + user.shape.r * sin(user.lookDir),
                            ), self.pRad, imgArg = 'Test'),
                            self.pCol
                            )
                           ]
            return not self.uses
