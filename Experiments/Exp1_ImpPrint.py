#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Project Base

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from deap import algorithms
from deap import base
from deap import creator

import inspect
import socket
import sys
import textwrap
import pygame
import math
import numpy
import tensorflow

print(globals())

imps = set(sys.modules) & set(globals())

                #==========================================#
            #~~~~~~~~~~~~]        Versions        [~~~~~~~~~~~~#
                #==========================================#

for mod in imps:
    print()
    try:
        print("Running " + sys.modules[mod].__name__ +
               " version: " + sys.modules[mod].__version__)

    except:
        print("No version found for " + sys.modules[mod].__name__ + ". Skipping...")

    finally:
        print("Available methods:")
        for line in textwrap.wrap(str(dir(sys.modules[mod]))):
            print("\t\t" + str(line))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]         Helpers         [~~~~~~~~~~~~#
                #==========================================#

                #==========================================#
            #~~~~~~~~~~~~]        Subheader        [~~~~~~~~~~~~#
                #==========================================#

                #==========================================#
            #~~~~~~~~~~~~]        Functions        [~~~~~~~~~~~~#
                #==========================================#

def transformElems(matrix, lamb):
    return list(map(lambda row: list(map(lambda x: lamb(x), row)), matrix))
