#Impors form Pygame are diffrent here, care. Let's leave it to that for now...
import pygame
import sys

class EventHandlerMenuPause():
    def __init__(self):
        pass

    def eventHandle(self,optionList,selector,close):
        self.optionList = optionList
        self.selector = selector
        self.close = close
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.optionList[self.selector.vPos].deselect()
                    self.selector.moveUp()
                    self.optionList[self.selector.vPos].select()
                elif event.key == pygame.K_DOWN:
                    self.optionList[self.selector.vPos].deselect()
                    self.selector.moveDown()
                    self.optionList[self.selector.vPos].select()
                elif event.key == pygame.K_SPACE:
                    self.optionList[self.selector.vPos].doOption()
                elif event.key == pygame.K_RETURN:
                    self.optionList[self.selector.vPos].doOption()
                elif event.key == pygame.K_BACKSPACE:
                    self.close()
                    self.optionList[self.selector.vPos].selectQuit()
                elif event.key == pygame.K_ESCAPE:
                    self.close()
                    self.optionList[self.selector.vPos].selectQuit()

