import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height) -> None:
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self._jump_velocity = 0

    def jump(self):
        velocities = [3, 3, 3, 3, 3, 3, 3, 3]
        if self._jump_velocity == len(velocities):
            self._jump_velocity = 0
            return False
        self.rect.y -= velocities[self._jump_velocity]
        return True
    
