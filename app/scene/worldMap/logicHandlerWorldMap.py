from app.mapData import MapData
from app.settings import *

class LogicHandlerWorldMap:
    def __init__(self, mapData):
        self.sceneRunning = True
        self.endState = None
        # self.spawmPointPlayerx = 0
        # self.spawmPointPlayery = 0
        self.newMapData = None
        self.mapData = mapData

    def handle(self, player):
        # self.handleObjectCollision(player, self.mapData)
        self.handleZoneCollision(player)
        self.mapData.allSprites.update()


    def handleZoneCollision(self, player):

        for obj in self.mapData.tmxData.objects:
            if self.isPlayerIsInZone(player, obj) == True:
                if obj.name == "OutZone":

                    nameNewZone = obj.LevelZone
                    nameInZone = obj.InZone

                    # Initializing new map
                    self.newMapData = MapData(nameNewZone, nameInZone)

    # def handleBottomCollision(self, sprites):
    #     for sprite in sprites:
    #         if sprite.rect.y + sprite.rect.height > SCREEN_HEIGHT:
    #             sprite.rect.y = SCREEN_HEIGHT - sprite.rect.height
    #             sprite.speedy = 0
    #             sprite.jumpState = GROUNDED


    def isPlayerIsInZone(self, player, object):

        if player.rect.centerx  >= object.x and \
           player.rect.centerx <= object.x + object.width and \
           player.rect.centery >= object.y and \
           player.rect.centery <= object.y + object.height:
           return True
        else:
           return False