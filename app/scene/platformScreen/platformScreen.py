import pygame

from app.mapData import MapData
from app.menuPause.menuPause import MenuPause
from app.scene.platformScreen.eventHandlerPlatformScreen import EventHandlerPlatformScreen
from app.scene.platformScreen.logicHandlerPlatformScreen import LogicHandlerPlatformScreen
from app.scene.drawer import Drawer
from app.settings import *
from app.sprites.playerPlatform import PlayerPlatform


class PlatformScreen:
    def __init__(self, screen, gameData):
        self.screen = screen
        self.gameData = gameData
        self.nextScene = None


        #For testing
        # TODO: BP need to set up things / position of the player and name of the map / use self.gameData BP
        self.mapData = MapData("Map_01")
        # Set the Player
        self.player = PlayerPlatform(300, 300)

        self.mapData.allSprites.add(self.player)
        self.mapData.camera.add(self.player)
        self.camera = self.mapData.camera

        self.eventHandler = EventHandlerPlatformScreen(self.player)
        self.logicHandler = LogicHandlerPlatformScreen(self.mapData)
        self.drawer = Drawer()

        #Menu
        self.menuPause = MenuPause(screen, self.backToMain)
        self.eventHandler.menuPause = self.menuPause


    def mainLoop(self):

        self.sceneRunning = True
        while self.sceneRunning:
            self.eventHandler.eventHandle()
            self.logicHandler.handle(self.player, self.mapData)
            self.drawer.draw(self.screen, self.mapData.camera, self.mapData.spritesHUD, self.player)

    def close(self):
        self.sceneRunning = False

    def backToMain(self):
        self.nextScene = TITLE_SCREEN
        self.menuPause.close()
        self.close()
