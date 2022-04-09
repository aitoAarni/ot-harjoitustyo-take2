from pygame.locals import *
import pygame
from game_logic.level.level_object import Spike, Block as Object

class Map:
    def __init__(self, n, height, level=1):
        self.n = n
        self.height = height
        self.level_list = level
        self.create_map ()

    def create_map(self):
        self.blocks = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        height = self.height - len(self.level_list) * self.n
        for i, row in enumerate(self.level_list):
            y = height + (1+i)*self.n
            for x, block in enumerate(row):
                x *= self.n
                sprite = None
                spike = None
                if block == "-":
                    sprite = Object(self.n, self.n, x, y, ((255, 0, 0)))
                elif block == "¤":
                    spike = Spike(self.n, self.n, x, y)
                if sprite: self.blocks.add(sprite)
                elif spike: self.spikes.add(spike)
        self.map_objects = pygame.sprite.Group()
        self.map_objects.add(self.blocks.sprites())
        self.map_objects.add(self.spikes.sprites())
        self.visible_sprites = pygame.sprite.Group()
        self.visible_blocks = pygame.sprite.Group()
        self.visible_spikes = pygame.sprite.Group()

