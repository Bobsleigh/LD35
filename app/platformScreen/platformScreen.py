from app.platformScreen.eventHandlerPlatformScreen import EventHandlerPlatformScreen
from app.menuPause.menuPause import MenuPause
from app.settings import *

import pygame

class PlatformScreen:
    def __init__(self, screen, gameData):
        self.screen = screen
        self.gameData = gameData
        self.eventHandler = EventHandlerPlatformScreen()

        self.nextScene = None

        #Menu
        self.menuPause = MenuPause(screen, self.backToMain)
        self.eventHandler.menuPause = self.menuPause

        #For testing
        self.screen.fill((255,255,255))


    def mainLoop(self):
        self.sceneRunning = True
        while self.sceneRunning:
            self.eventHandler.eventHandle()
            self.draw()

    def draw(self):
        self.screen.fill((255,255,255))
        pygame.display.flip()

    def close(self):
        self.sceneRunning = False

    def backToMain(self):
        self.nextScene = TITLE_SCREEN
        self.menuPause.close()
        self.close()