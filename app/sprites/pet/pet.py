import pygame
import os

from app.settings import *


class Pet(pygame.sprite.Sprite):
    def __init__(self,key,printedName,imageName,height,kind=NORMAL,eventTrigger=False):
        super().__init__()

        self.key = key
        self.name = printedName

        self.image = pygame.Surface((1,1))

        self.imageName = imageName
        self.wantedHeight = height

        self.kind = kind
        self.eventTrigger = eventTrigger

        self.found = False

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.midbottom = (SCREEN_WIDTH / 3, 2 * SCREEN_HEIGHT / 3)

    def scalingDim(self,height):
        self.update()
        self.imagePrintedWidth = self.image.get_width() * height / self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(self.imagePrintedWidth), int(height)))

    def loadImage(self):
        self.image = pygame.image.load(os.path.join('img', self.imageName))
        self.scalingDim(self.wantedHeight)
