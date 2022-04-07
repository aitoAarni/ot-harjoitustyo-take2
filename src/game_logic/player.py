import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    def __init__(self, color, n, w) -> None:
        super().__init__()
        self.n = n
        self.image = pygame.Surface((n, n))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self._jump_velocity_index = 0   
        self._falling_velocity_index = 0
        self.speed_y = 0
        self.__speed_x = n /6 
        self.do_jump = False
        self.falling_status = False
        self.generate_vel()

    def generate_vel(self):
        self.jump_velocities = [self.n/(i//2) for i in range(8, 23)]
        # self.jump_velocities.append(0)
        print(self.jump_velocities)
        self.falling_velocities = [self.n/(i//2) for i in range(8, 23)]
        # self.falling_velocities.append(0)
        self.falling_velocities.reverse()

    @property
    def speed_x(self):
        return self.__speed_x
    
    def stop_x(self):
        self.__speed_x = 0

    def position_player_for_start(self, height):
        if 0+self.n <= height:
            x_pos = self.n * 7
            y_pos = height-self.n
            self.rect.move_ip(x_pos, y_pos)
        
    def jump(self):
        if self._jump_velocity_index == len(self.jump_velocities)-1:
            self._jump_velocity_index = 0
            self.do_jump = False
            return 
        self.rect.y -= self.jump_velocities[self._jump_velocity_index]
        self._jump_velocity_index += 1
        self.do_jump = True
        return
    
    def falling(self):
        if self.falling_status:
            self.rect.y += self.falling_velocities[self._falling_velocity_index]
            if self._falling_velocity_index < len(self.falling_velocities)-1:
                self._falling_velocity_index += 1


    def next_position_while_falling(self):
        down_by = self.falling_velocities[self._falling_velocity_index]
        rect = self.rect.copy()
        rect.x += self.speed_x
        rect.y += down_by
        return rect

    def update(self, x=None, y=None):
        if x:
            self.rect.x -= x
        if y:
            self.rect.y += y