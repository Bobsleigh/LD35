import pygame
from app.tools.functionTools import *

class EventHandlerWorldMap():
    def __init__(self):
        self.menuPause = None

    def eventHandle(self,player):
        for dummyEv in pygame.event.get():
            if dummyEv.type == pygame.QUIT:
                quitGame()

            elif dummyEv.type == pygame.KEYDOWN:
                if dummyEv.key == pygame.K_BACKSPACE:
                    self.menuPause.mainLoop()
                elif dummyEv.key == pygame.K_ESCAPE:
                    self.menuPause.mainLoop()
                elif dummyEv.key == pygame.K_RIGHT: #Does nothing for now...
                    player.moveRight()
                elif dummyEv.key == pygame.K_LEFT: #Does nothing for now...
                    player.moveLeft()
                elif dummyEv.key == pygame.K_UP:
                    player.moveUp()
                elif dummyEv.key == pygame.K_DOWN:
                    player.moveDown()
                elif dummyEv.key == pygame.K_SPACE:
                    pass
                elif dummyEv.key == pygame.K_RETURN:
                    pass
        pass
