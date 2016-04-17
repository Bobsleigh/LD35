import pygame
import os
from app.settings import *

from app.sprites.pet.pet import Pet

class Dragon(Pet):
    def __init__(self):
        super().__init__()

        self.type = DRAGON
        self.name = 'dragon'


        # Set wanted height
        self.imagePrintedHeight = 500
        self.scalingDim(self.imagePrintedHeight)

        self.image = pygame.transform.scale(self.image, (int(self.imagePrintedWidth), int(self.imagePrintedHeight)))