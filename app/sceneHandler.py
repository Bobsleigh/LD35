from app.settings import *
from app.titleScreen.titleScreen import TitleScreen
from app.petScreen.petScreen import PetScreen
from app.gameData import GameData


class SceneHandler():
    def __init__(self, screen, firstScene):

        self.handlerRunning = True
        self.runningScene = firstScene
        self.screen = screen
        self.gameData = GameData()

    def mainLoop(self):
        self.handlerRunning = True
        while self.handlerRunning:
            self.runningScene.mainLoop()

            #When we exit the scene, this code executes
            if self.runningScene.nextScene == TITLE_SCREEN:
                self.runningScene = TitleScreen(self.screen)
            elif self.runningScene.nextScene == PET_SCREEN:
                self.runningScene = PetScreen(self.screen,self.gameData)

