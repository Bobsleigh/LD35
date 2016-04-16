import pygame
from app.settings import *


#For a very short message only

class MessageBox(pygame.sprite.Sprite):
    def __init__(self, message, width, height, centerx, centery):
        super().__init__()

        self.msgFont = pygame.font.SysFont(FONT_NAME, 30)
        self.message = message
        self.printedMessage = self.msgFont.render(self.message, True, COLOR_MENU_FONTS)

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
        self.printedMessage = self.msgFont.render(self.message, True, COLOR_MENU_FONTS)

        self.textPos = [(self.image.get_width() - self.printedMessage.get_width()) * 0.5,
                        (self.image.get_height() - self.printedMessage.get_height()) * 0.5]
        self.image.blit(self.printedMessage, self.textPos)
