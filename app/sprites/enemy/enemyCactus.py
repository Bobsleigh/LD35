import math
import pygame
import os

from app.sprites.enemy.enemy import Enemy
from app.settings import *


class EnemyCactus(Enemy):
    def __init__(self, x, y, direction="Right"):
        super().__init__(x, y, os.path.join('img', 'enemyCactus.png'))

        self.name = "enemyCactus"

        self.imageEnemy = pygame.image.load(os.path.join('img', 'enemyCactus.png'))

        self.initx = self.rect.x
        self.inity = self.rect.y

        self.speedBase = 1
        self.distanceMax = 200

        self.speedx = self.speedBase
        self.speedy = 0
        self.distance = 0

        self.direction = direction
        if self.direction == "Left":
            self.speedx = -self.speedBase
            self.image = self.imageEnemy

            self.isGravityApplied = True
            self.isCollisionApplied = True

    def set_direction(self, direction):
        self.direction = direction
        if self.direction == "Left":
            self.speedx = -self.speedBase
            self.image = self.imageEnemy
        if self.direction == "Right":
            self.speedx = self.speedbase
            self.image = self.imageEnemy

    def set_distance_max(self, distance):
        self.distanceMax = distance

    def update(self):

        if self.speedx == 0 or self.distance >= self.distanceMax:
            if self.direction == "Right":
                self.direction = "Left"
                self.speedx = -self.speedBase
            elif self.direction == "Left":
                self.direction = "Right"
                self.speedx = self.speedBase

        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # print(self.speedy)

        self.distance = math.fabs(self.initx - self.rect.x)