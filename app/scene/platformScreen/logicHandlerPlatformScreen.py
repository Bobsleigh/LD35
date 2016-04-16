# from app.map.mapData import MapData
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
        # self.applyGravity(self.mapData.allSprites)
        # self.applyFriction(self.mapData.allSprites)
        # self.collisionChecker.collisionAllSprites(player, self.mapData, mapData)
        self.mapData.allSprites.update()


        # self.handleBullets(self.mapData, player)
        # self.handleObjectCollision(player, self.mapData)
        # self.gameOverCondition(player, self.mapData)

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