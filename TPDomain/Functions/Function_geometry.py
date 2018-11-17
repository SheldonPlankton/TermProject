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
from time import time

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Function Defs:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Defines the euclidean metric, an indespensible tool for collision.
def eucDist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# this function expects ordered pairs representing coordinates of a line
def getUnitNormal(x1, y1, x2, y2):
    mag = eucDist(x1, y1, x2, y2)
    return ((y2 - y1) / mag, (x1 - x2) / mag)

print(eucDist(*getUnitNormal(1,2,3,4), 0, 0))
                #==========================================#
            #~~~~~~~~~~~~]        Collision        [~~~~~~~~~~~~#
                #==========================================#

# Function for checking circle/ point collision.
def colPointLine(px, py, lxi, lyi, lxf, lyf):
    return isclose(eucDist(lxi, lyi, lxf, lyf),
                   eucDist(px, py, lxi, lyi) + eucDist(px, py, lxf, lyf))



def colCircLine(cx, cy, cr, lxi, lyi, lxf, lyf):
    pass



def colCircPoint(cx, cy, cr, px, py):
    return cr >= eucDist(cx, cy, px, py)



def colCircCirc(c1x, c1y, c1r, c2x, c2y, c2r):
    return c1r + c2r >= eucDist(c1x, c1y, c2x, c2y)



def colRectPoint(rx, ry, rw, rh, px, py):
    return (rx <= px <= rx + rw) and (ry <= py <= ry + rh)



def colRectRect(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h):
    for p in [(0,0), (0,1), (1,0), (1,1)]:
        if colRectPoint(r1x, r1y, r1w, r1h,
                        r2x + r2w * p[0],
                        r2y + r2h * p[1]):
            return True
    return False



def colCircRect(cx, cy, cr, rx, ry, rw, rh):
    if rx <= cx <= rx + rw and ry <= cy <= ry + rh:
        return True
    return colCircPoint()



def colTriPoint():
    pass



def colTriTri():
    pass



def colTriRect():
    pass



def colTriCirc():
    pass
