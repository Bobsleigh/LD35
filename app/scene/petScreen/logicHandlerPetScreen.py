import pygame
from app.settings import *

class LogicHandlerPetScreen:
    def __init__(self,gameData,data):

        self.sceneRunning = True
        self.gameData = gameData
        self.data = data


    def logicHandle(self):

        self.data.allSprites.update()

    # place temporaire
    def giveApple(self):
        if self.gameData.inventory["apple"] > 0:
            self.gameData.inventory["apple"] += -1

            if self.gameData.myPet == RABBIT:
                self.gameData.myPet = TIGER

            else:
                self.nothingHappened()

    def nothingHappened(self):
        self.text = pygame.font.SysFont(FONT_NAME, 50)
        self.data.messageLog.message = 'Nothing happened.'