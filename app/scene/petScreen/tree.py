import pygame
from app.settings import *

class Tree:
    def __init__(self,gameData,data):

        self.sceneRunning = True
        self.gameData = gameData
        self.screenData = data

        #to change pet
        self.nextPet = None

        #All item trigger list [parent,child]
        self.gameData.cupcake.linkList.append([RABBIT,TIGER])
        self.gameData.cupcake.linkList.append([TIGER, UNICORN])
        self.gameData.cupcake.linkList.append([UNICORN, DRAGON])


    #Get rabbit back
    def getRabbit(self):
        self.screenData.messageLog.message = 'You killed your ' + self.gameData.myPet.name + ' and took another rabbit.'
        self.nextPet = RABBIT
        self.updatePet()

    def updatePet(self):
        self.screenData.allSprites.remove(self.gameData.myPet)
        for petType in self.gameData.petTypeList:
            if self.nextPet == petType[0]:
                self.gameData.myPet = petType[1]
        self.screenData.allSprites.add(self.gameData.myPet)

        # Place temporaire?



    def giveCupcake(self):
        if self.gameData.inventory["cupcake"] == 0:
            self.screenData.messageLog.message = 'You\'re out of cupcake.'
        elif self.gameData.inventory["cupcake"] > 0:
            self.gameData.inventory["cupcake"] += -1

            for parent in self.gameData.cupcake.linkList:
                if self.gameData.myPet.type == parent[0]:
                    self.screenData.allSprites.add(self.gameData.myPet)
                    self.nextPet = parent[1]
                    self.updatePet()
                    self.screenData.messageLog.message = 'You got a ' + self.gameData.myPet.name + '!'
                    break
                else:
                    self.nothingHappened()

    def nothingHappened(self):
        self.screenData.messageLog.message = 'Nothing happened.'
