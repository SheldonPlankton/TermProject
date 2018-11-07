#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Experiment 1: Import printer
# Created 10/28/2018

# Version 0.2
# Updated 11/6/2018
#   o Modified error text for packages without version labels.
#   o Improved collecting module names from manual entry to automatic process.
#   o Added a 'finally' statement to error handler.

# Planned features / updates:
#   o Print only practially useable methods.
#       - exclude exceptions, __"word"__ methods etc.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# A few random packages to import for demonstration purposes.
import inspect
import socket
import sys
import textwrap
import pygame
import math
import numpy
import tensorflow

imps = set(sys.modules) & set(globals())

                #==========================================#
            #~~~~~~~~~~~~]        Versions        [~~~~~~~~~~~~#
                #==========================================#

# Top level header code that prints out each imported module along with available
#methods and version number (if available).

for mod in imps:
    print()
    try:
        print("Running " + sys.modules[mod].__name__ +
               " version: " + sys.modules[mod].__version__)

    except:
        print("No version found for " + sys.modules[mod].__name__ + "!")

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
