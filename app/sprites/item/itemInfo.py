import pygame
import os

from app.settings import *


class ItemInfo(pygame.sprite.Sprite):
    def __init__(self, key, imageNamePNG='cochon.png'):
        super().__init__()

        self.key = key
        self.name = key

        self.image = pygame.Surface((1, 1))
        self.imageNamePNG = imageNamePNG

        self.wantedHeight = 32

        self.inventory = 0
        self.unlock = False #Put false when done testing
        self.linkList = []


    def update(self):
        self.rect = self.image.get_rect()
        self.rect.midbottom = (SCREEN_WIDTH / 3, 2 * SCREEN_HEIGHT / 3)

    def scalingDim(self, height):
        self.update()
        self.imagePrintedWidth = self.image.get_width() * height / self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(self.imagePrintedWidth), int(self.wantedHeight)))

    def loadImage(self):
        self.image = pygame.image.load(os.path.join('img', self.imageName))
        self.scalingDim(self.wantedHeight)


