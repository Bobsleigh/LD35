from app.mapData import MapData
from app.tools.functionTools import *
from app.settings import *
from app.scene.platformScreen.collisionPlayerPlatform import CollisionPlayerPlatform


class LogicHandlerPlatformScreen:
    def __init__(self, mapData):

        self.sceneRunning = True
        self.endState = None
        self.collisionChecker = CollisionPlayerPlatform()
        self.spawmPointPlayerx = 0
        self.spawmPointPlayery = 0
        self.newMap = None
        self.mapData = mapData


    def handle(self, player, mapData):
        self.applyGravity(self.mapData.allSprites)
        self.applyFriction(self.mapData.allSprites)
        self.collisionChecker.collisionAllSprites(player, self.mapData, mapData)
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

    def applyGravity(self, allSprites):
        for sprite in allSprites:
            if sprite.isPhysicsApplied == True or sprite.isGravityApplied == True:
                sprite.speedy += GRAVITY

    def applyFriction(self, allSprites):
        for sprite in allSprites:
            if sprite.isPhysicsApplied == True or sprite.isFrictionApplied == True:
                pass
                if sprite.speedx > 0 and sprite.speedx - FRICTION > 0:
                    sprite.speedx -= FRICTION
                elif sprite.speedx > 0:
                    sprite.speedx = 0

                if sprite.speedx < 0 and sprite.speedx + FRICTION < 0:
                    sprite.speedx += FRICTION
                elif sprite.speedx < 0:
                    sprite.speedx = 0