from app.settings import *

#To initialize my pet
import os
import pygame
from app.sprites.pet.petList import PetList
from app.sprites.item.itemInfoList import ItemInfoList


# All the global data for the game and player
class GameData:
    def __init__(self, scene=None):

        #Item info list
        #Go see ItemInfo class in sprite to look at lock, and inventory
        self.itemInfoList = ItemInfoList()

        #For testing purpose
        self.itemInfoList.item['cupcake'].unlock = True
        self.itemInfoList.item['goldBar'].unlock = True

        self.itemInfoList.item['cupcake'].inventory = 10
        self.itemInfoList.item['goldBar'].inventory = 20

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

