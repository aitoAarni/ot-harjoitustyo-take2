import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, color, n, w, h) -> None:
        super().__init__()
        self.n = n
        self.width = w
        self.height = h
        self.image = pygame.Surface([n, n])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self._jump_velocity = 0

    def position_player_for_start(self, height):
        if 0+self.n <= height <= self.height:
            x_pos = self.n * 7
            y_pos = height-self.n
            self.rect.move_ip(x_pos, y_pos)

    def jump(self):
        velocities = [3, 3, 3, 3, 3, 3, 3, 3]
        if self._jump_velocity == len(velocities):
            self._jump_velocity = 0
            return False
        self.rect.y -= velocities[self._jump_velocity]
        return True
    
