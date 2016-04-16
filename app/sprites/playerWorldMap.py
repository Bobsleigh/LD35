__author__ = 'Bobsleigh'

import pygame
import os

from app.settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.name = "player"

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        #Tile Coordinates
        self.tileX = x * TILE_WIDTH
        self.tileY = y * TILE_HEIGHT

    def update(self):
        self.capSpeed()
        self.rect.x = self.tileX * TILE_WIDTH
        self.rect.y = self.tileY * TILE_HEIGHT

    def moveRight(self):
        self.tileX += 1
        self.facingSide = RIGHT

    def moveLeft(self):
        self.tileX -= 1
        self.facingSide = LEFT

    def moveUp(self):
        self.tileY -= 1
        self.facingSide = UP

    def moveDown(self):
        self.tileY += 1
        self.facingSide = DOWN