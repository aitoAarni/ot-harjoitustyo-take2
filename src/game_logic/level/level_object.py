import pygame
from pygame.locals import *

class Object(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color) -> None:
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos_x, pos_y)
    
    def move(self, x, y):
        pass
