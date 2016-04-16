import pygame

from app.mapData import MapData
from app.menuPause.menuPause import MenuPause
from app.scene.platformScreen.eventHandlerPlatformScreen import EventHandlerPlatformScreen
from app.scene.platformScreen.logicHandlerPlatformScreen import LogicHandlerPlatformScreen
from app.settings import *
from app.sprites.playerPlatform import PlayerPlatform


class PlatformScreen:
    def __init__(self, screen, gameData):
        self.screen = screen
        self.gameData = gameData


        self.nextScene = None

        #For testing
        self.mapData = MapData("Map_02")

        # Set the Player
        self.player = PlayerPlatform(540, 445)

        #Set Handlers
        self.eventHandler = EventHandlerPlatformScreen(self.player)
        self.logicHandler = LogicHandlerPlatformScreen(self.mapData)

        #Menu
        self.menuPause = MenuPause(screen, self.backToMain)
        self.eventHandler.menuPause = self.menuPause

        self.mapData.allSprites.add(self.player)
        self.mapData.camera.add(self.player)
        self.camera = self.mapData.camera

    def mainLoop(self):
        self.sceneRunning = True
        while self.sceneRunning:
            self.eventHandler.eventHandle()
            self.logicHandler.logicHandle()
            self.draw()

    def draw(self):
        self.camera.center(self.player.rect.center)
        self.camera.draw(self.screen)
        # self.mapData.spritesHUD.draw(self.screen)
        pygame.display.flip()

    def close(self):
        self.sceneRunning = False

    def backToMain(self):
        self.nextScene = TITLE_SCREEN
        self.menuPause.close()
        self.close()