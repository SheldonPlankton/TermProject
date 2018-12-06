#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Class: Player Spawner



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Description:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    An object with geometry and a draw method designed specifically to be
collidable. A player will point to this and respawn at the center point.

    The collidability is for use in the terrain generation step. Scenery object
will see this and avoid it in spawning.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from Classes.Package_Geometry import Polygon

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class PlayerSpawner:

    def __init__(self, cArg, playerArg):
        self.player = playerArg
        self.c = cArg
        self.shape = Polygon([(self.c[0] + 15 * i[0], self.c[1] + 15 * i[1]) \
                              for i in [(0, 1), (1, 0), (0, -1), (-1, 0)]])
        self.player.setSpawn(self)


    def collision(self, other):
        return self.shape.collision(other)

    def draw(self, screen):
        self.shape.draw(screen,
                        [max(self.player.color[0] - 50, 0),
                         max(self.player.color[1] - 50, 0),
                         max(self.player.color[2] - 50, 0)])
