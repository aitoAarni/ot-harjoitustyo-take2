import pygame
from pygame.locals import *

class Map:
    def __init__(self, width, height, level=1):
        self.width = width
        self.height = height

    def create_diplay_group(self):
        return pygame.sprite.Group()