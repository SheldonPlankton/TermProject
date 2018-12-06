#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Class: Gui Box Player Info
# Created

# Version #

# Planned features / updates:
#   o Main feature description
#       - Subdescription

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Changelog:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    This is a class that simply points to a player and draws a simple inventory
at the top of the screen. Each part is marked by what is being drawn
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from Classes.Class_GUIBox import GUIBox
from Classes.Class_TextObj import TextObj
import pygame

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class GUIBoxPlayerInfo:

    def __init__(self, playerArg):
        self.player = playerArg
        self.mainBox = GUIBox(175 * (self.player.pNum - 1), 0, 150, 100,
                              [(15, 5, 5), (15, 50, 5),
                               (12, 10, 15), (12, 10, 24)],
                              [100, 100, 100], True)
        self.anchor = 175 * (self.player.pNum - 1)
        self.itemBox = []
        for i in range(1, 6):
            xPos = self.anchor + 10 + (i - 1) * (self.mainBox.w / 5)
            self.itemBox += [(i, GUIBox(xPos - 9, 50, self.mainBox.w / 5 - 1, 50,
                                    [(12, 10, 30)], (240, 240, 240), True))]



    def draw(self, screen):

        self.mainBox.draw(screen,
                          ["Player " + str(self.player.pNum),
                          "Score: " + str(self.player.wins),
                          "Swap Cooldown", "Collect Cooldown"],
                          [self.player.color] + 3 * [None])

        barConst = self.anchor + 10
        pygame.draw.rect(screen, (40, 40, 40),
                         pygame.Rect(barConst, 35, 120, 10), 0)

        GUIBox(barConst, 35,
               120 * (self.player.life / self.player.maxLife), 10,
               [(12, 5, 2)], [60, 120, 0], True).\
               draw(screen, [str(self.player.life) + "/" +
                             str(self.player.maxLife)], [(255, 255, 255)])

        # Draw swap and collection cooldown bars
        pygame.draw.rect(screen, (40, 40, 40),
                        pygame.Rect(self.anchor + 90, 18, 40, 4), 0)
        pygame.draw.rect(screen, (40, 40, 40),
                        pygame.Rect(self.anchor + 90, 27, 40, 4), 0)

        pygame.draw.rect(screen, (170, 210, 80),
                     pygame.Rect(self.anchor + 90, 18,
                     40 * ((50 - self.player.swapCool) / 50), 4), 0)

        pygame.draw.rect(screen, (170, 210, 80),
                     pygame.Rect(self.anchor + 90, 27,
                     40 * ((120 - self.player.colCool) / 120), 4), 0)

        # Draw inventory
        for slot in self.itemBox:

            xPos = self.anchor + 10 + (slot[0] - 1) * (self.mainBox.w / 5)
            item = self.player.inv[slot[0]]
            useText = item.uses if item.uses else ""
            slot[1].draw(screen, [str(useText)])
            self.player.inv[slot[0]].icon.draw(screen, (xPos - 5, 60))
            if item.name != None:
                pygame.draw.rect(screen, (40, 40, 40),
                                pygame.Rect(xPos - 3, 90, 20, 4), 0)

                pygame.draw.rect(screen, (210, 210, 20),
                             pygame.Rect(xPos - 3, 90,
                            20 * ((item.cool - item.coolCurrent) /\
                                  item.cool), 4), 0)


        pygame.draw.rect(screen, (self.player.inv[self.player.curItem].color),
                         pygame.Rect(self.anchor + self.mainBox.w *\
                                     (self.player.curItem - 1) / 5,
                                     50, self.mainBox.w / 5, 50), 2)
