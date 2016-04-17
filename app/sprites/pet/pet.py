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

        self.petTypeList = []
        self.petTypeList.append([RABBIT])
        self.petTypeList.append([TIGER])
        self.petTypeList.append([UNICORN])
        self.petTypeList.append([DRAGON])

    def update(self):
        self.rect = self.image.get_rect()
        self.rect.midbottom = (SCREEN_WIDTH / 3, 2 * SCREEN_HEIGHT / 3)

    def scalingDim(self,height):
        self.update()
        self.imagePrintedWidth = self.image.get_width() * height / self.image.get_height()

    def changePet(self,nextPet):
        if nextPet == RABBIT:
            self.becomeRabbit()
        elif nextPet == TIGER:
            self.becomeTiger()
        elif nextPet == UNICORN:
            self.becomeUnicorn()
        elif nextPet == DRAGON:
            self.becomeDragon()


    def becomeRabbit(self):

        self.type = RABBIT
        self.name = 'rabbit'

        self.image = pygame.image.load(os.path.join('img', 'lapin.png'))

        # Set wanted height
        self.imagePrintedHeight = 250
        self.scalingDim(self.imagePrintedHeight)

        self.image = pygame.transform.scale(self.image, (int(self.imagePrintedWidth), int(self.imagePrintedHeight)))


    def becomeTiger(self):
        self.type = TIGER
        self.name = 'tiger'

        self.image = pygame.image.load(os.path.join('img', 'tigre.png'))

        # Set wanted height
        self.imagePrintedHeight = 275
        self.scalingDim(self.imagePrintedHeight)

        self.image = pygame.transform.scale(self.image, (int(self.imagePrintedWidth), int(self.imagePrintedHeight)))

    def becomeUnicorn(self):
        self.type = UNICORN
        self.name = 'unicorn'

        self.image = pygame.image.load(os.path.join('img', 'licorne.png'))

        # Set wanted height
        self.imagePrintedHeight = 350
        self.scalingDim(self.imagePrintedHeight)

        self.image = pygame.transform.scale(self.image, (int(self.imagePrintedWidth), int(self.imagePrintedHeight)))

    def becomeDragon(self):
        self.type = DRAGON
        self.name = 'dragon'

        self.image = pygame.image.load(os.path.join('img', 'dragon.png'))

        # Set wanted height
        self.imagePrintedHeight = 425
        self.scalingDim(self.imagePrintedHeight)

        self.image = pygame.transform.scale(self.image, (int(self.imagePrintedWidth), int(self.imagePrintedHeight)))
