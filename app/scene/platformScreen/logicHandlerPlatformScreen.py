from app.mapData import MapData
from app.tools.functionTools import *

class LogicHandlerPlatformScreen:
    def __init__(self, mapData):

        self.sceneRunning = True
        self.endState = None
        # self.collisionChecker = CollisionPlayer(mapData.soundController)
        self.spawmPointPlayerx = 0
        self.spawmPointPlayery = 0
        self.newMap = None
        self.mapData = mapData


    def logicHandle(self, player):

        self.handleZoneCollision(player, self.mapData)
        self.mapData.allSprites.update()

    def handleZoneCollision(self, player):

        for obj in self.mapData.tmxData.objects:
            if self.isPlayerIsInObject(player, obj) == True:
                if obj.name == "OutZone":
                    nameNewZone = seekAtt(obj, "LevelZone")
                    nameInZone = seekAtt(obj, "InZone")

                    # Initializing new map
                    self.newMap = MapData(nameNewZone, nameInZone)

    def isPlayerIsInZone(self, player, zone):

        if player.rect.centerx  >= zone.x and \
           player.rect.centerx <= zone.x + zone.width and \
           player.rect.centery >= zone.y and \
           player.rect.centery <= zone.y + zone.height:
           return True
        else:
           return False