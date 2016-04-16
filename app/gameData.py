from app.settings import *
from app.sprites.pet.rabbit import Rabbit
from app.sprites.pet.tiger import Tiger

# All the global data for the game and player
class GameData:
    def __init__(self):

        self.inventory = {}
        self.inventory["coin"] = 0
        self.inventory["apple"] = 10
        self.inventory["orange"] = 0
        self.inventory["item3"] = 0
        self.inventory["item4"] = 0

        #Was item discovered?
        self.itemUnlock = {}
        self.itemUnlock["apple"] = True
        self.itemUnlock["orange"] = False
        self.itemUnlock["item3"] = False
        self.itemUnlock["item4"] = False

        #My pet: rabbit at first
        self.myPet = Rabbit()

        #petList
        self.petTypeList = []
        self.petTypeList.append([RABBIT, Rabbit()])
        self.petTypeList.append([TIGER, Tiger()])
