#Imports
import pygame
import sys

from app.menuPause.eventHandlerMenuPause import EventHandlerMenuPause
from app.menu.menu import Menu
from app.settings import *

class MenuPause():
    def __init__(self, screen,backToMain,backToWorldMap = None):

        self.screen = screen

        # Menu
        self.menuPause = Menu(
                              pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
        self.menuPause.addOption('Resume', self.close)

        if backToWorldMap != None:
            self.menuPause.addOption('Back to world map', backToWorldMap)

        self.menuPause.addOption('Back to title screen', backToMain)
        self.menuPause.addOption('Exit', sys.exit)

        self.eventHandler = EventHandlerMenuPause()

        # some sound
        soundUnPause = pygame.mixer.Sound('music_pcm/unpause.wav')
        soundUnPause.set_volume(.4)
        self.menuPause.optionList[0].soundSelect = soundUnPause
        self.menuPause.optionList[1].soundSelect = soundUnPause
        self.menuPause.optionList[2].soundSelect = soundUnPause

    def mainLoop(self):
        self.menuRunning = True

        # some sound
        soundPause = pygame.mixer.Sound('music_pcm/pause.wav')
        soundPause.set_volume(.4)
        soundPause.play(0)

        while self.menuRunning:
            self.eventHandler.eventHandle(self.menuPause.optionList, self.menuPause.selector, self.close)
            self.menuPause.spritesMenu.update()  # This would be in the logic
            self.draw()  # Drawer in THIS file, below

    def draw(self):
        self.menuPause.spritesMenu.draw(self.screen)

        pygame.display.flip()

    def close(self):

        self.menuRunning = False
