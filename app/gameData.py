from app.settings import *

# All the global data for the game and player
class GameData:
    def __init__(self):

        self.inventory = {}
        self.inventory["coin"] = 0
        self.inventory["apple"] = 0