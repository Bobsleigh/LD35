import os
import sys

import pygame

from app.scene.platformScreen.platformScreen import PlatformScreen
from app.settings import *
# from app.titleScreen.titleScreen import TitleScreen
from app.scene.sceneHandler import SceneHandler
from app.gameData import GameData
from app.mapData import MapData


if __name__ == '__main__':
    #Code to check if the code is running from a PyInstaller --onefile .exe
    if getattr(sys, 'frozen', False):
        os.chdir(sys._MEIPASS)

    # Init
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    pygame.font.init()

    # Screen
    screenSize = (SCREEN_WIDTH, SCREEN_HEIGHT)
    screen = pygame.display.set_mode(screenSize)

    #icon = pygame.transform.scale(pygame.image.load(os.path.join('img', 'player_triangle_v1.png')), (TILEDIMX, TILEDIMY))
    #pygame.display.set_icon(icon)
    pygame.display.set_caption("I want my dragon!")


    # Setup with gameData and the first scene
    sceneHandler = SceneHandler(screen)
    # we short cut
    sceneHandler.gameData.mapData = MapData("LevelSheriff", "StartPointSheriff")
    platformScene = PlatformScreen(screen, sceneHandler.gameData)
    sceneHandler.gameData.scene = platformScene
    sceneHandler.runningScene = platformScene

    sceneHandler.mainLoop()