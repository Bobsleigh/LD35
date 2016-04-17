import pygame
import os

from app.menu.menu import Menu
from app.menu.menuPetScreen import MenuPetScreen

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
        self.menuFeedWidth = 1* SCREEN_WIDTH / 7
        self.realMenuFeedHeight = 7 * SCREEN_HEIGHT / 9
        self.menuFeedPosx = 4* SCREEN_WIDTH / 5
        self.realMenuFeedPosy = 2*SCREEN_HEIGHT / 5
        self.createFeedMenu()

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
        self.groupAllMenu(0,0)

        #Menu pause
        self.menuPause = MenuPause(screen,self.backToMain)
        self.eventHandler.menuPause = self.menuPause

        MusicFactory(PET_SCREEN)


    def mainLoop(self):
        self.sceneRunning = True
        while self.sceneRunning:
            self.eventHandler.eventHandle(self.optionList,self.selectorList)
            self.logicHandler.logicHandle()  # This will go in the logic

            #Don't know where to put this....
            if self.logicHandler.recreateFeedMenuPlease:
                self.logicHandler.recreateFeedMenuPlease = False
                self.screenData.allSprites.remove(self.menuFeed.spritesMenu)
                self.createFeedMenu()
                self.groupAllMenu(self.eventHandler.hPos,0)
            if self.logicHandler.updateFeedMenuPlease:
                self.logicHandler.updateFeedMenuPlease = False
                self.updateMenuFeed()

            self.draw()  # Drawer in THIS file, below

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        # For testing only
        # self.testFont = pygame.font.SysFont('arial', 36)
        # test = self.testFont.render('map4: ' + str(self.gameData.mapUnlock['map4']), True, (0, 0, 0))
        # self.screen.blit(test, (0, 0))

        self.screenData.allSprites.draw(self.screen)
        pygame.display.flip()

    def createFeedMenu(self):
        self.getMenuSpec(self.realMenuFeedPosy,self.realMenuFeedHeight)

        if self.optForNow > 0:
            self.menuFeed = MenuPetScreen(pygame.Rect(self.menuFeedPosx, self.menuFeedPosy, self.menuFeedWidth, self.menuFeedHeight)
            )
            #Check what item we have
            if self.gameData.itemInfoList.item["cupcake"].unlock:
                self.menuFeed.addOption(self.gameData.itemInfoList.item['cupcake'], self.logicHandler.giveCupcake)
            if self.gameData.itemInfoList.item["goldBar"].unlock:
                self.menuFeed.addOption(self.gameData.itemInfoList.item['goldBar'], self.logicHandler.giveGoldBar)
            if self.gameData.itemInfoList.item["horseshoe"].unlock:
                self.menuFeed.addOption(self.gameData.itemInfoList.item['horseshoe'], self.logicHandler.giveHorseshoe)
            if self.gameData.itemInfoList.item["bone"].unlock:
                self.menuFeed.addOption(self.gameData.itemInfoList.item['bone'], self.logicHandler.giveBone)
            if self.gameData.itemInfoList.item["carrot"].unlock:
                self.menuFeed.addOption(self.gameData.itemInfoList.item['carrot'], self.logicHandler.giveCarrot)
            if self.gameData.itemInfoList.item["apple"].unlock:
                self.menuFeed.addOption(self.gameData.itemInfoList.item['apple'], self.logicHandler.giveApple)
            if self.gameData.itemInfoList.item["pokerChip"].unlock:
                self.menuFeed.addOption(self.gameData.itemInfoList.item['gun'], self.logicHandler.giveGun)
            if self.gameData.itemInfoList.item["pokerChip"].unlock:
                self.menuFeed.addOption(self.gameData.itemInfoList.item['pokerChip'], self.logicHandler.givePokerChip)
            if self.gameData.itemInfoList.item["totem"].unlock:
                self.menuFeed.addOption(self.gameData.itemInfoList.item['totem'], self.logicHandler.giveTotem)
            self.screenData.allSprites.add(self.menuFeed.spritesMenu)  # Add sprite

        else:
            self.menuFeed = None

    def updateMenuFeed(self):
        for key in self.gameData.itemInfoList.item:
            self.menuFeed.updateName(self.gameData.itemInfoList.item[key])

    def setDefaultPos(self,hPos,vPos):  # Goes with 2D selector
        for optionColumn in self.optionList:
            for option in optionColumn:
                option.deselect()
        self.optionList[hPos][vPos].select()

    def getMenuSpec(self,centery,height):
        self.optForNow = 0
        for item in self.gameData.itemInfoList.item:
            if self.gameData.itemInfoList.item[item].unlock:
                self.optForNow += 1

        realOptNum = 9
        self.menuFeedHeight = height*(self.optForNow)/realOptNum
        self.menuFeedPosy = centery-self.realMenuFeedHeight/2+self.menuFeedHeight/2


    def groupAllMenu(self,selectorHPos,selectorVPos):
        if self.optForNow == 0:
            self.optionList = [self.backToWorldMap.optionList, self.getRabbitButton.optionList]
            self.selectorList = [self.backToWorldMap.selector, self.getRabbitButton.selector]
        else:
            self.optionList = [self.backToWorldMap.optionList, self.getRabbitButton.optionList,self.menuFeed.optionList]
            self.selectorList = [self.backToWorldMap.selector, self.getRabbitButton.selector, self.menuFeed.selector]
        self.setDefaultPos(selectorHPos,selectorVPos)

    def close(self):
        self.nextScene = TITLE_SCREEN
        self.sceneRunning = False #To stop petScreen running

    def backToMain(self):
        self.menuPause.close()
        self.close()