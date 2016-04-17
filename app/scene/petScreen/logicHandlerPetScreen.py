import pygame
from app.settings import *

class LogicHandlerPetScreen:
    def __init__(self,gameData,data):

        self.sceneRunning = True
        self.gameData = gameData
        self.screenData = data

        #to change pet
        self.nextPet = None



    def logicHandle(self):

        self.screenData.allSprites.update()

    #Get rabbit back
    def getRabbit(self):
        self.screenData.messageLog.message = 'You cooked your ' + self.gameData.myPet.name + ' and took another rabbit.'
        self.nextPet = RABBIT
        self.updatePet()

    #Update pet
    def updatePet(self):
        self.screenData.allSprites.remove(self.gameData.myPet)
        for petType in self.gameData.petTypeList:
            if self.nextPet == petType[0]:
                self.gameData.myPet = petType[1]
        self.screenData.allSprites.add(self.gameData.myPet)

    #Place temporaire?
    def giveApple(self):
        if self.gameData.inventory["apple"] == 0:
            self.screenData.messageLog.message = 'You\'re out of apple.'
        elif self.gameData.inventory["apple"] > 0:
            self.gameData.inventory["apple"] += -1

            if self.gameData.myPet.type == RABBIT:
                self.screenData.allSprites.add(self.gameData.myPet)
                self.nextPet = TIGER
                self.updatePet()
                self.screenData.messageLog.message = 'You got a ' + self.gameData.myPet.name + '!'

            elif self.gameData.myPet.type == TIGER:
                self.screenData.allSprites.add(self.gameData.myPet)
                self.nextPet = DRAGON
                self.updatePet()
                self.screenData.messageLog.message = 'You got a ' + self.gameData.myPet.name + '!'

            else:
                self.nothingHappened()

    def nothingHappened(self):
        self.screenData.messageLog.message = 'Nothing happened.'