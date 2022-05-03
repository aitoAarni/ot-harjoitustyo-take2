import pygame
from game_logic.level.level_object import Spike, Finish, Block as Object


class Map:
    """Class for creating a map for the game

    Atrributes:
        block_size (int): how much every map object will take space
        height (int): how many pixels the screen's height is
        level (list): list of strings that represents the map
    """
    
    def __init__(self, block_size, height, level):
        """Class constructor

        Args:
            block_size (int): how much every map object will take space
            height (int): how many pixels the screen's height is
            level (list): list of strings that represents the map
        """
        self.block_size = block_size
        self.level_list = level
        self.create_map(height)
        self.visible_sprites = pygame.sprite.Group()
        self.visible_blocks = pygame.sprite.Group()
        self.visible_spikes = pygame.sprite.Group()
        self.visible_finish = pygame.sprite.Group()

    def create_map(self, heigth):
        """Creates map objects according to a list of strings

        Args:
            heigth (int): height of the screen
        """
        self.blocks = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.finish = pygame.sprite.Group()
        total_height = heigth - len(self.level_list) * self.block_size
        for i, row in enumerate(self.level_list):
            y_coord = total_height + (1+i)*self.block_size
            for j, block in enumerate(row):
                x_coord = j * self.block_size
                if block == "-":
                    self.blocks.add(Object(self.block_size, self.block_size, x_coord, y_coord,
                                    ((255, 0, 0))))
                elif block == "¤":
                    self.spikes.add(Spike(self.block_size,
                                          self.block_size, x_coord, y_coord))
                elif block.lower() == "f":
                    self.finish.add(Finish(self.block_size, x_coord, y_coord))

        self.map_objects = pygame.sprite.Group()
        self.map_objects.add(self.blocks.sprites())
        self.map_objects.add(self.spikes.sprites())
        self.map_objects.add(self.finish.sprites())
