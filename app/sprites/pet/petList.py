from app.sprites.pet.rabbit import Rabbit
from app.sprites.pet.tiger import Tiger
from app.sprites.pet.unicorn import Unicorn
from app.sprites.pet.dragon import Dragon

import pygame
import os
from app.settings import *

from app.sprites.pet.pet import Pet

class petList
    def __init__(self):

        #petList
        self.petTypeList = []
        self.petTypeList.append([RABBIT, Rabbit()])
        self.petTypeList.append([TIGER, Tiger()])
        self.petTypeList.append([UNICORN, Unicorn()])
        self.petTypeList.append([DRAGON, Dragon()])

        self.addPet(RABBIT,'rabbit',pygame.image.load(os.path.join('img', 'lapin.png')),250)

    def addPet(self,petType,name,image,printedHeight):
        self.petTypeList.append(Pet(petType,name,image,printedHeight))

        self.image = pygame.image.load(os.path.join('img', 'lapin.png'))

        # Set wanted height
        self.imagePrintedHeight = 250
        self.scalingDim(self.imagePrintedHeight)

        self.image = pygame.transform.scale(self.image, (int(self.imagePrintedWidth), int(self.imagePrintedHeight)))
