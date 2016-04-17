import pygame
from app.settings import *

class LogicHandlerPetScreen:
    def __init__(self,gameData,data):

        self.sceneRunning = True
        self.gameData = gameData
        self.screenData = data


    def logicHandle(self):

        self.screenData.allSprites.update()

    # Get rabbit back
    def getRabbit(self):
        self.screenData.messageLog.message = 'You killed your ' + self.gameData.myPet.name + ' and took another rabbit.'
        self.updatePet('rabbit')

    def updatePet(self, nextPet):
        self.screenData.allSprites.remove(self.gameData.myPet)
        self.gameData.myPet = self.screenData.petTypeList.pet[nextPet]
        self.gameData.myPet.loadImage()
        self.screenData.allSprites.add(self.gameData.myPet)

    def giveCupcake(self):
        self.give(self.gameData.itemInfoList.item["cupcake"].key)

    def giveGoldBar(self):
        self.give(self.gameData.itemInfoList.item["goldBar"].key)

    def giveHorseshoe(self):
        self.give(self.gameData.itemInfoList.item["horseshoe"].key)

    def give(self, givenItem):
        item = givenItem
        if self.gameData.itemInfoList.item[item].inventory == 0:
            self.screenData.messageLog.message = 'You\'re out of ' + self.gameData.itemInfoList.item[item].inventory + '!'
        elif self.gameData.itemInfoList.item[item].inventory > 0:
            self.gameData.itemInfoList.item[item].inventory += -1

            for link in self.gameData.itemInfoList.item[givenItem].linkList:
                if self.gameData.myPet.key == link[0]:
                    self.updatePet(link[1])
                    self.screenData.messageLog.message = 'You got a ' + self.gameData.myPet.name + '!'
                    break

                else:
                    self.nothingHappened()

    def nothingHappened(self):
        self.screenData.messageLog.message = 'Nothing happened.'
