#from app.MenuPause import MenuPause
#from app.drawing.drawerGame import DrawerGame
#from app.event.eventHandlerFactory import EventHandlerFactory
#from app.logic.logicHandler import LogicHandler
#from app.map.gameMemory import GameMemory
#from app.map.mapData import MapData
from app.sprites.playerWorldMap import Player
from app.worldMap.eventHandlerWorldMap import EventHandlerWorldMap
from app.worldMap.drawerWorldMap import DrawerWorldMap
from app.settings import *


class WorldMap:
    def __init__(self, screen):
        # Écran
        self.screen = screen

        #Map : HardCoded
        self.mapData = MapData("Map_01")
        self.gameData = GameMemory()

        # TODO: See where to put player. In mapData? But he will reset with each map change..?
        self.player = Player(540, 445)

        self.mapData.allSprites.add(self.player)
        self.mapData.camera.add(self.player)
        self.camera = self.mapData.camera

        # Handler
        self.eventHandlerGame = self.eventHandlerWorldMap.create(self.screenType, self.camera, self.mapData)
        self.logicHandler = LogicHandler(self.mapData)
        self.drawer = DrawerWorldMap()

        self.nextScene = None

        #Menu
        self.menuPause = MenuPause(screen,self.backToMain)
        self.eventHandlerGame.menuPause = self.menuPause

    def mainLoop(self):
        self.sceneRunning = True
        while self.sceneRunning:
            self.sceneRunning = self.eventHandlerGame.sceneRunning and self.logicHandler.sceneRunning
            self.eventHandlerGame.handle()
            self.sceneRunning = self.eventHandlerGame.sceneRunning and self.logicHandler.sceneRunning

            self.logicHandler.handle(self.player, self.gameMemory)
            self.checkNewMap(self.logicHandler.newMap)

            self.drawer.draw(self.screen, self.mapData.camera, self.mapData.spritesHUD, self.player)

        if self.nextScene == None:
            self.nextScene = self.logicHandler.endState


    def checkNewMap(self, newMap):
        if newMap is not None:
            self.changeMap(newMap)

    def changeMap(self, newMap):

            self.player.rect.x = self.logicHandler.spawmPointPlayerx
            self.player.rect.y = self.logicHandler.spawmPointPlayery

            self.mapData = newMap
            self.mapData.allSprites.add(self.player)
            self.mapData.camera.add(self.player)

            self.gameMemory.enteringMap(self.mapData)
            self.gameMemory.updateMap(self.mapData)

            self.eventHandlerGame.newMap(self.mapData)
            self.eventHandlerGame.eventHandlerPlayer.soundControllerPlayer = self.mapData.soundController

            self.logicHandler.mapData = self.mapData
            self.logicHandler.collisionChecker.soundControl = self.mapData.soundController
            self.logicHandler.newMap = None

    def close(self):
        self.eventHandlerGame.sceneRunning = False #To stop game running

    def backToMain(self):
        self.nextScene = TITLE_SCREEN
        self.menuPause.close()
        self.close()