import pygame
import os
from app.settings import *

from app.sprites.pet.pet import Pet

class PetList:
    def __init__(self):
        self.pet = {}

        #All pet
        #Tier 1
        self.pet["rabbit"] = Pet('rabbit','cute and fluffy rabbit', 'lapin.png', 250)

        #Tier2
        self.pet["rainbowRabbit"] = Pet('rainbowRabbit','colored rabbit', 'lapin-multicouleur.png', 250)
        self.pet["tigerRabbit"] = Pet('tigerRabbit','rabbit with a tiger tail','lapin-tigre.png', 250)
        self.pet["muscularRabbit"] = Pet('muscularRabbit','douchebag rabbit','lapin-steroide.png', 250)

        #Tier3
        self.pet["chocoRabbit"] = Pet('chocoRabbit','rabbit made of chocolate','lapin-chocolat.png', 250,kind=DEAD_END)
        self.pet["carrotRabbit"] = Pet('carrotRabbit','playful rabbit','lapin-carotte.png', 250,kind=DEAD_END,eventTrigger=True)
        self.pet["orangeRabbit"] = Pet('orangeRabbit','weird orange rabbit', 'lapin-tigre-carotte.png', 250,kind=DEAD_END)
        self.pet["alienRabbit"] = Pet('alienRabbit','rabbit form outer space','lapin-alien.png', 250,kind=DEAD_END,eventTrigger=True)
        self.pet["pimpRabbit"] = Pet('pimpRabbit','rapper rabbit', 'lapin-pimp.png', 250,kind=DEAD_END)

        #Tier10
        self.pet["tiger"] = Pet('tiger','wild tiger', 'tigre.png', 275,kind=KEY_ANIMAL)

        #Tier20
        self.pet["horse"] = Pet('horse','gentle horse', 'cheval.png', 325)
        self.pet["lion"] = Pet('lion','fierce lion', 'lion.png', 300)
        self.pet["hornedTiger"] = Pet('hornedTiger','horned tiger', 'tigre-licorne.png', 320)

        #Tier30
        self.pet["dog"] = Pet('dog','nice dog', 'chien.png', 275,kind=DEAD_END,eventTrigger=True)
        self.pet["muscularHorse"] = Pet('muscularHorse','powerful horse', 'cheval-pomme.png', 325,kind=DEAD_END,eventTrigger=True)
        self.pet["cosmicLion"] = Pet('cosmicLion','lion from another dimension', 'lion-cosmique.png', 300,kind=DEAD_END)
        self.pet["smartLion"] = Pet('smartLion','smart lion', 'lion-savant.png', 300,kind=DEAD_END)
        self.pet["saberToothTiger"] = Pet('saberToothTiger','saber\-toothed cat', 'tigre_a_dent_sabre.png', 275,kind=DEAD_END)

        #Tier100
        self.pet["unicorn"] = Pet('unicorn', 'legendary unicorn', 'licorne.png', 325,kind=KEY_ANIMAL)
        self.pet["dragonUnicorn"] = Pet('dragonUnicorn', 'winged unicorn', 'licorne-dragon.png', 325)
        self.pet["pimpUnicorn"] = Pet('pimpUnicorn', 'badass unicorn', 'licorne-pimp.png', 325,kind=DEAD_END,eventTrigger=True)

        self.pet["dragon"] = Pet('dragon', 'dragon', 'dragon.png', 400,kind=WINNER)