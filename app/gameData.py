from app.settings import *

#To initialize my pet
import os
import pygame
from app.sprites.pet.petList import PetList


# All the global data for the game and player
class GameData:
    def __init__(self, scene=None):

        self.inventory = {}
        self.inventory["coin"] = 0
        self.inventory["cupcake"] = 10
        self.inventory["goldBar"] = 10
        self.inventory["horseshoe"] = 10
        self.inventory["bone"] = 0
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
        self.itemUnlock["item4"] = True
        self.itemUnlock["item5"] = True
        self.itemUnlock["item6"] = True
        self.itemUnlock["item7"] = True
        self.itemUnlock["item8"] = True
        self.itemUnlock["item9"] = True

        #Was map unlocked?
        self.mapUnlock = {}
        self.mapUnlock["map1"] = True
        self.mapUnlock["map2"] = True
        self.mapUnlock["map3"] = True
        self.mapUnlock["map4"] = True

        #My pet: rabbit at first
        self.petList = PetList()
        self.myPet = self.petList.pet['rabbit']
        self.myPet.loadImage()


        self.scene = scene
        self.mapData = None

