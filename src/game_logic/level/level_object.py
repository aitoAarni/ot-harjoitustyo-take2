import pygame
from pygame.locals import *

class Block(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color=(255, 255, 0)) -> None:
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.color = color
        self.rect.bottomleft = (pos_x, pos_y)
        self.draw_rect(width, height)
    
    def draw_rect(self, width, height):
        pygame.draw.rect(self.image, self.color, pygame.Rect(0, 0, width, height), width=1)

    def update(self, x=None, y=None):
        if x:
            self.rect.x -= x
        if y:
            self.rect.y += y

class Spike(pygame.sprite.Sprite):
    def __init__(self, width, height, pos_x, pos_y, color=(0, 255, 255)) -> None:
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (pos_x, pos_y)
        self.draw_tri(color)
        self.mask = pygame.mask.from_surface(self.image)

    def draw_tri(self, color):
        pygame.draw.polygon(self.image, color, ((self.rect.width / 2, self.rect.height / 2),
                                                    (0, self.rect.height), 
                                                    (self.rect.width, self.rect.height)), width=1)

    def update(self, x=None, y=None):
        if x:
            self.rect.x -= x
        if y:
            self.rect.y += y
            
