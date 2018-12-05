#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# "Project Name"
# Created

# Version 0.1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Changelog:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# No changes yet!

# Updated to vx.x on mm/dd/yyyy
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import Classes.Class_Item
from Classes.Package_Geometry import Circle
from math import *
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class HealItem(Classes.Class_Item.Item):

    def __init__(self, nameArg, usesArg, coolArg, healArg,
                 colorArg = (0, 0, 0), imgArg = None):
        super().__init__(nameArg, usesArg, coolArg, colorArg, imgArg)
        self.healVal = healArg

    def use(self, user, players, projectiles):
        if not self.coolCurrent:
            self.uses -= 1
            self.coolCurrent = self.cool
            user.heal(self.healVal)
            return not self.uses
