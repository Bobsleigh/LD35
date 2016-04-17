import pygame
from app.settings import *

class LogicHandlerPetScreen:
    def __init__(self,gameData,data):

        self.sceneRunning = True
        self.gameData = gameData
        self.screenData = data

        #Set Link
        self.screenData.cupcake.linkList.append(['rabbit','rainbowRabbit'])
        self.screenData.goldBar.linkList.append(['rabbit','tigerRabbit'])

        #Test link
        self.screenData.cupcake.linkList.append(['unicorn', 'dragonUnicorn'])

        self.screenData.goldBar.linkList.append(['unicorn', 'pimpUnicorn'])

        self.screenData.horseshoe.linkList.append(['dragonUnicorn', 'dragon'])


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
        self.give(self.screenData.cupcake)

    def giveGoldBar(self):
        self.give(self.screenData.goldBar)

    def giveHorseshoe(self):
        self.give(self.screenData.horseshoe)

    def give(self, givenItem):
        item = givenItem
        if self.gameData.inventory[item.key] == 0:
            self.screenData.messageLog.message = 'You\'re out of ' + item.name + '!'
        elif self.gameData.inventory[item.key] > 0:
            self.gameData.inventory[item.key] += -1

            for link in item.linkList:
                if self.gameData.myPet.key == link[0]:
                    self.updatePet(link[1])
                    self.screenData.messageLog.message = 'You got a ' + self.gameData.myPet.name + '!'
                    break

                else:
                    self.nothingHappened()

    def nothingHappened(self):
        self.screenData.messageLog.message = 'Nothing happened.'
