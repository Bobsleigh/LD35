import pygame
import os
from app.sprites.item.itemInfo import ItemInfo

class ItemInfoList:
    def __init__(self):
        self.item = {}

        #All item
        self.item['cupcake'] = ItemInfo('cupcake')
        self.item['goldBar'] = ItemInfo('goldBar')
        self.item['horseshoe'] = ItemInfo('horseshoe')
        #self.item['bone'] = ItemInfo('bone')
        #self.item['carrot'] = ItemInfo('carrot')
        #self.item['apple'] = ItemInfo('apple')
        #self.item['gun'] = ItemInfo('gun')
        #self.item['pokerChip'] = ItemInfo('pokerChip')
        #self.item['totem'] = ItemInfo('totem')

        # Set Link
        self.item['cupcake'].linkList.append(['rabbit', 'rainbowRabbit'])
        self.item['goldBar'].linkList.append(['rabbit', 'tigerRabbit'])

        # Test link
        self.item['cupcake'].linkList.append(['unicorn', 'dragonUnicorn'])

        self.item['goldBar'].linkList.append(['unicorn', 'pimpUnicorn'])

        self.item['horseshoe'].linkList.append(['dragonUnicorn', 'dragon'])