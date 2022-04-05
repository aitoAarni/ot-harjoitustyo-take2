import pygame
from pygame.locals import *

class Map:
    def __init__(self, n, level=1):
        self.n = n

    def create_diplay_group(self):
        return pygame.sprite.Group()