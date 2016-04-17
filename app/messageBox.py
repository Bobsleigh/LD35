import pygame
from app.settings import *

from app.textLine import TextLine


#For a very short message only

class MessageBox(pygame.sprite.Sprite):
    def __init__(self, textList, width, height, centerx, centery,line2='123'):
        super().__init__()

        self.msgFont = pygame.font.SysFont(FONT_NAME,24)

        self.lines = []

        for text in textList:
            self.lines.append(TextLine(text))

        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.rect.center = (centerx,centery)

        self.button = pygame.Rect(0, 0, 0, 0)
        self.button = self.rect.inflate(-self.image.get_height() * 0.1, -self.image.get_height() * 0.1)
        self.button.x = self.image.get_height() * 0.05
        self.button.y = self.image.get_height() * 0.05

        self.textPos = [0,0]

        # Color
        self.color1 = COLOR_MENU_1
        self.color2 = COLOR_MENU_2

        self.image.fill(self.color2)
        self.image.fill(self.color1, self.button)

    def update(self):
        self.image.fill(self.color2)
        self.image.fill(self.color1, self.button)

        #Update message
        self.textHeight = 0
        self.textWidth = 0

        for line in self.lines:
            line.printedLine = self.msgFont.render(line.text, True, COLOR_MENU_FONTS)
            self.textHeight += line.printedLine.get_height()
            if line.printedLine.get_width() > self.textWidth:
                self.textWidth = line.printedLine.get_width()

        #Get each line position
        numberLine = len(self.lines)
        count = 0
        for line in self.lines:
            line.position = [(self.image.get_width() - self.textWidth) * 0.5,
                        (self.image.get_height() - self.textHeight) * 0.5 + self.textHeight * (count / numberLine)]
        for line in self.lines:
            self.image.blit(line.printedLine, line.position)
    def addLine(self):
        pass