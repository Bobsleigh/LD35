import pygame
from app.tools.functionTools import *

class EventHandlerPlatformScreen():
    def __init__(self, player):
        self.menuPause = None
        self.player = player

    def eventHandle(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.menuPause.mainLoop()
                elif event.key == pygame.K_ESCAPE:
                    self.menuPause.mainLoop()
                elif event.key == pygame.K_RIGHT:
                    self.player.updateSpeedRight()
                elif event.key == pygame.K_LEFT:
                    self.player.updateSpeedLeft()
                elif event.key == pygame.K_UP:
                    self.player.updateSpeedUp()
                elif event.key == pygame.K_DOWN:
                    self.player.updateSpeedDown()
