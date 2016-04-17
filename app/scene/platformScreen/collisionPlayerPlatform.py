from app.settings import *
import pygame

class CollisionPlayerPlatform:
    def __init__(self):
        # self.soundControl = soundPlayerController
        pass

    def collisionAllSprites(self, player, mapData, gameMemory):
        for sprite in mapData.allSprites:
            if sprite.isPhysicsApplied == True or sprite.isCollisionApplied == True:

                self.rightCollision(sprite, mapData)
                self.downCollision(sprite, mapData)
                self.leftCollision(sprite, mapData)
                self.upCollision(sprite, mapData)

                self.collisionWithEnemy(player, mapData.enemyGroup)
                # self.pickPowerUp(player, mapData.powerUpGroup, gameMemory)

    def rightCollision(self,player, map):
        tileWidth = map.tmxData.tilewidth
        tileHeight = map.tmxData.tileheight
        mapWidth = map.tmxData.width * tileWidth
        # mapHeight = map.tmxData.height * tileHeight
        i=0

        if player.rect.right + player.speedx > 0:
            if player.speedx >= tileWidth:
                while player.rect.right+i*tileWidth < player.rect.right + player.speedx:
                    if player.rect.right+i*tileWidth >= mapWidth:
                        j=0
                        while map.tmxData.get_tile_gid((mapWidth - 1 - j*tileWidth)/tileWidth, player.rect.top/tileHeight, COLLISION_LAYER) == SOLID and map.tmxData.get_tile_gid((mapWidth - 1- j*tileWidth)/tileWidth, (player.rect.bottom)/tileHeight, COLLISION_LAYER) == SOLID:
                            j += 1
                        player.rect.right = mapWidth-j*tileWidth-1
                        player.speedx = 0
                        return

                    upRightTileGid = map.tmxData.get_tile_gid((player.rect.right + i*tileWidth)/tileWidth, player.rect.top/tileHeight, COLLISION_LAYER)
                    downRightTileGid = map.tmxData.get_tile_gid((player.rect.right + i*tileWidth)/tileWidth, (player.rect.bottom-1)/tileHeight, COLLISION_LAYER)

                    if (upRightTileGid  == SOLID or downRightTileGid  == SOLID) and player.speedx > 0 and player.facingSide == RIGHT:
                        while map.tmxData.get_tile_gid((player.rect.right + 1)/tileWidth, player.rect.top/tileHeight, COLLISION_LAYER) != SOLID and map.tmxData.get_tile_gid((player.rect.right + 1)/tileWidth, (player.rect.bottom-1)/tileHeight, COLLISION_LAYER) != SOLID:
                            player.rect.right += 1
                        player.speedx = 0
                    i += 1

            else:
                upRightTileGid = map.tmxData.get_tile_gid((player.rect.right + player.speedx)/tileWidth, player.rect.top/tileHeight, COLLISION_LAYER)
                downRightTileGid = map.tmxData.get_tile_gid((player.rect.right + player.speedx)/tileWidth, (player.rect.bottom-1)/tileHeight, COLLISION_LAYER)

                if (upRightTileGid  == SOLID or downRightTileGid  == SOLID) and player.speedx > 0:
                    while map.tmxData.get_tile_gid((player.rect.right + 1)/tileWidth, player.rect.top/tileHeight, COLLISION_LAYER) != SOLID and map.tmxData.get_tile_gid((player.rect.right + 1)/tileWidth, (player.rect.bottom)/tileHeight, COLLISION_LAYER) != SOLID:
                        player.rect.right += 1
                    player.speedx = 0

    def leftCollision(self,player, map):
        tileWidth = map.tmxData.tilewidth
        tileHeight = map.tmxData.tileheight
        # mapWidth = map.tmxData.width * tileWidth
        # mapHeight = map.tmxData.height * tileHeight
        i = 0

        if -player.speedx >= tileWidth:
            while player.rect.x-i*tileWidth > player.rect.x + player.speedx:
                if player.rect.x-i*tileWidth <= 0:
                    j=0
                    while map.tmxData.get_tile_gid((0 + j*tileWidth)/tileWidth, player.rect.top/tileHeight, COLLISION_LAYER) == SOLID and map.tmxData.get_tile_gid((0 + j*tileWidth)/tileWidth, (player.rect.bottom-1)/tileHeight, COLLISION_LAYER) == SOLID:
                        j += 1
                    player.rect.left = j*tileWidth
                    player.speedx = 0
                    return

                upLeftTileGid = map.tmxData.get_tile_gid((player.rect.left - i*tileWidth)/tileWidth, player.rect.top/tileHeight, COLLISION_LAYER)
                downLeftTileGid = map.tmxData.get_tile_gid((player.rect.left - i*tileWidth)/tileWidth, (player.rect.bottom-1)/tileHeight, COLLISION_LAYER)

                if (upLeftTileGid  == SOLID or downLeftTileGid  == SOLID) and player.facingSide == LEFT:
                    while map.tmxData.get_tile_gid((player.rect.left)/tileWidth, player.rect.top/tileHeight, COLLISION_LAYER) != SOLID and map.tmxData.get_tile_gid((player.rect.left)/tileWidth, (player.rect.bottom-1)/tileHeight, COLLISION_LAYER) != SOLID:
                        player.rect.left -= 1
                    player.speedx = 0
                i += 1

        else:
            upLeftTileGid = map.tmxData.get_tile_gid((player.rect.left + player.speedx)/tileWidth, player.rect.top/tileHeight, COLLISION_LAYER)
            downLeftTileGid = map.tmxData.get_tile_gid((player.rect.left + player.speedx)/tileWidth, (player.rect.bottom-1)/tileHeight, COLLISION_LAYER)

            if (upLeftTileGid  == SOLID or downLeftTileGid  == SOLID) and player.speedx < 0:
                while map.tmxData.get_tile_gid((player.rect.left)/tileWidth, player.rect.top/tileHeight, COLLISION_LAYER) != SOLID and map.tmxData.get_tile_gid((player.rect.left)/tileWidth, (player.rect.bottom-1)/tileHeight, COLLISION_LAYER) != SOLID:
                    player.rect.left -= 1
                player.speedx = 0

    def downCollision(self,player, map):
        tileWidth = map.tmxData.tilewidth
        tileHeight = map.tmxData.tileheight
        # mapWidth = map.tmxData.width * tileWidth
        # mapHeight = map.tmxData.height * tileHeight

        downLeftTileGid = map.tmxData.get_tile_gid((player.rect.left+1)/tileWidth, (player.rect.bottom + player.speedy)/tileHeight, COLLISION_LAYER)
        downRightTileGid = map.tmxData.get_tile_gid((player.rect.right)/tileWidth, (player.rect.bottom + player.speedy)/tileHeight, COLLISION_LAYER)

        if downLeftTileGid == SOLID or downRightTileGid == SOLID:
            while map.tmxData.get_tile_gid((player.rect.left+1)/tileWidth, (player.rect.bottom)/tileHeight, COLLISION_LAYER) != SOLID and map.tmxData.get_tile_gid((player.rect.right)/tileWidth, (player.rect.bottom)/tileHeight, COLLISION_LAYER) != SOLID:
                player.rect.bottom += 1
            player.speedy = 0
            player.jumpState = GROUNDED
            player.wallJumpRightAllowed = True
            player.wallJumpLeftAllowed = True
        elif downLeftTileGid == SPIKE or downRightTileGid == SPIKE:
            player.dead()
        else:
            if player.jumpState == GROUNDED:
                player.jumpState = JUMP


    def upCollision(self,player, map):
        tileWidth = map.tmxData.tilewidth
        tileHeight = map.tmxData.tileheight

        upLeftTileGid = map.tmxData.get_tile_gid((player.rect.left+1)/tileWidth, (player.rect.top + player.speedy)/tileHeight, COLLISION_LAYER)
        upRightTileGid = map.tmxData.get_tile_gid(player.rect.right/tileWidth, (player.rect.top + player.speedy)/tileHeight, COLLISION_LAYER)

        if upLeftTileGid == SOLID or upRightTileGid == SOLID:
            while map.tmxData.get_tile_gid((player.rect.left+1)/tileWidth, (player.rect.top)/tileHeight, COLLISION_LAYER) != SOLID and map.tmxData.get_tile_gid(player.rect.right/tileWidth, (player.rect.top)/tileHeight, COLLISION_LAYER) != SOLID:
                player.rect.bottom -= 1
            player.speedy = 0
        elif upLeftTileGid == SPIKE or upRightTileGid == SPIKE:
            player.dead()

    def collisionWithEnemy(self, player, enemyGroup):
        collisionList = pygame.sprite.spritecollide(player, enemyGroup, False)
        for enemy in collisionList:
            # player.loseLife()
            # self.soundControl.hurt()
            pass

    # def pickPowerUp(self, player, powerUpGroup, gameMemory):
    #     collisionList = pygame.sprite.spritecollide(player, powerUpGroup, False)
    #     for powerUp in collisionList:
    #         if powerUp.name == "powerUp_HealthMax":
    #             player.pickedPowerUpMaxHealth()
    #             gameMemory.registerPickedUpPowerUpHealth()
    #             self.soundControl.maxHealthPowerup()
    #         elif powerUp.name == "powerUp_Health":
    #             player.pickedPowerUpHealth()
    #             self.soundControl.healthPowerup()
    #         powerUp.kill()


