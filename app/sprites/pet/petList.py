import pygame
import os
from app.sprites.pet.pet import Pet

class PetList:
    def __init__(self):
        self.pet = {}

        #All pet
        #Tier 1
        self.pet["rabbit"] = Pet('rabbit', pygame.image.load(os.path.join('img', 'lapin.png')), 250)

        #Tier2
        self.pet["rainbowRabbit"] = Pet('rainbowRabbit', pygame.image.load(os.path.join('img', 'lapin-multicouleur.png')), 250)
        self.pet["tigerRabbit"] = Pet('tigerRabbit',
                                        pygame.image.load(os.path.join('img', 'lapin-tigre.png')), 250)
        self.pet["strongRabbit"] = Pet('strongRabbit',
                                        pygame.image.load(os.path.join('img', 'lapin-steroide.png')), 250)

        #Tier3
        self.pet["chocoRabbit"] = Pet('chocoRabbit', pygame.image.load(os.path.join('img', 'lapin-multicouleur.png')), 250)
        self.pet["carrotRabbit"] = Pet('carrotRabbit',
                                        pygame.image.load(os.path.join('img', 'lapin-tigre.png')), 250)
        self.pet["alienRabbit"] = Pet('alienRabbit',
                                        pygame.image.load(os.path.join('img', 'lapin-steroide.png')), 250)
        self.pet["pimpRabbit"] = Pet('alienRabbit',
                                      pygame.image.load(os.path.join('img', 'cochon.png')), 250)


        self.pet["tiger"] = Pet('tiger', pygame.image.load(os.path.join('img', 'tigre.png')), 275)
        self.pet["unicorn"] = Pet('unicorn', pygame.image.load(os.path.join('img', 'licorne.png')), 300)
        self.pet["dragon"] = Pet('dragon', pygame.image.load(os.path.join('img', 'dragon.png')), 400)