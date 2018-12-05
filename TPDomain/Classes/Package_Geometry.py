#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Geometry Package
# Created

# Version 0.3

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Changelog:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Updated to v0.3 on 11/27/2018
# o Finished Separating Axis Theorem integration for collision detection

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

# This take a line segment and a point and return the distance between the
#point and the line segment. lp1 and lp2 define the line, p0 is the
#point to check. This equation comes from reading some wikipedia articles.
def distPointLine(lp1, lp2, p0):
    if lp1[0] - lp2[0] == 0:
        return abs(p0[0]-lp2[0])

    elif lp1[1] - lp2[1] == 0:
        return abs(p0[1]-lp2[1])

    termA = (lp2[1] - lp1[1]) * p0[0]
    termB = (lp2[0] - lp1[0]) * p0[1]
    termC = lp2[0]*lp1[1] - lp2[1]*lp1[0]
    termD = sqrt((lp2[1] - lp1[1])**2 + (lp2[0] - lp1[0])**2)
    return abs(termC + termA - termB) / termD

def colCircLineSeg(lp1, lp2, circ):
    if (min(lp1[0], lp2[0]) < circ.c[0] < max(lp1[0], lp2[0]) and \
       min(lp1[1], lp2[1]) < circ.c[1] < max(lp1[1], lp2[1])) and \
       distPointLine(lp1, lp2, (circ.c[0], circ.c[1])) < circ.r:
       return True
    return False

# Checks for collision between a polygon and a circle using a modified
#version of the separating axis theorem. Effectively, the minimum and maximum
#projections onto an axis for a circle will always be the projection of the
#center plus or minus the radius. It then returns true if there is collision,
#or false if there is not. Finally, this function will also handle
#searching for a minimum translation vector, since players are assumed to
#circles
def colCircPoly(circle, polygon, mtvCheck = False):
    minTransVect = (0, 0)

    for side in getSides(polygon.points):
        norm = getUnitNormal(*side)

        if colCircLineSeg(*side, circle):
            if mtvCheck:
                theta = atan2(norm[1], norm[0])
                minTransVect = (-5 * cos(theta), -5 * sin(theta))
            return True if not mtvCheck else True, minTransVect

    return False if not mtvCheck else False, minTransVect

                #==========================================#
            #~~~~~~~~~~~~]        Collision        [~~~~~~~~~~~~#
                #==========================================#

# This gets the minimum and maximum projections along a given axis
def getMinMaxProj(shape, axis):
    minP, maxP = projection(shape.points[0], axis), 0
    for p in shape.points:
        proj = projection(p, axis)
        if proj < minP: minP = proj
        elif proj > maxP: maxP = proj

    return minP, maxP

# Returns True if there is no overlap between the minimum projection of one
#and the maximum of another
def sepAxisTheoremCheck(shape1, shape2, axis):
    min1, max1, min2, max2 = (*getMinMaxProj(shape1, axis),
                              *getMinMaxProj(shape2, axis))
    if max1 < min2 or max2 < min1:
        return True
    return False

# This checks for a separating axis and returns False as soon as one is found,
#indicating no collision
def generalCollider(shape1, shape2, mtvCheck = False):
    if type(shape1) == Circle == type(shape2):
        return colCircCirc(shape1.c, shape1.r, shape2.c, shape2.r)

    elif type(shape1) == Polygon == type(shape2):

        for norm in getNorms(shape2.points):
            if sepAxisTheoremCheck(shape1, shape2, norm): return False
        return True

    elif type(shape1) == Circle:
        return colCircPoly(shape1, shape2, mtvCheck)

    elif type(shape2) == Circle:
        return colCircPoly(shape2, shape1, mtvCheck)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Class Defs:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Both of these classes are cases to handle polygonal and round bounding boxes
#with both collisional and drawing methods bundled inside
class Circle:

    def __init__(self, centerArg, rArg, imgArg = False, angArg = 0):
        self.c = list(centerArg)
        self.r = rArg
        if imgArg:
            self.img = Icon(imgArg, angArg)

    def collision(self, other):
        return generalCollider(self, other)

    def draw(self, screen, color):
        if not hasattr(self, 'img'):
            pygame.draw.circle(screen, color,
                               (int(self.c[0]), int(self.c[1])),
                               int(self.r))
        else:
            self.img.draw(screen,
                         (int(self.c[0] - sqrt((self.r**2)/2)),
                         int(self.c[1] - sqrt((self.r**2)/2))))

class Polygon:

    def __init__(self, pointsArg):
        self.points = [list(p) for p in pointsArg]

    def collision(self, otherShape):
        return generalCollider(self, otherShape)

    def draw(self, screen, color):
        pygame.draw.polygon(screen, color, self.points)
