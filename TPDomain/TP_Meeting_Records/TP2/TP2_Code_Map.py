#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Term Project Deliverable 2: Code Map

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Description:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
    This document aims to be a roadmap to the program that I've written so far,
providing a description of where to look for specific features.

    This is the updated version and /only/ includes things that have been
changed since the last version of the project. Since I haven't done much in
terms of fully removing code (aside from a folder of defunct functions), I
don't mention most radical changes. I do however try to mention any cases where
important code has been moved.
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
    I've added an additional test line that instantiates a scenery object for
collision testing. This is found on line 111.

    In the final verion this file will instead call a separate game loop
and this file will simply be used for the top level stuff, like separating
menus from the actual game.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TPDomain\Classes:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]  playerControlPortion  [~~~~~~~~~~~~#
                #==========================================#

"""
    This file is the player logic section.

This function now accepts a list of scenery objects as an argument.

On line 60, you can find the player/ scenery collision detection loop.

On line 64, you can find the projectile collision detection loop which
will delete any projectiles as soon as they've collided with something.
"""

                #==========================================#
            #~~~~~~~~~~~~]    displayPortion     [~~~~~~~~~~~~#
                #==========================================#

"""
    This file controls all things displayed in game.

On line 64 I've added debugging text to track player health.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# TPDomain\Classes:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]      Collectible       [~~~~~~~~~~~~#
                #==========================================#

"""
    This is a base class for collectible objects shown on screen.

    The draw function has been slightly modified in accordance with the
new geometry system that I've implemented. It now draws an aura based on the
contained item's color and then draws the item's icon within. This is found on
line 47 in the draw method.
"""

                #==========================================#
            #~~~~~~~~~~~~]          Item          [~~~~~~~~~~~~#
                #==========================================#

"""
    This is the base class that all in-inventory items will inherit from.

    On line 47, if the function is called with the name of one of the assets
in the assets/images folder, it will have an icon associated which is the
indicated image. It then has a draw function which only does anything if the
image has been instantiated with an icon.
"""

                #==========================================#
            #~~~~~~~~~~~~]          Icon          [~~~~~~~~~~~~#
                #==========================================#

"""
    This is class used to instantiated a "blit" item in pygame, which is just
a way of drawing an image. It takes the name (without extension) of a png
in the assets/images folder of the folder TPDomain in its constructor and
uses the pygame image load function to load the image. This is then implemented
in the geometry package later for easy access to images.
"""

                #==========================================#
            #~~~~~~~~~~~~]         Player         [~~~~~~~~~~~~#
                #==========================================#

"""
    On line 180, there is a use function defined which calls an item's use
function and then removes it from inventory if the given item is out of
uses.

    Additionally, on line 174, the player object now has a collision detection
method which has an almost functional system for moving a player away from an
arbitrarily angled wall upon collision.

    Finally, the player object calls it's shape variable's draw function in
order to be drawn. This is on line 211.
"""

                #==========================================#
            #~~~~~~~~~~~~]        PyGameObj       [~~~~~~~~~~~~#
                #==========================================#

"""
    This now takes a shape object as an argument in its constructor. It now
uses its shape's draw and collision methods for these respective tasks, which
are defined on lines 44 and 47.

"""

                #==========================================#
            #~~~~~~~~~~~~]    Projectile Base     [~~~~~~~~~~~~#
                #==========================================#

"""
    This extends the entity class and will be extended by other projectile
objects.

    On lines 48 and 51, the projectile will invoke its shape's collision and
draw methods.

Line 54 is the new update, which checks how long a projectile has existed,
whether it has collided with a player or any scenery, and finally will return
True if it collides or has existed for too long. Additionally, on line 61,
if it detects collision with a player, it will deal damage to the player it
hits.
"""

                #==========================================#
            #~~~~~~~~~~~~]     Items\Item Wep     [~~~~~~~~~~~~#
                #==========================================#

"""
    This is the first weapon item created and already supports a good amount
of generality.

    On line 30, it invokes the constructor for the Item superclass. The
following lines of its constructor are all variables that will be the properties
of the projectiles it creates.

    On line 45, the use method is defined. This method is called by the player
class. Effectively, it takes in the list of projectiles in game and adds a new
one whenever this function is called until the item runs out of uses. Line 49
is where the new projectile is instantiated, and it's instantiation is called
taking a number of the weapon's variables as arguments such as the damage,
position, speed etc.
"""

                #==========================================#
            #~~~~~~~~~~~~]    Package_Geometry    [~~~~~~~~~~~~#
                #==========================================#

"""
Line 51 defines the euclidean distance function between two points using
scipy.

Line 54 gets the unit vector of a vector from point 1 to point 2. It has a
default parameter of setting the tail of the vector to the origin.

Line 60 is similar to getUnitVect but it gets the unit normal, which is simply
the unit vector which is perpendicular to a given vector.

Line 66 is a generator that yields two sequential points in a list of points.

Line 70 is a generator that yields the unit normal of a pair of points.

Line 74 returns the projection of 1 vector centered at the origin onto another
vector.

Line 78 detects circle-circle collisions.

Line 88 is a bit unfinished, but it accurately detects the collision of a circle
and a convex polygon. The "mtvCheck" stuff is intended to obtain something
called the minimum translation vector, which is basically the smallest push
needed to move two objects out of collision.

Line 119 obtains the minimum and maximum projections of a list of vectors onto
a given axis. This is necessary for the Separating axis theorem to work.

Line 130 implements the separating axis theorem by seeing if the maximum
projection of one shape is smaller than the minimum of another, which implies
there is a separation between the shapes along the axis normal to the checked
axis.

Line 139 is the general collider. This takes two shapes, determines their types,
and then uses the collision detector most appropriate for the shape pairing. It
returns True as soon as it is detemined that two shapes do not collide.

Line 163 defines the circle class, a class which is integral to the geometric
functionality of this game. On line 165 we find the constructor. On line 171,
the circle calls the general collider. In it's draw function, it will draw
it's icon if it is called with an image name for the parameter imgArg,
or it will simply display the actual circle if not.

Line 183 Is the polygon, which is simpler for now in that it cannot have an
icon displayed. It is created with a set of points. On line 188, we see the
general collision function again called as the collision detector. Finally,
on line 191, we see the draw function, which draws a polygon with the
set of points stored in the polygon object.
"""
