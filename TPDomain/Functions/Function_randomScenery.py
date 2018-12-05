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

# Updated to vx.x on mm/dd/yyyy
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from Classes.Class_PyGameObj import PyGameObj
from Classes.Package_Geometry import Polygon
from random import randint
from copy import copy
from math import *

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def randomSceneryObject(verts, center, baseRad, radDev, angDev):
    dTheta = 360 / verts
    points = []
    for i in range(verts):
        angle = -i * dTheta + randint(-angDev, angDev)
        rad = baseRad + randint(-radDev, radDev)
        x = center[0] + rad * cos(radians(angle))
        y = center[1] + rad * sin(radians(angle))
        points += [(x, y)]
    return PyGameObj(Polygon(points))

def randomSceneryGen(screenSize, pieces, scenery = []):
    scenery = copy(scenery)

    if len(scenery) == pieces: return scenery



    while True:
        skip = False
        newSceneryPiece = randomSceneryObject(randint(3, 7),
                                              (randint(0, screenSize[1]),
                                              randint(50, screenSize[0])),
                                              randint(20, 70), randint(2, 5),
                                              randint(0, 10)
                                              )
        for obj in scenery:
            if obj.collision(newSceneryPiece.shape):
                skip = True

        if not skip:
            scenery += [newSceneryPiece]
            newScenery = randomSceneryGen(screenSize, pieces, scenery)
            if newScenery != None:
                return newScenery
