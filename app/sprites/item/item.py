import pygame
import os

from app.settings import *
from app.sprites.item.itemInfoList import ItemInfoList


class Item(pygame.sprite.Sprite):
    def __init__(self, x, y, imageName):
        super().__init__()

        self.name = "item"

        # self.image = pygame.transform.scale(pygame.image.load(image), (TILEDIMX, TILEDIMY))
        listItemInfo = ItemInfoList()
        if imageName in listItemInfo.item:
            imageNamePNG = listItemInfo.item[imageName].imageNamePNG
        else:
            imageNamePNG = 'cochon.png'
        linkImage = os.path.join('img', imageNamePNG)

        self.image = pygame.image.load(linkImage)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.isPhysicsApplied = False
        self.isGravityApplied = False
        self.isFrictionApplied = False
        self.isCollisionApplied = False

    def update(self):
        pass
