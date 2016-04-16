from app.scene.worldMap.eventHandlerWorldMap import EventHandlerWorldMap
from app.scene.worldMap.logicHandlerWorldMap import LogicHandlerWorldMap

from app.mapData import MapData
from app.scene.drawer import Drawer
from app.settings import *
from app.sprites.playerWorldMap import Player


class WorldMap:
    def __init__(self, screen, gameData):
        # Écran
        self.screen = screen

        #Map : HardCoded
        self.mapData = MapData("theme_v2.tmx")
        self.gameMemory = gameData

        # TODO: See where to put player. In mapData? But he will reset with each map change..?
        self.player = Player(600, 600)

        self.mapData.allSprites.add(self.player)
        self.mapData.camera.add(self.player)
        self.camera = self.mapData.camera

        # Handler
        self.eventHandlerWorldMap = EventHandlerWorldMap()
        self.logicHandler = LogicHandlerWorldMap(self.mapData)
        self.drawer = Drawer()

        self.nextScene = None

        #Menu
        # self.menuPause = MenuPause(screen,self.backToMain)
        # self.eventHandlerWorldMap.menuPause = self.menuPause

    def mainLoop(self):
        self.sceneRunning = True
        while self.sceneRunning:
            self.eventHandlerWorldMap.eventHandle(self.player)

            self.logicHandler.handle(self.player, self.gameMemory)
            # self.checkNewMap(self.logicHandler.newMap)

            self.drawer.draw(self.screen, self.mapData.camera, self.mapData.spritesHUD, self.player)

        if self.nextScene == None:
            self.nextScene = self.logicHandler.endState


    def checkNewMap(self, newMap):
        if newMap is not None:
            self.changeMap(newMap)

    # def changeMap(self, newMap):
    #
    #         self.player.rect.x = self.logicHandler.spawmPointPlayerx
    #         self.player.rect.y = self.logicHandler.spawmPointPlayery
    #
    #         self.mapData = newMap
    #         self.mapData.allSprites.add(self.player)
    #         self.mapData.camera.add(self.player)
    #
    #         self.gameMemory.enteringMap(self.mapData)
    #         self.gameMemory.updateMap(self.mapData)
    #
    #         self.eventHandlerWorldMap.newMap(self.mapData)
    #         self.eventHandlerWorldMap.eventHandlerPlayer.soundControllerPlayer = self.mapData.soundController
    #
    #         self.logicHandler.mapData = self.mapData
    #         self.logicHandler.collisionChecker.soundControl = self.mapData.soundController
    #         self.logicHandler.newMap = None

    def close(self):
        self.eventHandlerWorldMap.sceneRunning = False #To stop game running

    def backToMain(self):
        self.nextScene = TITLE_SCREEN
        self.menuPause.close()
        self.close()