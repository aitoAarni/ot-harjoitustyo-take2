import pygame
from pygame.locals import *

class GameDisplay:
    def __init__(self, display: pygame.display, sprites):
        self.display = display
        self.sprite_group = sprites


    def display_game(self):
        self.display.fill((0,0,0))
        self.sprite_group.draw(self.display)
        pygame.display.flip()


class MenuDisplay:
    def __init__(self, display: pygame.display, buttons) -> None:
        self.display = display
        self.buttons = buttons
    
    def display_menu(self, map=None):
        self.display.fill((0, 0, 0))
        self.buttons.draw(self.display)
        pygame.display.flip()
        