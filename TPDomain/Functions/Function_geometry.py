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

# Planned features / updates:
#   o Write collision detections

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Changelog:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# No changes yet!

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Overview:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    This file is just a bin of euclidian geometry helpers. Most of the utility
of this file is in the euclidian collision detection functions used.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from math import *
from numpy import *
from scipy.spatial import distance
from time import time

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function Defs:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Defines the euclidean metric, an indespensible tool for collision.
def eucDist(p1, p2):
    return distance.euclidean(p1, p2)

def getUnitVect(p1, p2 = (0,0)):
    (x1, y1), (x2, y2) = p1, p2
    mag = eucDist(p1, p2)
    return ((x1 - x2) / mag, (y1 - y2) / mag)

# this function expects ordered pairs representing coordinates of a line
def getUnitNormal(p1, p2 = (0, 0)):
    (x1, y1), (x2, y2) = p1, p2
    mag = eucDist(p1, p2)
    return ((y2 - y1) / mag, (x1 - x2) / mag)

#Generator to get pairs of points which define the sides of a shape
def getSides(points):
    for i in range(len(points)):
        yield points[i-1], points[i]

def getNorms(points):
    for i in range(len(points)):
        yield getUnitNormal(points[i-1], points[i])

def projection(vect1, vect2):
    return dot(vect1, getUnitVect(vect2))


                #==========================================#
            #~~~~~~~~~~~~]        Collision        [~~~~~~~~~~~~#
                #==========================================#

def sepAxisTheoremCheck(line1, line2, norm):


def generalCollider(shape1, shape2):
    norms = [(p1, p2) for p1, p2 in getNorms(shape1.points)] + \
            [(p3, p4) for p3, p4 in getNorms(shape2.points)]

    if type(shape1) == Polygon == type(shape2):
        for norm in getNorms(shape2.points):
            for side1 in getSides(shape1):
                for side2 in getSides(shape2):
                    if not sepAxisTheoremCheck(side1, side2, norm): return True

    elif type(shape1) == Circ:
        pass

    elif type(shape2) == Circ:
        pass

def colCircCirc(c1, r1, c2, r2):
    return eucDist(c1, c2) < r1 + r2
