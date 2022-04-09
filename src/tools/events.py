from curses import KEY_DOWN
import pygame
from pygame.locals import *
import sys

class GameEvents:
    def __init__(self) -> None:
        self.player_jump = False
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player_jump = True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.player_jump = False


class MenuEvents:
    def __init__(self) -> None:
        self.mouse_click_pos = None
        self.mouse_movement_pos = None
        

    def events(self):
        self.mouse_click = False
        self.mouse_movement_pos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse_click = True

            if event.type == pygame.MOUSEMOTION:
                self.mouse_movement_pos = event.pos