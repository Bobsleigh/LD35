import pygame
import os
import sys

from app.settings import *

from app.titleScreen.titleScreen import TitleScreen
from app.sceneHandler import SceneHandler



if __name__ == '__main__':
    #Code to check if the code is running from a PyInstaller --onefile .exe
    if getattr(sys, 'frozen', False):
        os.chdir(sys._MEIPASS)

    running = True
    while running:
    # Init
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()
        pygame.font.init()

        # Écran
        screenSize = (SCREEN_WIDTH, SCREEN_HEIGHT)
        screen = pygame.display.set_mode(screenSize)

        #icon = pygame.transform.scale(pygame.image.load(os.path.join('img', 'player_triangle_v1.png')), (TILEDIMX, TILEDIMY))
        #pygame.display.set_icon(icon)
        pygame.display.set_caption("I want my dragon!")

        titleScreen = TitleScreen(screen)

        sceneHandler = SceneHandler(screen, titleScreen)
        sceneHandler.mainLoop()