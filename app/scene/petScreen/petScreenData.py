import pygame

from app.settings import *

from app.messageBox import MessageBox

class PetScreenData:
    def __init__(self,gameData):
        self.gameData = gameData
        self.allSprites = pygame.sprite.Group()

        self.messageLog = MessageBox(2*SCREEN_WIDTH/3,SCREEN_HEIGHT/9,SCREEN_WIDTH/2,8*SCREEN_HEIGHT/9)
        self.messageLog.textList.append('Your pet is hungry. Get him something.')
        self.allSprites.add(self.messageLog)  # Add sprite

        #All item
        self.itemInfoList = gameData.itemInfoList

        #For testing purpose
        for item in self.gameData.itemInfoList.item:
            self.gameData.itemInfoList.item[item].unlock = True
            self.itemInfoList.item[item].inventory = 10
        #self.gameData.itemInfoList.item['apple'].unlock = True
        #self.gameData.itemInfoList.item['carrot'].unlock = True

        #All pet
        self.petTypeList = gameData.petList
