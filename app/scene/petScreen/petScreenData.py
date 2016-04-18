import pygame

from app.settings import *

from app.messageBox import MessageBox

class PetScreenData:
    def __init__(self,gameData):
        self.gameData = gameData
        self.allSprites = pygame.sprite.Group()

        self.messageLog = MessageBox(3*SCREEN_WIDTH/4,SCREEN_HEIGHT/6,SCREEN_WIDTH/2,8*SCREEN_HEIGHT/9)
        self.messageLog.textList.append('Your pet is hungry. Get him something.')
        self.allSprites.add(self.messageLog)  # Add sprite

        #All item
        self.itemInfoList = gameData.itemInfoList

        # All pet
        self.petTypeList = gameData.petList

        # TODO: comment all following
        #or testing purpose
        #for item in self.gameData.itemInfoList.item:
        #    self.gameData.itemInfoList.item[item].unlock = True
        #    self.itemInfoList.item[item].inventory = 5
        # self.gameData.itemInfoList.item['apple'].unlock = False
        # self.gameData.itemInfoList.item['carrot'].unlock = False
        # self.gameData.itemInfoList.item['gun'].unlock = False
        # self.gameData.itemInfoList.item['pokerChip'].unlock = False
        # self.gameData.itemInfoList.item['totem'].unlock = False

        #for pet in self.gameData.petList.pet:
        #    if self.gameData.petList.pet[pet].key != 'unicorn':
        #        if self.gameData.petList.pet[pet].key != 'tiger':
        #            if self.gameData.petList.pet[pet].key != 'dragon':
        #                self.gameData.petList.pet[pet].found = True