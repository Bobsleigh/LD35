import pygame
import os

from app.settings import *


class Item(pygame.sprite.Sprite):
    def __init__(self,key):
        super().__init__()

        self.key = key
        self.name = key

        self.image = pygame.image.load(os.path.join('img', 'cochon.png'))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (2 * SCREEN_WIDTH / 5, 2 * SCREEN_HEIGHT / 3)

        self.imagePrintedWidth = self.rect.width
        self.imagePrintedHeight = self.rect.height

        self.linkList = []

    def update(self):
        pass


