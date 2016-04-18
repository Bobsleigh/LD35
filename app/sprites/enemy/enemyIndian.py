import math
import os
from app.sprites.enemy.enemy import Enemy
import random
from app.bullet import SpiritBullet
from app.settings import *


class EnemyIndian(Enemy):
    def __init__(self, xCenter, yCenter, theMap, radius=50):
        super().__init__(xCenter, yCenter, os.path.join('img', 'EnemyIndian75.png'))

        self.name = "enemyIndian"

        self.rect = self.image.get_rect()

        self.xCenter = xCenter
        self.yCenter = yCenter

        self.angleBase = 2 * math.pi / 100
        self.angleDir = self.angleBase
        self.angle = 0

        self.initx = self.xCenter + radius
        self.inity = self.yCenter

        self.theMap = theMap

        self.rect.x = self.initx
        self.rect.y = self.inity

        self.imageIterShoot = random.randint(10,70)
        self.imageWaitNextShoot = 80

        self.direction = "Right"

    def setRadius(self, radius):
        self.initx = self.xCenter + radius

    def setAngleDirection(self, factor):
        if factor == 1:
            self.angleDir = self.angleBase
        elif factor == -1:
            self.angleDir = -self.angleBase

    def update(self):
        self.setRandomDirection()
        self.angle = (self.angle - self.angleDir) % (2 * math.pi)
        self.rect.x = self.xCenter + (self.initx - self.xCenter) * math.cos(self.angle) \
            + (self.inity - self.yCenter) * math.sin(self.angle)
        self.rect.y = self.yCenter - (self.initx - self.xCenter) * math.sin(self.angle) \
            + (self.inity - self.yCenter) * math.cos(self.angle)

        self.imageIterShoot += 1
        if self.imageIterShoot > self.imageWaitNextShoot:

            if self.direction == "Right":
                bullet = SpiritBullet(self.rect.x + self.rect.width + 1, self.rect.centery, RIGHT, False)
            elif self.direction == "Left":
                bullet = SpiritBullet(self.rect.x - 1, self.rect.centery, LEFT, False)

            self.theMap.camera.add(bullet)
            self.theMap.allSprites.add(bullet)
            self.theMap.enemyBullet.add(bullet)

            self.imageIterShoot = 0

    def setRandomDirection(self):
        dummy = random.randint(1,2)
        if dummy == 1:
            self.direction = "Right"
        else:
            self.direction = "Left"

    def dead(self):
        self.soundDead.play()
        self.kill()