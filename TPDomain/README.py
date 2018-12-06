#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# READ ME!

# Project name: Collision

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Description:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    My project is a simple multiplayer pvp game with a focus on implementing
collision detection, sensible random generation and file loading. It's akin to
retro space shooter type games where two players duke it out in a rather
simple, geometric map.

    The project itself allows players to, as mentioned before, duke it out in
a 2-dimensional arena where they can collect items and run around in a small
procedurally generated map.
"""

                #==========================================#
            #~~~~~~~~~~~~]         Control         [~~~~~~~~~~~~#
                #==========================================#

"""
FOR KEYBOARD:

    Use the mouse cursor to aim.

    Left Mouse = Use/ fire current item
    Middle Mouse = Pick up item
    Right Mouse = Change current item

    w = Move up
    a = Move left
    s = Move down
    d = Move right

FOR CONTROLLER:

    Use the right thumbstick to aim.
    Use the left thumbstick to move.

    Right Bumper = Use/ fire current item
    x (west-pointing button) = Pick up item
    Left Bumper = Change current item
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# How to use:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    First, this game ONLY supports multiplayer if controllers are plugged
into the computer, but it should support an arbitrary number of players.
Additionally, for the keyboard player, you will need a mouse with a scroll
wheel.


    Next, once you have your controllers plugged in, simply follow the
aformentioned control scheme to play.

TO ACTUALLY RUN THE GAME:

    Simply execute the file "GameShell.py". You will NEED to read the
dependencies section as it is important that you have the required libraries.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Dependencies:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    Note: This project is only tested for windows.

    This project requires that you install:
        - NumPy
        - PyGame
        - SciPy

    These are all available through Pip. While creating this project, I had
my python directory included in my Environment variables so that my computer
could always find pip and any required libraries. If python is not in your
environment variables, you will need to run the python 3 installer,
select modify, and at the advanced options tab, click next WITH the following
option selected in the installer:

    'Add python 3 to environment variables'



    If you've done this, you can simply go into command prompt and run the
following three commands:

pip install numpy
pip install pygame
pip install scipy

    With this done, you should be able to run the GameShell.py file.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Shortcut Commands:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
Hit r on the keyboard to reset game time.
Press escape at any time to end the game.
"""
