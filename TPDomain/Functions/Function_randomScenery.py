#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Function: Generate Random Scenery

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Description:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    This package is used to first create a semi-random scenery object, and
then recursively create a valid random list of scenery objects such no single
scenery object has collision with any other object. This is done with a sort
of twisted backtracking solution in tandem with the separating axis collision
detector from the geometry package.
"""

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


# This creates a scenery object randomized by a set of parameters. Basically,
#it takes a center point and generates a vertex at a certain slightly
#randomized radius at each subdivision of . Verts is number of vertices to
#create, center is the point of the center, baseRad is the base radius,
#radDev is the amount that we let the radius vary, and angDev is the variance
#allowed in the angular position of the vertex.

def randomSceneryObject(verts, center, baseRad, radDev, angDev):
    dTheta = 360 / verts
    points = []
    for i in range(verts):
        angle = -i * dTheta + randint(-angDev, angDev)
        rad = baseRad + randint(-radDev, radDev)
        x = center[0] + rad * cos(radians(angle))
        y = center[1] + rad * sin(radians(angle))
        points += [(x, y)]

    return PyGameObj(Polygon(points),
                     (randint(150, 200),
                      randint(100, 150),
                      randint(20, 100)))

def randomSceneryGen(screenSize, pieces, scenery = []):
    scenery = copy(scenery)

    if len(scenery) == pieces: return scenery

    while True:
        skip = False
        # Generate a new random scenery object
        newSceneryPiece = randomSceneryObject(randint(3, 7),
                                              (randint(0, screenSize[0]),
                                              randint(100, screenSize[1])),
                                              randint(20, 70), randint(2, 5),
                                              randint(0, 10)
                                              )

        # Test object's collision with already-present scenery. If collision
        #occurs, break loop and try a new scenery object. If no collisions
        #occur, recursively call the scenery generator
        for obj in scenery:
            if obj.collision(newSceneryPiece.shape):
                skip = True
                break

        if not skip:
            scenery += [newSceneryPiece]
            return randomSceneryGen(screenSize, pieces, scenery)
