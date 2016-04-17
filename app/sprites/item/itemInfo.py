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
        pass


