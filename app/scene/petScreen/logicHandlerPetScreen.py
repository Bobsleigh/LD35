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
