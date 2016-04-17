import pygame
import os

class Padlock(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.name = "Padlock"

        self.image = pygame.image.load(os.path.join('img', 'padlock.png'))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.isGravityApplied = False
        self.isCollisionApplied = False