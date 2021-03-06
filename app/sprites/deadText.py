import pygame
import os

class DeadText(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.name = "deadText"

        self.image = pygame.image.load(os.path.join('img', 'dead.png'))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        self.isGravityApplied = False
        self.isCollisionApplied = False