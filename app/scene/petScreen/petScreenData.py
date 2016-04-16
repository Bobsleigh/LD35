import pygame
from app.settings import *

from app.messageBox import MessageBox

class PetScreenData:
    def __init__(self):
        self.allSprites = pygame.sprite.Group()

        self.messageLog = MessageBox('Your pet is hungry',SCREEN_WIDTH/2,SCREEN_WIDTH/10,SCREEN_WIDTH/2,8*SCREEN_HEIGHT/9)
        self.allSprites.add(self.messageLog)  # Add sprite

