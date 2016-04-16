import pygame
import os
from app.settings import *

from app.sprites.pet.pet import Pet

class Tiger(Pet):
    def __init__(self):
        super().__init__()

        self.type = TIGER
        self.name = 'tiger'
