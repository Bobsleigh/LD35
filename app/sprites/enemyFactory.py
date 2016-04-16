from app.sprites.enemy import Enemy
# from app.enemy.enemyFlyingCircle import EnemyFlyingCircle
# from app.enemy.enemyShooter import EnemyShooter
from app.tools.functionTools import *


class EnemyFactory:
    def __init__(self):
        pass

    def create(self, enemy):
        eName = seekAtt(enemy, "name")
        if eName == "enemy_noob":
            return self.createEnemyNoob(enemy)


    def createEnemyNoob(self, enemy):
        direction = seekAtt(enemy, "direction")
        distanceMax = seekAtt(enemy, "distanceMax")

        enemyCreated = Enemy_noob(enemy.x, enemy.y)

        if direction:
            enemyCreated.setDirection(direction)
        if distanceMax:
            enemyCreated.setDistanceMax(int(distanceMax))
        return enemyCreated


