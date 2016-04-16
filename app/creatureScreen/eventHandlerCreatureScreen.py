import pygame
from sys import exit

class EventHandlerCreatureScreen():
    def __init__(self):
        pass

    def eventHandle(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
