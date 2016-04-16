__author__ = 'Bobsleigh'

from app.settings import *
from app.titleScreen.titleScreen import TitleScreen
from app.creatureScreen.creatureScreen import CreatureScreen


class SceneHandler():
    def __init__(self, screen, firstScene):

        self.handlerRunning = True
        self.runningScene = firstScene
        self.screen = screen

    def mainLoop(self):
        self.handlerRunning = True
        while self.handlerRunning:
            self.runningScene.mainLoop()

            #When we exit the scene, this code executes
            if self.runningScene.nextScene == TITLE_SCREEN:
                self.runningScene = TitleScreen(self.screen)
            elif self.runningScene.nextScene == CREATURE_SCREEN:
                self.runningScene = CreatureScreen(self.screen)
                self.runningScene.mainLoop()

