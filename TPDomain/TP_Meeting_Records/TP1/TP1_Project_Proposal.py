#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Term Project Deliverable 1: Proposal


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Preface:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    This text file provides answers to each written part of the project proposal
as per the Term Project section of the 15-112 course website. Each answer is
given under an appropriately named subheader
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Design proposal:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                #==========================================#
            #~~~~~~~~~~~~]      Description       [~~~~~~~~~~~~#
                #==========================================#

"""
    This project aims to be a simple arena-based multiplayer combat game where
players either battle eachother with items scattered around a map, or cooperate
to battle a common enemy. Players will run around a map, gather items and
optimize their loadouts in order to compete most effectively.
"""

                #==========================================#
            #~~~~~~~~~~~~]     Comp Analysis      [~~~~~~~~~~~~#
                #==========================================#

"""
    This project aims to play like a multiplayer 2-D player-vs-player and
player-vs-environment style game with a control style inspired by the classic
game Geometry Wars: Retro Evolved. Geometry Wars is an arcade-style twin-stick
shooter originally featured as a minigame in an old XBox racing game that grew
to become its own full-fledged franchise. In the game, the player pilots a small
triangular ship and aims to survive an onslaught of various hostile geometric
figures such as squares, circles, hexagons, etc. The game features straight-
forward fluid controls wherein the player uses one stick to move their ship and
one stick to aim the gun on their ship.

    However, while the control scheme is intended to follow suit and the raw
gameplay is meant to be similar, the player was limited to either single-player
or online coop, had access to only one primary weapon, and had a choice of only
one map with varying enemy patterns depending on gamemode. In my project, I seek
to emphasize the gameplay elements while adding various maps, more dynamic enemy
types and AI, and a more diverse selection of items. Additionally, from a
thematic perspective, I seek to bring this game out of the abstract and surreal
style of the source material and into something more akin to arena-based
online player-vs-player games like the Halo games, PUBG and, begrudgingly,
Fortnite.

    These titles spring to mind as they are the sorts of gold-standards of the
"run around, explore and fight in a limited time frame" style of video game.
However, as these 3 are renowned triple A games made by large studios, I will
not be making something on the same scale. However, I seek to go more in-depth
with item selection and player customizability than what these games permit so
that for whatever this project lacks in showiness in comparison to these games,
it will have significantly more creative playstyles and strategies. In a way,
the truncation of the third dimension allows for effective use of more complex
randomization, ensuring that no two experiences with this project will be
identical.
"""

                #==========================================#
            #~~~~~~~~~~~~]    Structural Plan     [~~~~~~~~~~~~#
                #==========================================#

"""
    As you may have noticed, this project is currently broken down into various
folders with different names. For the time being, they are divided by code
segments that define classes and code segments that define functions and
subroutines that the project must execute in order to run properly.

    I plan to further break down the folders and sort their contents such that
functions are divided by whether or not they are used as a functional subroutine
called by the main body of the code or whether they are a package of algorithms.

    For classes, I plan to organize by whether or not a class is an in-game
element, a User Interface element or a more nuanced tool employed by the
program, as in the controller manager and keyboard manager classes I have
written.
"""

                #==========================================#
            #~~~~~~~~~~~~]    Algorithmic Plan    [~~~~~~~~~~~~#
                #==========================================#

"""
    As for algorithms, I will need to create a set of functions for fast
collision handling, a set of functions for fast random map generation, and
a function for enemy AI:

Collision:

    I have started writing a library for this but plan to reimplement it
according to the SAT collision algorithm. This algorithm takes two polygons
and attempts to find a line which can be drawn between both of them that does
not intersect either polygon. This will be a tad tricky, but there are
simplifications which check the intersections of the projections of each face
of the polygons on the lines defined by the vector normal to each face.

    Additonally, there is a supplemental algorithm, the minimum translation
vector, which finds a vector that moves an object the minimum distance from
a site of collision.

    The main difficulty in this will be checking the points that define
an object's bounding box, but I can reconcile this by writing polygon classes
which have collision handling methods and then, on initializing an object,
just pass the object's shape in as the polygon object and then have the object
receive it's collision based on the polygon variable in the object.

Map generation:

    The maps will have scenery that can be genaerated randomly, but the
goal is to ensure a certain amount of the screen is player-navigable. This
can be done with random generation and backtracking, wherein each map generated
will need to satisfy a predefined condition each time a new scenery object is
added during initialization. This will take advantage of the collision
algorithms mentioned previously as well as approximate area calculations.

Enemy AI:

    For now, the goal is to have simple generic enemy AI's, and the easiest way
to do this is to have enemies seek players by checking a given radius circle
around the enemy's centroid for player collision. After this, for more complex
enemy behavior, it will be integral that I implement some kind of finite state
automata into the AI where the state of the game changes the enemy's state,
and from there the state will determine the decisions of the enemies. I also
want the enemy AI to be parametric and modular so that I can diversify
what enemies are capable of with different numerical inputs.
"""

                #==========================================#
            #~~~~~~~~~~~~]     Timeline Plan      [~~~~~~~~~~~~#
                #==========================================#

"""
    I have a pretty light schedule so I've been working for about 3 hours a day
on this project. I have the game in a very stable functioning form without any
implemented generalized collision as of now. I should be finished with all of
the collision and map generation stuff by the end of Thanksgiving break, and
seek to at least have a simple enemy AI complete by then.

    After this, I seek to begin implementing different hand-drawn art assets
into the project and hope to have these done before TP2. I will begin finalizing
the GUI elements by then as well so that the player experience is a tad more
intriguing. and straightforward.
"""

                #==========================================#
            #~~~~~~~~~~~~]  Version Control Plan  [~~~~~~~~~~~~#
                #==========================================#

"""
    I am using GitHub for version control as well as backing up files on my
personal computer. See included image for proof of GitHub.
"""

                #==========================================#
            #~~~~~~~~~~~~]       Module List      [~~~~~~~~~~~~#
                #==========================================#

"""
pygame
numpy
"""
