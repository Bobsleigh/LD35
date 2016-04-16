from app.petScreen.eventHandlerPetScreen import EventHandlerPetScreen
from app.menuPause.menuPause import MenuPause
from app.settings import *
from app.sprites.pet import Pet

import pygame

import os


class PetScreen:
    def __init__(self, screen, gameData):
        self.screen = screen
        self.gameData = gameData
        self.eventHandler = EventHandlerPetScreen()

        self.nextScene = None

        #All sprite
        self.allSprites = pygame.sprite.Group()

        self.pet = Pet(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        self.allSprites.add(self.pet )

        #Menu
        self.menuPause = MenuPause(screen,self.backToMain)
        self.eventHandler.menuPause = self.menuPause

        #For testing
        self.screen.fill((255,255,255))


    def mainLoop(self):
        self.sceneRunning = True
        while self.sceneRunning:
            self.eventHandler.eventHandle()
            self.draw()  # Drawer in THIS file, below

    def draw(self):
        self.screen.fill((255,255,255))
        self.allSprites.draw(self.screen)
        pygame.display.flip()

    def createPet(self):
        pass


    def close(self):
        self.sceneRunning = False #To stop creatureScreen running

    def backToMain(self):
        self.nextScene = TITLE_SCREEN
        self.menuPause.close()
        self.close()