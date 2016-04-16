# from app.map.mapData import MapData

class LogicHandlerPlatformScreen:
    def __init__(self, mapData):

        self.sceneRunning = True
        self.endState = None
        # self.collisionChecker = CollisionPlayer(mapData.soundController)
        self.spawmPointPlayerx = 0
        self.spawmPointPlayery = 0
        self.newMap = None
        self.mapData = mapData


    def logicHandle(self):

        self.mapData.allSprites.update()
        pass
