import pygame
import os

from app.sprites.enemy.enemy import Enemy
from app.bullet import HeartBullet
from app.settings import *
import random


class EnemySaloon(Enemy):
    def __init__(self, x, y, theMap, direction="Right"):
        super().__init__(x, y)

        self.name = "enemySaloon"

        self.imageEnemyLeft = pygame.image.load(os.path.join('img', 'FrenchCancan75.png'))
        self.imageEnemyRight = pygame.transform.flip(pygame.image.load(os.path.join('img', 'FrenchCancan75.png')), True, False)

        self.rect = self.imageEnemyLeft.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speedx = 0
        self.speedy = 0

        self.theMap = theMap

        self.setDirection(direction)

        self.isGravityApplied = True
        self.isCollisionApplied = True

        self.imageIterShoot = random.randint(10,70)
        self.imageWaitNextShoot = 80

    def setDirection(self, direction):
        self.direction = direction
        if self.direction == "Right":
            self.image = self.imageEnemyRight
        if self.direction == "Left":
            self.image = self.imageEnemyLeft

    def update(self):

        self.imageIterShoot += 1
        if self.imageIterShoot > self.imageWaitNextShoot:

            if self.direction == "Right":
                bullet = HeartBullet(self.rect.x + self.rect.width + 1, self.rect.centery, RIGHT, False)
                self.setDirection("Left")
            elif self.direction == "Left":
                bullet = HeartBullet(self.rect.x - 1, self.rect.centery, LEFT, False)
                self.setDirection("Right")

            self.theMap.camera.add(bullet)
            self.theMap.allSprites.add(bullet)
            self.theMap.enemyBullet.add(bullet)

            self.imageIterShoot = 0

        self.rect.x += self.speedx
        if self.speedy < 15:
            self.rect.y += self.speedy

    def dead(self):
        self.kill()