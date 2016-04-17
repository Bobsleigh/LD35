import pygame
import os
from app.settings import *

from app.sprites.pet.pet import Pet

class Unicorn(Pet):
    def __init__(self):
        super().__init__()

        self.type = UNICORN
        self.name = 'unicorn'

        self.image = pygame.image.load(os.path.join('img', 'licorne.png'))

        # Set wanted height
        self.imagePrintedHeight = 350
        self.scalingDim(self.imagePrintedHeight)

        self.image = pygame.transform.scale(self.image,(int(self.imagePrintedWidth),int(self.imagePrintedHeight)))