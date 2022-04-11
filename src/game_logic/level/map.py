import pygame
from tools.db_interface import get_map
from game_logic.level.level_object import Spike, Block as Object


class Map:
    def __init__(self, block_size, height, level):
        self.block_size = block_size
        self.level_list = get_map(level)
        self.create_map(height)
        self.visible_sprites = pygame.sprite.Group()
        self.visible_blocks = pygame.sprite.Group()
        self.visible_spikes = pygame.sprite.Group()

    def create_map(self, heigth):
        self.blocks = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        total_height = heigth - len(self.level_list) * self.block_size
        for i, row in enumerate(self.level_list):
            y_coord = total_height + (1+i)*self.block_size
            for j, block in enumerate(row):
                x_coord = j * self.block_size
                sprite = None
                spike = None
                if block == "-":
                    sprite = Object(self.block_size, self.block_size, x_coord, y_coord,
                                ((255, 0, 0)))
                elif block == "¤":
                    spike = Spike(self.block_size, self.block_size, x_coord, y_coord)
                if sprite:
                    self.blocks.add(sprite)
                elif spike:
                    self.spikes.add(spike)
        self.map_objects = pygame.sprite.Group()
        self.map_objects.add(self.blocks.sprites())
        self.map_objects.add(self.spikes.sprites())
