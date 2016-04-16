from app.creatureScreen.eventHandlerCreatureScreen import EventHandlerCreatureScreen
import pygame

class CreatureScreen:
    def __init__(self, screen):
        self.screen = screen
        self.screen.fill((255,255,255))


        self.eventHandler = EventHandlerCreatureScreen()

        self.nextScene = None

    def mainLoop(self):
        self.sceneRunning = True
        while self.sceneRunning:
            self.eventHandler.eventHandle()
            self.draw()  # Drawer in THIS file, below

    def draw(self):
        pygame.display.flip()

    def close(self):
        self.sceneRunning = False #To stop creatureScreen running

    def backToMain(self):
        self.nextScene = TITLE_SCREEN
        #self.menuPause.close()
        self.close()