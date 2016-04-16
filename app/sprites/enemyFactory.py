from app.tools.functionTools import *
from app.sprites.enemy.enemy import Enemy


class EnemyFactory:
    def __init__(self):
        pass

    def create(self, enemy):
        eName = seekAtt(enemy, "name")
        if eName == "enemy_noob":
            return self.createEnemyBase(enemy)


    def createEnemyBase(self, enemy):
        enemyCreated = Enemy(enemy.x, enemy.y)
        return enemyCreated


    # def createEnemyNoob(self, enemy):
    #     direction = seekAtt(enemy, "direction")
    #     distanceMax = seekAtt(enemy, "distanceMax")
    #
    #     enemyCreated = Enemy_noob(enemy.x, enemy.y)
    #
    #     if direction:
    #         enemyCreated.setDirection(direction)
    #     if distanceMax:
    #         enemyCreated.setDistanceMax(int(distanceMax))
    #     return enemyCreated


