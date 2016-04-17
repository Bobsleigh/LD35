import pygame
from app.settings import *

class LogicHandlerPetScreen:
    def __init__(self,gameData,data):

        self.sceneRunning = True
        self.gameData = gameData
        self.screenData = data
        self.updateFeedMenuPlease = False
        self.recreateFeedMenuPlease = False


    def logicHandle(self):

        self.screenData.allSprites.update()

    # Get rabbit back
    def getRabbit(self):
        self.screenData.messageLog.message = 'You killed your critter and took another rabbit.'
        self.updatePet('rabbit')

    def updatePet(self, nextPet):
        self.screenData.allSprites.remove(self.gameData.myPet)
        self.gameData.myPet = self.screenData.petTypeList.pet[nextPet]
        self.gameData.myPet.loadImage()
        if self.gameData.myPet.eventTrigger:
            self.checkTrigger()
        self.screenData.allSprites.add(self.gameData.myPet)

    def giveCupcake(self):
        self.give(self.gameData.itemInfoList.item["cupcake"].key)

    def giveGoldBar(self):
        self.give(self.gameData.itemInfoList.item["goldBar"].key)

    def giveHorseshoe(self):
        self.give(self.gameData.itemInfoList.item["horseshoe"].key)

    def giveBone(self):
        self.give(self.gameData.itemInfoList.item["bone"].key)

    def giveCarrot(self):
        self.give(self.gameData.itemInfoList.item["carrot"].key)

    def giveApple(self):
        self.give(self.gameData.itemInfoList.item["apple"].key)

    def giveGun(self):
        self.give(self.gameData.itemInfoList.item["gun"].key)

    def givePokerChip(self):
        self.give(self.gameData.itemInfoList.item["pokerChip"].key)

    def giveTotem(self):
        self.give(self.gameData.itemInfoList.item["totem"].key)


    def give(self, givenItem):
        item = givenItem
        if self.gameData.itemInfoList.item[item].inventory == 0:
            self.screenData.messageLog.message = 'You\'re out of ' + self.gameData.itemInfoList.item[item].name + '!'
        elif self.gameData.itemInfoList.item[item].inventory > 0:
            self.gameData.itemInfoList.item[item].inventory += -1
            self.updateFeedMenuPlease = True

            for link in self.gameData.itemInfoList.item[givenItem].linkList:
                if self.gameData.myPet.key == link[0]:
                    self.updatePet(link[1])
                    self.screenData.messageLog.message = 'You got a ' + self.gameData.myPet.name + '!'
                    break

                else:
                    self.nothingHappened()

    def nothingHappened(self):
        self.screenData.messageLog.line1 = 'Nothing happened.'

    def checkTrigger(self):
        if self.gameData.myPet.key == 'dog':
            self.obtain('carrot')
        if self.gameData.myPet.key == 'carrotRabbit':
            self.obtain('apple')
        if self.gameData.myPet.key == 'alienRabbit':
            self.unlockMap('map2')
        if self.gameData.myPet.key == 'muscularHorse':
            self.unlockMap('map3')
        if self.gameData.myPet.key == 'pimpUnicorn':
            self.unlockMap('map4')

    def obtain(self,key):
        if self.gameData.itemInfoList.item[key].unlock == False:
            self.gameData.itemInfoList.item[key].unlock = True

        self.gameData.itemInfoList.item[key].inventory += 4
        self.recreateFeedMenuPlease = True
        self.updateFeedMenuPlease = True

    def unlockMap(self,map):
        if self.gameData.mapUnlock[map] == False:
            self.gameData.mapUnlock[map] = True



