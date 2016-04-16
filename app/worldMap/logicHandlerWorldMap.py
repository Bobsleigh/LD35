from app.mapData import MapData
from app.settings import *

class LogicHandlerWorldMap:
    def __init__(self, mapData):
        self.sceneRunning = True
        self.endState = None
        self.spawmPointPlayerx = 0
        self.spawmPointPlayery = 0
        self.newMap = None
        self.mapData = mapData

    def handle(self, player, gameMemory):
        self.handleObjectCollision(player, self.mapData)
        self.mapData.allSprites.update()
        self.mapData.soundController.update()

    def handleBottomCollision(self, sprites):
        for sprite in sprites:
            if sprite.rect.y + sprite.rect.height > SCREEN_HEIGHT:
                sprite.rect.y = SCREEN_HEIGHT - sprite.rect.height
                sprite.speedy = 0
                sprite.jumpState = GROUNDED

    def handleObjectCollision(self, player, map):
        for object in map.tmxData.objects:
            if self.isPlayerIsInObject(player, object) == True:
                if object.type == "out_zone":
                    tuple = map.reqNameAndPositionNewMap(object.name, player)

                    nameNewMap = tuple[0]

                    self.spawmPointPlayerx = tuple[1]
                    self.spawmPointPlayery = tuple[2]
                    self.newMap = MapData(nameNewMap)

    def isPlayerIsInObject(self, player, object):

        if player.rect.centerx  >= object.x and \
           player.rect.centerx <= object.x + object.width and \
           player.rect.centery >= object.y and \
           player.rect.centery <= object.y + object.height:
           return True
        else:
           return False