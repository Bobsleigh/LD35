from app.settings import *
from app.sprites.item.item import Item

from app.sprites.pet.pet import Pet


# All the global data for the game and player
class GameData:
    def __init__(self, scene=None):

        self.inventory = {}
        self.inventory["coin"] = 0
        self.inventory["cupcake"] = 10
        self.inventory["goldBar"] = 10
        self.inventory["horseshoe"] = 10
        self.inventory["item4"] = 0
        self.inventory["item5"] = 0
        self.inventory["item6"] = 0
        self.inventory["item7"] = 0
        self.inventory["item8"] = 0
        self.inventory["item9"] = 0

        #Was item discovered?
        self.itemUnlock = {}
        self.itemUnlock["cupcake"] = True
        self.itemUnlock["goldBar"] = True
        self.itemUnlock["horseshoe"] = True
        self.itemUnlock["item4"] = False
        self.itemUnlock["item5"] = False
        self.itemUnlock["item6"] = True
        self.itemUnlock["item7"] = False
        self.itemUnlock["item8"] = False
        self.itemUnlock["item9"] = False

        #My pet: rabbit at first
        self.myPet = Pet()
        self.myPet.becomeRabbit()


        self.scene = scene
        self.mapData = None