def collisionBulletWall(bullet, map):
    tileWidth = map.tmxData.tilewidth
    tileHeight = map.tmxData.tileheight
    mapWidth = map.tmxData.width * tileWidth
    mapHeight = map.tmxData.height * tileHeight

    if (bullet.rect.top < tileHeight or bullet.rect.bottom > mapHeight - tileHeight) or (bullet.rect.left < tileWidth or bullet.rect.right > mapWidth - tileWidth):
        bullet.kill()
        return

    if bullet.speedx > 0:
        upRightTileGid = map.tmxData.get_tile_gid((bullet.rect.right + bullet.speedx)/tileWidth, bullet.rect.top/tileHeight, COLLISION_LAYER)
        downRightTileGid = map.tmxData.get_tile_gid((bullet.rect.right + bullet.speedx)/tileWidth, (bullet.rect.bottom-1)/tileHeight, COLLISION_LAYER)

        if (upRightTileGid  == SOLID or downRightTileGid  == SOLID):
            bullet.kill()

    elif bullet.speedx < 0:
        upLeftTileGid = map.tmxData.get_tile_gid((bullet.rect.left + bullet.speedx)/tileWidth, bullet.rect.top/tileHeight, COLLISION_LAYER)
        downLeftTileGid = map.tmxData.get_tile_gid((bullet.rect.left + bullet.speedx)/tileWidth, (bullet.rect.bottom)/tileHeight, COLLISION_LAYER)

        if (upLeftTileGid  == SOLID or downLeftTileGid  == SOLID) and bullet.speedx < 0:
            bullet.kill()

# def collisionBulletEnemy(bullet, map):
#     collisionList = pygame.sprite.spritecollide(bullet, map.enemyGroup, False)
#     for enemy in collisionList:
#         enemy.kill()
#         bullet.kill()

def collisionBulletPlayer(map, player):
    collisionList = pygame.sprite.spritecollide(player, map.enemyBullet, False)
    for bullet in collisionList:
        player.loseLife()
        bullet.kill()
