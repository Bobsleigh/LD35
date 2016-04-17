import pygame
import os

from app.settings import *


class Pet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.type = None
        self.name = None

        self.image = pygame.image.load(os.path.join('img', 'cochon.png'))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (2*SCREEN_WIDTH / 5,2*SCREEN_HEIGHT / 3)

        self.imagePrintedWidth = self.rect.width
        self.imagePrintedHeight = self.rect.height

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.midbottom = (SCREEN_WIDTH / 3, 2 * SCREEN_HEIGHT / 3)

    def scalingDim(self,height):
        self.update()
        self.imagePrintedWidth = self.image.get_width() * height / self.image.get_height()
