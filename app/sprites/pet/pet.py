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
        self.rect.midbottom = (SCREEN_WIDTH / 3,2*SCREEN_HEIGHT / 3)
