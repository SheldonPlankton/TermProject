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

# Updated to v0.2 11/27/2018
# o Moved all of the shape classes into this file to avoid circular
#       dependency bug.

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
import pygame
from Classes.Class_Icon import Icon

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

# Quick circle/ circle collision function
def colCircCirc(c1, r1, c2, r2):
    return eucDist(c1, c2) < r1 + r2

                #==========================================#
            #~~~~~~~~~~~~]        Collision        [~~~~~~~~~~~~#
                #==========================================#

def sepAxisTheoremCheck(line1, line2, norm):
    pass

def generalCollider(shape1, shape2):
    if type(shape1) == Circle == type(shape2):
        return colCircCirc(shape1.c, shape1.r, shape2.c, shape2.r)

    elif type(shape1) == Polygon == type(shape2):
        norms = [(p1, p2) for p1, p2 in getNorms(shape1.points)] + \
                [(p3, p4) for p3, p4 in getNorms(shape2.points)]
        for norm in getNorms(shape2.points):
            for side1 in getSides(shape1):
                for side2 in getSides(shape2):
                    if not sepAxisTheoremCheck(side1, side2, norm): return True

    elif type(shape1) == Circle:
        pass

    elif type(shape2) == Circle:
        pass

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Class Defs:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Circle:

    def __init__(self, centerArg, rArg, imgArg = False):
        self.c = list(centerArg)
        self.r = rArg
        if imgArg:
            self.img = Icon(imgArg)

    def collision(self, other):
        if type(other) == Circle:
            return colCircCirc(self.c, self.r, other.c, other.r)

        else:
            return generalCollider(self, other)

    def draw(self, screen, color):
        if not hasattr(self, 'img'):
            pygame.draw.circle(screen, color,
                               (int(self.c[0]), int(self.c[1])),
                               int(self.r))
        else:
            self.img.draw(screen, (int(self.c[0] - sqrt((self.r**2)/2)),
                                   int(self.c[1] - sqrt((self.r**2)/2))))

class Polygon:

    def __init__(self, pointsArg):
        self.points = [list(p) for p in pointsArg]

    def collision(self, otherShape):
        return generalCollider()

    def draw(self, parent, screen):
        pygame.draw.polygon(screen, parent.color, self.points)
