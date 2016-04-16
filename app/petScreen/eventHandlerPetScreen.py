import pygame
from sys import exit

class EventHandlerPetScreen():
    def __init__(self):
        self.menuPause = None

    def eventHandle(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.menuPause.mainLoop()
                if event.key == pygame.K_ESCAPE:
                    self.menuPause.mainLoop()
