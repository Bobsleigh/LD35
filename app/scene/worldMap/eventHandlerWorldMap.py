from pygame import event,QUIT,KEYDOWN,K_RIGHT,K_LEFT,K_UP,K_DOWN,K_SPACE,K_RETURN
from sys import exit

class EventHandlerWorldMap():
    def __init__(self):
        pass

    def eventHandle(self,player):
        for dummyEv in event.get():
            if dummyEv.type == QUIT:
                exit()
            elif dummyEv.type == KEYDOWN:
                if dummyEv.key == K_RIGHT: #Does nothing for now...
                    player.moveRight()
                elif dummyEv.key == K_LEFT: #Does nothing for now...
                    player.moveLeft()
                elif dummyEv.key == K_UP:
                    player.moveUp()
                elif dummyEv.key == K_DOWN:
                    player.moveDown()
                elif dummyEv.key == K_SPACE:
                    pass
                elif dummyEv.key == K_RETURN:
                    pass
        pass
