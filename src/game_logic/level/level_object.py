import pygame
from pygame.locals import *

class Object(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color) -> None:
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (pos_x, pos_y)
    
    def update(self, x=None, y=None):
        if x:
            self.rect.x -= x
        if y:
            self.rect.y += y