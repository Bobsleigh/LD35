import pygame
import os
from app.settings import *


class MusicFactory:
    def __init__(self, typeScene=None, secondOption=None):

        self.nameMusic = None
        if typeScene == TITLE_SCREEN:
            self.nameMusic = 'MainTheme'
        elif typeScene == WORLD_MAP:
            self.nameMusic = 'MainTheme'
        elif typeScene == PET_SCREEN:
            self.nameMusic = 'MainTheme'
        elif typeScene == PLATFORM_SCREEN:
            if secondOption == "LevelDesert":
                self.nameMusic = 'Desert'
            if secondOption == "LevelIndian":
                self.nameMusic = 'Indians'
            if secondOption == "LevelSaloon":
                self.nameMusic = 'Saloon'
            if secondOption == "LevelSheriff":
                self.nameMusic = 'Sheriff'

        if self.nameMusic is not None:
            pygame.mixer.music.load(os.path.join('music_pcm', self.nameMusic + '.wav'))
            if typeScene == PET_SCREEN:
                pygame.mixer.music.set_volume(0.7)
            else:
                pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()

