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

# No changes yet!

# Updated to vx.x on mm/dd/yyyy
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
                              [(15, 5, 5), (15, 5, 20)],
                              [200, 200, 200], True)
        self.anchor = 175 * (self.player.pNum - 1)


    def draw(self, screen):
        self.mainBox.draw(screen,
                          ["Player " + str(self.player.pNum),
                          "Score: " + str(self.player.wins)])
        barConst = self.anchor + 10
        pygame.draw.rect(screen, (110, 110, 110),
                         pygame.Rect(barConst, 35, 120, 10), 0)

        GUIBox(barConst, 35,
               120 * (self.player.life / self.player.maxLife), 10,
               [(12, 5, 2)], [120, 240, 0], True).\
               draw(screen, [str(self.player.life) + "/" +
                             str(self.player.maxLife)])

        for i in range(1, 6):
            xPos = self.anchor + 10 + (i - 1) * (self.mainBox.w / 5)
            pygame.draw.rect(screen, (240, 240, 240),
                             pygame.Rect(xPos - 9, 50,
                                         self.mainBox.w / 5 - 1, 50), 0)
            self.player.inv[i].icon.draw(screen, (xPos - 5, 60))
            useText = self.player.inv[i].uses if self.player.inv[i].uses else ""
            TextObj(12, xPos, 85).printS(screen, str(useText))

        pygame.draw.rect(screen, (self.player.inv[self.player.curItem].color),
                         pygame.Rect(self.anchor + self.mainBox.w *\
                                     (self.player.curItem - 1) / 5,
                                     50, self.mainBox.w / 5, 50), 2)
