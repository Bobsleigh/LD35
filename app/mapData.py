import pygame
import pyscroll
import pytmx
import re
import pygame
from app.settings import *
import os

# from app.enemy.enemyFactory import EnemyFactory
# from app.powerup.powerUpFactory import PowerUpFactory
# from app.sound.soundPlayerController import *
from app.player import *

class MapData:
    def __init__(self, mapName="Map_01", screenSize=(SCREEN_WIDTH, SCREEN_HEIGHT)):

        self.nameMap = mapName

        self.tmxData = pytmx.util_pygame.load_pygame(self.reqImageName(self.nameMap))
        self.mapData = pyscroll.data.TiledMapData(self.tmxData)
        self.cameraPlayer = pyscroll.BufferedRenderer(self.mapData, screenSize, clamp_camera=True)
        # self.soundController = soundPlayerController()

        self.allSprites = pygame.sprite.Group()
        # self.enemyGroup = pygame.sprite.Group()
        # self.powerUpGroup = pygame.sprite.Group()
        # self.friendlyBullet = pygame.sprite.Group()
        # self.enemyBullet = pygame.sprite.Group()
        # self.spritesHUD = pygame.sprite.Group()

        # eFactory = EnemyFactory()
        # pUpFactory = PowerUpFactory()

        for object in self.tmxData.objects:
            # if object.type == "enemy":
            #     enemy = eFactory.create(object, self)
            #     self.allSprites.add(enemy)
            #     self.enemyGroup.add(enemy)

            # if object.type == "powerUp":
            #     powerUp = pUpFactory.create(object)
            #     self.allSprites.add(powerUp)
            #     self.powerUpGroup.add(powerUp)
            pass

        # TODO: Put camera in mapData
        self.camera = pyscroll.PyscrollGroup(map_layer=self.cameraPlayer, default_layer=SPRITE_LAYER)
        self.camera.add(self.allSprites)

    # Map names are "Map_XX" where XX is the number 01 to 99
    # Tiled names are "theme_vX.tmx" where X is the number 1 to 99
    def reqImageName(self, nameMap):
        numberOfTheMap = int((re.findall("\d+", nameMap))[0])
        return os.path.join('tiles_map', "theme_v" + str(numberOfTheMap) + ".tmx")
