from app.tools.functionTools import *
from app.sprites.item.item import Item


class ItemFactory:
    def __init__(self):
        pass

    def create(self, item):
        iName = seekAtt(item, "name")
        if iName == "item":
            return self.createItemGen(item)
        return self.createItem(item)

    def createItemGen(self, item):
        return Item(item.x, item.y)
