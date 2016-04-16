import pygame
import pyscroll
import pytmx
import re
import pygame
from app.settings import *
import os

from app.sprites.enemyFactory import EnemyFactory
from app.sprites.itemFactory import ItemFactory
# from app.sound.soundPlayerController import *
# from app.sprites.player import *

class MapData:
    def __init__(self, mapName="Map_01", screenSize=(SCREEN_WIDTH, SCREEN_HEIGHT)):

        self.nameMap = mapName

        self.tmxData = pytmx.util_pygame.load_pygame(self.reqImageName(self.nameMap))
        self.mapData = pyscroll.data.TiledMapData(self.tmxData)
        self.cameraPlayer = pyscroll.BufferedRenderer(self.mapData, screenSize, clamp_camera=True)
        # self.soundController = soundPlayerController()

        self.allSprites = pygame.sprite.Group()
        self.enemyGroup = pygame.sprite.Group()
        self.itemGroup = pygame.sprite.Group()
        # self.friendlyBullet = pygame.sprite.Group()
        # self.enemyBullet = pygame.sprite.Group()
        self.spritesHUD = pygame.sprite.Group()

        eFactory = EnemyFactory()
        iFactory = ItemFactory()

        for obj in self.tmxData.objects:
            if obj.type == "enemy":
                enemy = eFactory.create(obj)
                self.allSprites.add(enemy)
                self.enemyGroup.add(enemy)

            if obj.type == "item":
                item = iFactory.create(obj)
                self.allSprites.add(item)
                self.itemGroup.add(item)

        # Put camera in mapData
        self.camera = pyscroll.PyscrollGroup(map_layer=self.cameraPlayer, default_layer=SPRITE_LAYER)
        self.camera.add(self.allSprites)

    # For now.
    # Map names are "Map_XX" where XX is the number 01 to 99
    # Tiled names are "theme_vX.tmx" where X is the number 1 to 99
    # Changes will come.
    def reqImageName(self, nameMap):
        numberOfTheMap = int((re.findall("\d+", nameMap))[0])
        return os.path.join('tiles_map', "theme_v" + str(numberOfTheMap) + ".tmx")
