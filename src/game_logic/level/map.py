from pygame.locals import *
import pygame
from game_logic.level.level_object import Object

class Map:
    def __init__(self, n, height, level=1):
        self.n = n
        self.height = height
        self.level_list = [
            '                                                                                               ',
            '                                                                                               ',
            '                                                                                               ',
            '                                           -                                                   ',
            '                      -                                          ---                           ',
            '                  -      -                                                        ---          ',
            '------------------------------------------------------------------------------------------------'
        ]
        self.create_map()

    def create_map(self):
        self.blocks = pygame.sprite.Group()
        height = self.height - len(self.level_list) * self.n
        for i, row in enumerate(self.level_list):
            y = height + (1+i)*self.n
            for x, block in enumerate(row):
                x *= self.n
                sprite = None
                if block == "-":
                    sprite = Object(self.n, self.n, x, y, ((255, 0, 0)))
                if sprite: self.blocks.add(sprite)



    def create_diplay_group(self):
        return self.blocks.copy()
    