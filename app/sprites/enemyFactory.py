from app.sprites.enemy.enemy import Enemy
from app.sprites.enemy.enemyCactus import EnemyCactus
from app.sprites.enemy.enemyShooter import EnemyShooter
from app.tools.functionTools import *


class EnemyFactory:
    def __init__(self):
        pass

    def create(self, enemy, theMap=None):
        eName = seekAtt(enemy, "name")
        if eName == "enemyCactus":
            return self.createEnemyCactus(enemy)
        if eName == "enemyShooter":
            return self.createEnemyShooter(enemy, theMap)

    def createEnemyBase(self, enemy):
        enemyCreated = Enemy(enemy.x, enemy.y)
        return enemyCreated

    def createEnemyCactus(self, enemy):
         direction = seekAtt(enemy, "direction")
         distanceMax = seekAtt(enemy, "distanceMax")

         enemyCreated = EnemyCactus(enemy.x, enemy.y)

         if direction:
            enemyCreated.set_direction(direction)
         if distanceMax:
            enemyCreated.set_distance_max(int(distanceMax))
         return enemyCreated

    def createEnemyShooter(self, enemy, theMap):
        direction = seekAtt(enemy, "direction")

        if direction is None:
            return EnemyShooter(enemy.x, enemy.y, theMap)
        else:
            return EnemyShooter(enemy.x, enemy.y, theMap, direction)