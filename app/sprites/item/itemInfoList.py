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
        self.item['bone'] = ItemInfo('bone')
        self.item['carrot'] = ItemInfo('carrot')
        self.item['apple'] = ItemInfo('apple')
        self.item['gun'] = ItemInfo('gun')
        self.item['pokerChip'] = ItemInfo('pokerChip')
        self.item['totem'] = ItemInfo('totem')

        # Set Link
        #Tier 1 link
        self.item['cupcake'].linkList.append(['rabbit', 'rainbowRabbit'])
        self.item['goldBar'].linkList.append(['rabbit', 'tigerRabbit'])
        self.item['carrot'].linkList.append(['rabbit', 'muscularRabbit'])

        # Tier 2 link
        self.item['goldBar'].linkList.append(['rainbowRabbit', 'chocoRabbit'])
        self.item['carrot'].linkList.append(['rainbowRabbit', 'tigerRabbit'])
        self.item['cupcake'].linkList.append(['tigerRabbit', 'tiger'])
        self.item['cupcake'].linkList.append(['muscularRabbit', 'alienRabbit'])
        self.item['goldBar'].linkList.append(['muscularRabbit', 'pimpRabbit'])

        # Tier 10 link
        self.item['horseshoe'].linkList.append(['tiger', 'horse'])
        self.item['bone'].linkList.append(['tiger', 'lion'])
        self.item['apple'].linkList.append(['tiger', 'hornedTiger'])

        #Tier 20 link
        self.item['bone'].linkList.append(['horse', 'dog'])
        self.item['apple'].linkList.append(['horse', 'muscularHorse'])
        self.item['horseshoe'].linkList.append(['lion', 'cosmicLion'])
        self.item['apple'].linkList.append(['lion', 'smartLion'])
        self.item['horseshoe'].linkList.append(['hornedTiger', 'unicorn'])
        self.item['bone'].linkList.append(['hornedTiger', 'saberToothTiger'])

        #Tier 100 link
        self.item['gun'].linkList.append(['unicorn', 'dragonUnicorn'])
        self.item['pokerChip'].linkList.append(['unicorn', 'pimpUnicorn'])

        #Tier 200 link
        self.item['totem'].linkList.append(['dragonUnicorn', 'dragon'])
