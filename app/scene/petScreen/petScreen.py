import pygame
import os

from app.menu.menu import Menu
from app.menuPause.menuPause import MenuPause
from app.scene.petScreen.eventHandlerPetScreen import EventHandlerPetScreen
from app.scene.petScreen.logicHandlerPetScreen import LogicHandlerPetScreen
from app.settings import *
from app.scene.petScreen.petScreenData import PetScreenData
from app.scene.musicFactory import MusicFactory


class PetScreen:
    def __init__(self, screen, gameData):
        self.screen = screen

        self.background = pygame.image.load(os.path.join('img', 'petScreenBackground.png'))
        self.screen.blit(self.background, (0, 0))

        self.gameData = gameData
        self.screenData = PetScreenData(self.gameData)
        self.eventHandler = EventHandlerPetScreen()
        self.logicHandler = LogicHandlerPetScreen(self.gameData,self.screenData)

        self.nextScene = None

        self.screenData.allSprites.add(self.gameData.myPet)

        #Create feedMenu
        self.realMenuFeedHeight = 3 * SCREEN_HEIGHT / 5
        self.realMenuFeedPosy = 2*SCREEN_HEIGHT / 5
        self.createFeedMenu(4 * SCREEN_WIDTH / 5, self.realMenuFeedPosy, SCREEN_WIDTH / 6, self.realMenuFeedHeight)

        #Get rabbit button
        self.getRabbitButton = Menu(
            pygame.Rect(1*SCREEN_WIDTH / 2, 3*SCREEN_HEIGHT / 4, SCREEN_WIDTH / 4, self.realMenuFeedHeight/9))
        self.getRabbitButton.addOption('Get rabbit', self.logicHandler.getRabbit)
        self.screenData.allSprites.add(self.getRabbitButton.spritesMenu) #Add sprite

        #Back to world button
        self.backToWorldMap = Menu(
            pygame.Rect(1 * SCREEN_WIDTH / 4, 3*SCREEN_HEIGHT / 4, SCREEN_WIDTH / 4, self.realMenuFeedHeight/9))
        self.backToWorldMap.addOption('Back to world', self.close)
        self.screenData.allSprites.add(self.backToWorldMap.spritesMenu) #Add sprite

        #all option and 2D selector for Pet Screen
        self.optionList = [self.backToWorldMap.optionList,self.getRabbitButton.optionList,self.menuFeed.optionList]
        self.selectorList = [self.backToWorldMap.selector,self.getRabbitButton.selector,self.menuFeed.selector]
        self.setDefaultPos()

        #Menu pause
        self.menuPause = MenuPause(screen,self.backToMain)
        self.eventHandler.menuPause = self.menuPause

        MusicFactory(PET_SCREEN)


    def mainLoop(self):
        self.sceneRunning = True
        while self.sceneRunning:
            self.eventHandler.eventHandle(self.optionList,self.selectorList)
            self.logicHandler.logicHandle( )  # This will go in the logic
            self.draw()  # Drawer in THIS file, below

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        #Test
        self.optFont = pygame.font.SysFont(FONT_NAME, 30)
        number = self.optFont.render('cupcake: ' + str(self.gameData.itemInfoList.item["cupcake"].inventory), True, (0, 0, 0))
        self.screen.blit(number, (SCREEN_WIDTH - number.get_width(), 0))

        self.optFont = pygame.font.SysFont(FONT_NAME, 30)
        number = self.optFont.render('goldBar: ' + str(self.gameData.itemInfoList.item["goldBar"].inventory), True, (0, 0, 0))
        self.screen.blit(number, (SCREEN_WIDTH - number.get_width(), 20))

        self.optFont = pygame.font.SysFont(FONT_NAME, 30)
        number = self.optFont.render('horseshoe: ' + str(self.gameData.itemInfoList.item["horseshoe"].inventory), True, (0, 0, 0))
        self.screen.blit(number, (SCREEN_WIDTH - number.get_width(), 40))


        self.screenData.allSprites.draw(self.screen)
        pygame.display.flip()

    def createFeedMenu(self,centerx,centery,width,height):
        self.getMenuSpec(centery,height)
        self.menuFeed = Menu(pygame.Rect(centerx, self.menuFeedPosy, width, self.menuFeedHeight)
        )
        #Check what item we have
        if self.gameData.itemInfoList.item["cupcake"].unlock:
            self.menuFeed.addOption('cupcake', self.logicHandler.giveCupcake)
        if self.gameData.itemInfoList.item["goldBar"].unlock:
            self.menuFeed.addOption('goldBar', self.logicHandler.giveGoldBar)
        if self.gameData.itemInfoList.item["horseshoe"].unlock:
            self.menuFeed.addOption('horseshoe', self.logicHandler.giveHorseshoe)
        if self.gameData.itemInfoList.item["bone"].unlock:
            self.menuFeed.addOption('bone', self.logicHandler.giveBone)
        if self.gameData.itemInfoList.item["carrot"].unlock:
            self.menuFeed.addOption('carrot', self.logicHandler.giveCarrot)
        if self.gameData.itemInfoList.item["apple"].unlock:
            self.menuFeed.addOption('apple', self.logicHandler.giveApple)
        if self.gameData.itemInfoList.item["pokerChip"].unlock:
            self.menuFeed.addOption('gun', self.logicHandler.giveGun)
        if self.gameData.itemInfoList.item["pokerChip"].unlock:
            self.menuFeed.addOption('pokerChip', self.logicHandler.givePokerChip)
        if self.gameData.itemInfoList.item["totem"].unlock:
            self.menuFeed.addOption('totem', self.logicHandler.giveTotem)
        self.screenData.allSprites.add(self.menuFeed.spritesMenu)  # Add sprite


    def setDefaultPos(self):  # Goes with 2D selector
        for optionColumn in self.optionList:
            for option in optionColumn:
                option.deselect()
        self.optionList[0][0].select()

    def getMenuSpec(self,centery,height):
        optForNow = 0
        for item in self.gameData.itemInfoList.item:
            if self.gameData.itemInfoList.item[item].unlock:
                optForNow += 1
        realOptNum = 9
        self.menuFeedHeight = height*(optForNow)/realOptNum
        self.menuFeedPosy = centery-self.realMenuFeedHeight/2+self.menuFeedHeight/2

    def close(self):
        self.nextScene = TITLE_SCREEN
        self.sceneRunning = False #To stop petScreen running

    def backToMain(self):
        self.menuPause.close()
        self.close()