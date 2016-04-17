import pygame
import os
from app.sprites.pet.pet import Pet

class PetList:
    def __init__(self):
        self.pet = {}

        #All pet
        #Tier 1
        self.pet["rabbit"] = Pet('rabbit', 'lapin.png', 250)

        #Tier2
        self.pet["rainbowRabbit"] = Pet('rainbowRabbit', 'lapin-multicouleur.png', 250)
        self.pet["tigerRabbit"] = Pet('tigerRabbit','lapin-tigre.png', 250)
        self.pet["muscularRabbit"] = Pet('muscularRabbit','lapin-steroide.png', 250)

        #Tier3
        self.pet["chocoRabbit"] = Pet('chocoRabbit','lapin-chocolat.png', 250)
        self.pet["carrotRabbit"] = Pet('carrotRabbit','lapin-carotte.png', 250,deadEnd=False,eventTrigger=True)
        self.pet["orangeRabbit"] = Pet('orangeRabbit', 'lapin-tigre-carotte.png', 250)
        self.pet["alienRabbit"] = Pet('alienRabbit','lapin-alien.png', 250)
        self.pet["pimpRabbit"] = Pet('pimpRabbit', 'lapin-pimp.png', 250)

        #Tier10
        self.pet["tiger"] = Pet('tiger', 'tigre.png', 275)

        #Tier20
        self.pet["horse"] = Pet('horse', 'cheval.png', 325)
        self.pet["lion"] = Pet('lion','lion.png', 300)
        self.pet["hornedTiger"] = Pet('hornedTiger','tigre-licorne.png', 320)

        #Tier30
        self.pet["dog"] = Pet('dog','chien.png', 275)
        self.pet["muscularHorse"] = Pet('muscularHorse','cheval-pomme.png', 325)
        self.pet["cosmicLion"] = Pet('cosmicLion','lion-cosmique.png', 300)
        self.pet["smartLion"] = Pet('smartLion','lion-savant.png', 300)
        self.pet["saberToothTiger"] = Pet('saberToothTiger', 'tigre_a_dent_sabre.png', 275)

        #Tier100
        self.pet["unicorn"] = Pet('unicorn','licorne.png', 325)
        self.pet["dragonUnicorn"] = Pet('dragonUnicorn','licorne-dragon.png', 325)
        self.pet["pimpUnicorn"] = Pet('pimpUnicorn','licorne-pimp.png', 325)

        self.pet["dragon"] = Pet('dragon', 'dragon.png', 400)