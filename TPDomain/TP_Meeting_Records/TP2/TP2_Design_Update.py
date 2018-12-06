#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Term Project Deliverable 2: Update

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Preface:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    This text file provides a brief synopsis of any of the updates that I've
made to the original version of my project.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Design update:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]        Nota Bene       [~~~~~~~~~~~~#
                #==========================================#

"""
    As I mentioned in my TP2 interview, much of the work that has gone into the
project thus far has been purely for functionality. However, now that most of
the groundwork is laid, I can take most of what I've written and apply it more
generally.
"""

                #==========================================#
            #~~~~~~~~~~~~]         Modules        [~~~~~~~~~~~~#
                #==========================================#

"""
    My project now additionally requires the use of Scipy for a few numerical
things, so if you don't have this module, I recommend you install it.
"""

                #==========================================#
            #~~~~~~~~~~~~]        Structure       [~~~~~~~~~~~~#
                #==========================================#

"""
    The biggest structural change that I've made to the code is an overhaul
to the geometric system of the project. In essence, I've written a package
which handles all geometric things and all on-screen objects make use of the
geometry package in some way.

    The main reason for this was so that I could implement accurate collision
for arbitrary convex polygons so that I can make interesting maps that the
players can actually interact with.

    Effectively this was done in two ways. First, all on screen drawn objects
have a shape argument. Shapes are either polygons or circles and are defined
in the geometrty package. Next, each shape has a draw and collision method,
where the collision method uses a function called generalCollider defined
again in the geometry package.

    I then rewrote all of the drawing and collision detection methods for all
in game objects in terms of their shape's methods.

    Because collision works properly, I can really implement anything from UI
widgets to projectiles. This means that the actual player vs player game
functionality works fine, but there is no game exit state, no menus etc as of
now.

    After doing this, I created a little class, Icon(), that contains an image
for any on-screen graphics display and aligns itself based on a given position.
This allows me to draw arbitrary on-screen icons so long as the desired image
exists in the assets folder.
"""
