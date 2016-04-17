import pygame
import os
from app.settings import *

from app.sprites.pet.pet import Pet

class Tiger(Pet):
    def __init__(self):
        super().__init__()

        self.type = TIGER
        self.name = 'tiger'

        self.image = pygame.image.load(os.path.join('img', 'tigre.png'))
        self.image = pygame.transform.scale(self.image, (200, 200))

        #Set wanted height
        self.imagePrintedHeight = 300
        self.scalingDim(self.imagePrintedHeight)

        self.image = pygame.transform.scale(self.image, (int(self.imagePrintedWidth), int(self.imagePrintedHeight)))
