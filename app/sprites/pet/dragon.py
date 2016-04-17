import pygame
import os
from app.settings import *

from app.sprites.pet.pet import Pet

class Dragon(Pet):
    def __init__(self):
        super().__init__()

        self.type = DRAGON
        self.name = 'dragon'