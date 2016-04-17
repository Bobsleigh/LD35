import pygame

from app.settings import *


class Pet(pygame.sprite.Sprite):
    def __init__(self,key,image,height):
        super().__init__()

        self.key = key
        self.name = key

        self.image = image
        self.rect = self.image.get_rect()
        self.rect.midbottom = (2*SCREEN_WIDTH / 5,2*SCREEN_HEIGHT / 3)

        #image dimension
        self.imagePrintedHeight = height
        self.scalingDim(self.imagePrintedHeight)
        self.image = pygame.transform.scale(self.image, (int(self.imagePrintedWidth), int(self.imagePrintedHeight)))

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.midbottom = (SCREEN_WIDTH / 3, 2 * SCREEN_HEIGHT / 3)

    def scalingDim(self,height):
        self.update()
        self.imagePrintedWidth = self.image.get_width() * height / self.image.get_height()
