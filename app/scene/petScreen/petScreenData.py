import pygame

from app.settings import *
from app.scene.petScreen.item import Item
from app.sprites.pet.petList import PetList

from app.messageBox import MessageBox

class PetScreenData:
    def __init__(self,gameData):
        self.gameData = gameData
        self.allSprites = pygame.sprite.Group()

        self.messageLog = MessageBox('Your ' + self.gameData.myPet.name + ' is hungry.',2*SCREEN_WIDTH/3,SCREEN_HEIGHT/10,SCREEN_WIDTH/2,8*SCREEN_HEIGHT/9)
        self.allSprites.add(self.messageLog)  # Add sprite

        #All item
        self.itemInfoList = gameData.itemInfoList

        #All pet
        self.petTypeList = gameData.petList
