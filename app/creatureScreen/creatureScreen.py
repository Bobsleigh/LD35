from app.creatureScreen.eventHandlerCreatureScreen import EventHandlerCreatureScreen
from app.menuPause.menuPause import MenuPause
from app.settings import *

import pygame

class CreatureScreen:
    def __init__(self, screen, gameData):
        self.screen = screen
        self.gameData = gameData
        self.eventHandler = EventHandlerCreatureScreen()

        self.nextScene = None

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
        pygame.display.flip()

    def close(self):
        self.sceneRunning = False #To stop creatureScreen running

    def backToMain(self):
        self.nextScene = TITLE_SCREEN
        self.menuPause.close()
        self.close()