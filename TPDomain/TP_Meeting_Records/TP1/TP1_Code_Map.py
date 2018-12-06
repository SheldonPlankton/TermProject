#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Term Project Deliverable 1: Code Map

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Description:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
    This document aims to be a roadmap to the program that I've written so far,
providing a description of where to look for specific features.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Map:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]       Preliminary      [~~~~~~~~~~~~#
                #==========================================#

"""
    First, you'll need to go into the folder TermProject\TPDomain to find all
the relevant code. Once there, to run the game, run the "GameShell.py" python
file. I recommend running through command line, as I've been wrting these in
atom but have realized that the program does not run in Pyzo or other python
script executors.
"""

                #==========================================#
            #~~~~~~~~~~~~]        GameShell        [~~~~~~~~~~~~#
                #==========================================#
"""
    This is the file where most of the control magic happens.

On line 75 I initialize a variable to control the main game loop.
On the next line, I initialize pygame.

Lines 79 through 84 create the input manager object and collectibles,
which will be described later.

On lines 87 through 89, I set up text display and window settings.

Line 91 is where the default keyboard player is created.

Lines 95 through 98 are where the gamepad players are initialized, if any
gamepads exist.

Lines 102 through 117 are the main game loop, and 119 exits if the loop ends.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TPDomain\Functions:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]  playerControlPortion  [~~~~~~~~~~~~#
                #==========================================#

"""
    This file is the player logic section.

Line 46 defines the function.

Lines 48 through 50 listen for game quit events and appropriately return True.
This behavior is used in the main game loop.

Lines 53 through 58 call player methods to be described later, but effectively,
they are calls that allow the game to work.

Lines 63 through 66 listen for a controller player to press the start butten,
closing the man game loop.
"""

                #==========================================#
            #~~~~~~~~~~~~]    displayPortion     [~~~~~~~~~~~~#
                #==========================================#

"""
    This file controls all things displayed in game.

Lines 35-37 initialize color constants.

Line 39 defines the function.

Line 40 starts the background as stark white.

Lines 41-43 draw all collectible objects.

Line 45 readies the text display.

Line 46 initializes the player draw loop.

Lines 48-49 draw the player and a line indicative of where the player is looking
for debugging purposes.

Lines 51 through 61 print information about the players to the screen.

Line 64 actually allows all of the information that is primed for drawing to
be drawn to the screen.
"""

                #==========================================#
            #~~~~~~~~~~~~]       geometry         [~~~~~~~~~~~~#
                #==========================================#

"""
    This is a nont-fully-implemented rudimentary collsion detection suite
that is planned to be replaced by a Separating axis theorem based collision
detection function.

The function names are pretty self explanatory:

col: Collision

circ: Circle

rect: Rectangle

tri: Triangle
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TPDomain\Classes:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]      Collectible       [~~~~~~~~~~~~#
                #==========================================#

"""
    This is a base class for collectible objects shown on screen.

Line 43 is the initialization function.

Line 49 is the collision detector.

Line 53 is the draw function.
"""

                #==========================================#
            #~~~~~~~~~~~~]         Entity         [~~~~~~~~~~~~#
                #==========================================#

"""
    This is the base entity class that all moving objects inherit from.

Line 38 is the initialization function.

Line 48 is the movement function.
"""

                #==========================================#
            #~~~~~~~~~~~~]          Item          [~~~~~~~~~~~~#
                #==========================================#

"""
    This is the base class that all in-inventory items will inherit from.

Line 39 is the initialization function.

Line 47 is the draw function that gets called by the collectible object
containing the item. This allows collectibless to be generic and have their
appearance change based on the item contained.
"""

                #==========================================#
            #~~~~~~~~~~~~]    Keyboard Manager    [~~~~~~~~~~~~#
                #==========================================#

"""
    This is a wrapper class for player keyboard input which is called by
player objects with the 'KEYBOARD' control type. This object was designed
to operate in a somewhat hacky parallel to the built-in Joystick object that
pygame ships with, for ease of code-writing.

Line 46 is the initialization.

Line 49-58 is the directional key wrapping method, which is checked in the
'KEYBOARD' player's move function.

Line 60 is a function that simply gets the position of the mouse cursor.

Line 64 is a function for getting the mouse button events.
"""

                #==========================================#
            #~~~~~~~~~~~~]         Player         [~~~~~~~~~~~~#
                #==========================================#

"""
    This is the default player object, subject to modification and improvement.

Line 62 is the docstring shown in text completion plugins for atom.

Line 68 is the initialization definition.

Line 91 is the equip method, which takes gets called by the later collect
method and performs operations on the list of in game collectibles. Effectively,
if the player tries to pick up an item, if the already have an item in their
current inventory slot, it will get dropped and replaced by the appropriate
collectible.

Line 103 is the swap method, which simply switches which item the player
currently has equipped.

Line 120 is a function which controls where the player is looking.

Line 136 is the player move function which listens to the results of the
appropriate controller methods from the input manager object initialized
at the start of the game.

Line 153 is the collect method which looks at all of the collectibles currently
spawned, checks collision with the player and then sees if the player is
pressing the appropriate collection method. It has an internal function on line
157 used to handle all of the aformentioned procedures.

Line 178 updates any cooldown timers so that the player cannot rapidly perform
actions like collection and swapping, making the game playable.

line 188 is the current draw method to be updated later.

Line 198 is a debugging method used to see what direction the player is
looking in.
"""

                #==========================================#
            #~~~~~~~~~~~~]  Player Input Manager  [~~~~~~~~~~~~#
                #==========================================#

"""
    This class doubles as a wrapper for pygame's joystick class and a sort
of container for all of the controllers in the game.

Line 68 initializes the controller manager object.

Line 83 adds is a method to add or remove controllers from the input manager
object so that no crashes occur.

Line 94 is a method to more safely handle player controller removal, though
due to various restructures it is entirely possible that this will be removed
in later updates.

Line 110 is amethod to start a joystick object, allowing the program to listen
for any events it produces.

Line 134 is a function to see if a controller is initialized for pygame.

Line 142 gets all of the events from a controller, though this may be removed.

Line 151 is a function which checks to see if the player is pressing a specific
button.

Line 165 is a function which reads the axial positions of a given thumbstick.
"""

                #==========================================#
            #~~~~~~~~~~~~]        PyGameObj       [~~~~~~~~~~~~#
                #==========================================#

"""
    This is a class that forms the basis of all on screen interactable and
scenery objects. line 40 is the initialization method and line 44 is the default
draw method.
"""

                #==========================================#
            #~~~~~~~~~~~~]       Text Print       [~~~~~~~~~~~~#
                #==========================================#

"""
    This is an extended version of a wrapper for putting text onto the screen,
obtained from a pygame tutorial.

Line 56 initializes a color constant.

Line 59 is the initalization function.

Line 63 is a method that puts text into the given text object and prepares it
to be drawn.

Line 68 resets the text object, like if the drawn text needs to be refreshed.

Lines 73 and 76 are self explanatory, they indent and unindent the text to be
drawn.
"""

                #==========================================#
            #~~~~~~~~~~~~]    Projectile Base     [~~~~~~~~~~~~#
                #==========================================#

"""
    This extends the entity class and will be extended by other projectile
objects.

Line 39 is the initializtion method.

Line 43 is the update method which returns true if the projectile has gotten
to the end of its lifetime.
"""
