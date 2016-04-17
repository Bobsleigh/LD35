import pygame
from app.settings import *

class LogicHandlerPetScreen:
    def __init__(self,gameData,data):

        self.sceneRunning = True
        self.gameData = gameData
        self.screenData = data

        #to change pet
        self.nextPet = None

        #Set Link
        self.screenData.cupcake.linkList.append([RABBIT,TIGER])
        self.screenData.cupcake.linkList.append([TIGER,UNICORN])
        self.screenData.cupcake.linkList.append([UNICORN, DRAGON])

        self.screenData.goldBar.linkList.append([RABBIT, DRAGON])



    def logicHandle(self):

        self.screenData.allSprites.update()

    # Get rabbit back
    def getRabbit(self):
        self.screenData.messageLog.message = 'You killed your ' + self.gameData.myPet.name + ' and took another rabbit.'
        nextPet = RABBIT
        self.updatePet(nextPet)

    def updatePet(self, nextPet):
        self.screenData.allSprites.remove(self.gameData.myPet)
        self.gameData.myPet.changePet(nextPet)
        self.screenData.allSprites.add(self.gameData.myPet)

    def giveCupcake(self):
        self.give(self.screenData.cupcake)

    def giveGoldBar(self):
        self.give(self.screenData.goldBar)

    def giveHorseshoe(self):
        self.give(self.screenData.horseshoe)

    def give(self, givenItem):
        item = givenItem
        if self.gameData.inventory[item.cle] == 0:
            self.screenData.messageLog.message = 'You\'re out of ' + item.name + '!'
        elif self.gameData.inventory[item.cle] > 0:
            self.gameData.inventory[item.cle] += -1

            for parent in item.linkList:
                if self.gameData.myPet.type == parent[0]:
                    self.screenData.allSprites.add(self.gameData.myPet)
                    nextPet = parent[1]
                    self.updatePet(nextPet)
                    self.screenData.messageLog.message = 'You got a ' + self.gameData.myPet.name + '!'
                    break
                else:
                    self.nothingHappened()

    def nothingHappened(self):
        self.screenData.messageLog.message = 'Nothing happened.'
