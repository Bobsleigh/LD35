import pygame
from app.menu.optionPetScreen import OptionPetScreen
from app.menu.selector import Selector


class MenuPetScreen():
    def __init__(self,dimension):

        # Menu center
        self.x = dimension.left
        self.y = dimension.top

        # Menu dimension
        self.menuWidth = dimension.width
        self.menuHeight = dimension.height

        # Menu list
        self.optionList = []

        #All sprite
        self.spritesMenu = pygame.sprite.Group()

    def addOption(self,item,method):
        self.optionList.append(OptionPetScreen(item,method))
        self.createMenu()

    def createMenu(self):

        # Default select opt. 1
        self.optionList[0].isSelected = True

        # Mecanics.
        self.optNum = len(self.optionList)
        self.setOptionSize()
        self.selector = Selector(self.optNum)

        # Add to sprite
        for option in self.optionList:
            self.spritesMenu.add(option)


    def setOptionSize(self):
        # Button real space
        spaceWidth = self.menuWidth
        spaceHeight = self.menuHeight / (self.optNum)

        for option in self.optionList:
            option.image = pygame.Surface([spaceWidth * 0.9, spaceHeight * 0.9])
            option.rect = option.image.get_rect()

            count = self.optionList.index(option)
            option.rect.x = self.x - spaceWidth * 0.45
            option.rect.y = self.y + self.menuHeight * (2 * count - self.optNum) / (
            2 * self.optNum) + spaceHeight * 0.15

            option.button = option.rect.inflate(-option.image.get_height() * 0.2, -option.image.get_height() * 0.2)
            option.button.x = option.image.get_height() * 0.1
            option.button.y = option.image.get_height() * 0.1

            option.textPos = [option.image.get_width()/2,(option.image.get_height()-option.printedName.get_height())*0.5]

            option.scalingDim(option.image.get_height() * 0.7)
            option.iconPos = [option.image.get_width()/2-option.icon.get_width()*1.1, (option.image.get_height() - option.icon.get_height()) * 0.5]


    def updateName(self,item):
        for option in self.optionList:
            if item.key == option.item.key:
                option.number = item.inventory