import pygame
import os

from app.menu.menu import Menu
from app.menuPause.menuPause import MenuPause
from app.scene.petScreen.eventHandlerPetScreen import EventHandlerPetScreen
from app.scene.petScreen.logicHandlerPetScreen import LogicHandlerPetScreen
from app.settings import *
from app.sprites.pet.pet import Pet
from app.scene.petScreen.petScreenData import PetScreenData


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

        self.pet = Pet()
        self.screenData.allSprites.add(self.pet)

        #Create feedMenu
        self.createFeedMenu(
            pygame.Rect(4 * SCREEN_WIDTH / 5, 2*SCREEN_HEIGHT / 5, SCREEN_WIDTH / 6, 3 * SCREEN_HEIGHT / 5)
        )

        #Get rabbit button
        self.getRabbitButton = Menu(
            pygame.Rect(1*SCREEN_WIDTH / 2, 3*SCREEN_HEIGHT / 4, self.menuFeed.optionList[1].image.get_width()/0.9, self.menuFeed.optionList[1].image.get_height()/0.7))
        self.getRabbitButton.addOption('Get rabbit', self.logicHandler.getRabbit)
        self.screenData.allSprites.add(self.getRabbitButton.spritesMenu) #Add sprite

        #Back to world button
        self.backToWorldMap = Menu(
            pygame.Rect(1 * SCREEN_WIDTH / 4, 3*SCREEN_HEIGHT / 4, self.menuFeed.optionList[1].image.get_width()/0.8, self.menuFeed.optionList[1].image.get_height()/0.7))
        self.backToWorldMap.addOption('Back to world', self.close)
        self.screenData.allSprites.add(self.backToWorldMap.spritesMenu) #Add sprite

        #all option and 2D selector for Pet Screen
        self.optionList = [self.backToWorldMap.optionList,self.getRabbitButton.optionList,self.menuFeed.optionList]
        self.selectorList = [self.backToWorldMap.selector,self.getRabbitButton.selector,self.menuFeed.selector]
        self.setDefaultPos(0, 2)

        #Menu pause
        self.menuPause = MenuPause(screen,self.backToMain)
        self.eventHandler.menuPause = self.menuPause

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
        number = self.optFont.render('apple: ' + str(self.gameData.inventory["apple"]), True, (0, 0, 0))
        self.screen.blit(number, (SCREEN_WIDTH - number.get_width(), 0))

        self.screenData.allSprites.draw(self.screen)
        pygame.display.flip()

    def createPet(self):
        pass

    def createFeedMenu(self,rect):
        self.menuFeed = Menu(rect)
        self.menuFeed.addOption('apple', self.logicHandler.giveApple)
        self.menuFeed.addOption('item2', self.close)
        self.menuFeed.addOption('item3', self.close)
        self.menuFeed.addOption('item4', self.close)
        self.menuFeed.addOption('item5', self.close)
        self.menuFeed.addOption('item6', self.close)
        self.menuFeed.addOption('item7', self.close)
        self.menuFeed.addOption('item8', self.close)
        self.menuFeed.addOption('item9', self.close)
        self.screenData.allSprites.add(self.menuFeed.spritesMenu)  # Add sprite


    def setDefaultPos(self, hPos, vPos):  # Goes with 2D selector
        for optionColumn in self.optionList:
            for option in optionColumn:
                option.deselect()
        self.optionList[0][0].select()


    def close(self):
        self.nextScene = TITLE_SCREEN
        self.sceneRunning = False #To stop creatureScreen running

    def backToMain(self):
        self.menuPause.close()
        self.close()