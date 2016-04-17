from app.settings import *
from app.sprites.item.item import Item

from app.sprites.pet.rabbit import Rabbit
from app.sprites.pet.tiger import Tiger
from app.sprites.pet.unicorn import Unicorn
from app.sprites.pet.dragon import Dragon

# All the global data for the game and player
class GameData:
    def __init__(self, scene=None):

        self.cupcake = Item(0,0)

        self.inventory = {}
        self.inventory["coin"] = 0
        self.inventory["cupcake"] = 10
        self.inventory["item2"] = 0
        self.inventory["item3"] = 0
        self.inventory["item4"] = 0
        self.inventory["item5"] = 0
        self.inventory["item6"] = 0
        self.inventory["item7"] = 0
        self.inventory["item8"] = 0
        self.inventory["item9"] = 0

        #Was item discovered?
        self.itemUnlock = {}
        self.itemUnlock["cupcake"] = True
        self.itemUnlock["item2"] = True
        self.itemUnlock["item3"] = True
        self.itemUnlock["item4"] = False
        self.itemUnlock["item5"] = False
        self.itemUnlock["item6"] = True
        self.itemUnlock["item7"] = False
        self.itemUnlock["item8"] = False
        self.itemUnlock["item9"] = False

        #My pet: rabbit at first
        self.myPet = Rabbit()

        #PetTypeList
        self.petTypeList = []
        self.petTypeList.append([RABBIT, Rabbit()])
        self.petTypeList.append([TIGER, Tiger()])
        self.petTypeList.append([UNICORN, Unicorn()])
        self.petTypeList.append([DRAGON, Dragon()])

        self.scene = scene
        self.mapData = None

