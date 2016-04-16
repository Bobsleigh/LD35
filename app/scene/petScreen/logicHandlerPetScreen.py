import pygame
from app.settings import *

class LogicHandlerPetScreen:
    def __init__(self,gameData,data):

        self.sceneRunning = True
        self.gameData = gameData
        self.data = data


    def logicHandle(self):

        self.data.allSprites.update()

    #Get rabbit back
    def getRabbit(self):

        self.data.messageLog.message = 'You cooked your ' + self.gameData.myPet.name + ' and took another rabbit.'
        self.gameData.myPet.type = RABBIT
        self.updatePet()

    #Update pet
    def updatePet(self):
        for petType in self.gameData.petTypeList:
            if self.gameData.myPet.type == petType[0]:
                self.gameData.myPet = petType[1]

    #Place temporaire?
    def giveApple(self):
        if self.gameData.inventory["apple"] == 0:
            self.data.messageLog.message = 'You\'re out of apple.'
        elif self.gameData.inventory["apple"] > 0:
            self.gameData.inventory["apple"] += -1

            if self.gameData.myPet.type == RABBIT:
                self.gameData.myPet.type = TIGER
                self.updatePet()
                self.data.messageLog.message = 'You got a ' + self.gameData.myPet.name + '!'

            else:
                self.nothingHappened()

    def nothingHappened(self):
        self.data.messageLog.message = 'Nothing happened.'