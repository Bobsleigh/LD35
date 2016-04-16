import pygame

from app.menu.menu import Menu
from app.menuPause.menuPause import MenuPause
from app.scene.petScreen.eventHandlerPetScreen import EventHandlerPetScreen
from app.settings import *
from app.sprites.pet import Pet


class PetScreen:
    def __init__(self, screen, gameData):
        self.screen = screen
        self.gameData = gameData
        self.eventHandler = EventHandlerPetScreen()

        self.nextScene = None

        #All sprite
        self.allSprites = pygame.sprite.Group()

        self.pet = Pet(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        self.allSprites.add(self.pet )

        #Create feedMenu
        self.createFeedMenu(
            pygame.Rect(3 * SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, SCREEN_WIDTH / 5, 3 * SCREEN_HEIGHT / 5)
        )

        #Get rabbit button
        self.getRabbitButton = Menu(
            pygame.Rect(1*SCREEN_WIDTH / 2, 4*SCREEN_HEIGHT / 5, self.menuFeed.optionList[1].image.get_width()/0.9, self.menuFeed.optionList[1].image.get_height()/0.7))
        self.getRabbitButton.addOption('Get rabbit', self.close)
        self.allSprites.add(self.getRabbitButton.spritesMenu) #Add sprite

        #Back to world button
        self.backToWorldMap = Menu(
            pygame.Rect(1 * SCREEN_WIDTH / 4, 4*SCREEN_HEIGHT / 5, self.menuFeed.optionList[1].image.get_width()/0.9, self.menuFeed.optionList[1].image.get_height()/0.7))
        self.backToWorldMap.addOption('Back to word', self.close)
        self.allSprites.add(self.backToWorldMap.spritesMenu) #Add sprite

        #all option and 2D selector for Pet Screen
        self.optionList = [self.backToWorldMap.optionList,self.getRabbitButton.optionList,self.menuFeed.optionList]
        self.selectorList = [self.backToWorldMap.selector,self.getRabbitButton.selector,self.menuFeed.selector]
        self.setDefaultPos(0, 2);

        #Menu pause
        self.menuPause = MenuPause(screen,self.backToMain)
        self.eventHandler.menuPause = self.menuPause

    def mainLoop(self):
        self.sceneRunning = True
        while self.sceneRunning:
            self.eventHandler.eventHandle(self.optionList,self.selectorList)
            self.allSprites.update()  # This will go in the logic
            self.draw()  # Drawer in THIS file, below

    def draw(self):
        self.screen.fill((255,255,255))
        self.allSprites.draw(self.screen)
        pygame.display.flip()

    def createPet(self):
        pass

    def createFeedMenu(self,rect):
        self.menuFeed = Menu(rect)
        self.menuFeed.addOption('item1', self.close)
        self.menuFeed.addOption('item2', self.close)
        self.menuFeed.addOption('item3', self.close)
        self.menuFeed.addOption('item4', self.close)
        self.menuFeed.addOption('item5', self.close)
        self.menuFeed.addOption('item6', self.close)
        self.menuFeed.addOption('item7', self.close)
        self.menuFeed.addOption('item8', self.close)
        self.menuFeed.addOption('item9', self.close)
        self.allSprites.add(self.menuFeed.spritesMenu)  # Add sprite


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