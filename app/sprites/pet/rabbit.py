import pygame
import os
from app.settings import *

from app.sprites.pet.pet import Pet
from app.sprites.pet.tiger import Tiger

class Rabbit(Pet):
    def __init__(self):
        super().__init__()

        self.name = RABBIT