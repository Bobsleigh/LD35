import pygame
import os
from app.settings import *

from app.sprites.pet.pet import Pet

class Rabbit(Pet):
    def __init__(self):
        super().__init__()

        self.type = RABBIT
        self.name = 'rabbit'

        self.image = pygame.image.load(os.path.join('img', 'lapin.png'))

        # Set wanted height
        self.imagePrintedHeight = 250
        self.scalingDim(self.imagePrintedHeight)

        self.image = pygame.transform.scale(self.image,(int(self.imagePrintedWidth),int(self.imagePrintedHeight)))