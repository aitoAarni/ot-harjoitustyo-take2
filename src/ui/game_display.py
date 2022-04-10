import pygame
from pygame.locals import *


class GameDisplay:
    def __init__(self, display: pygame.display, sprites):
        self.display = display
        self.sprite_group = sprites

    def display_game(self):
        self.display.fill((0, 0, 0))
        self.sprite_group.draw(self.display)
        pygame.display.flip()


class MenuDisplay:
    def __init__(self, display: pygame.display, buttons) -> None:
        self.display = display
        self.buttons = buttons

    def display_menu(self, light_up_button: pygame.Rect, map=None):
        self.display.fill((0, 0, 0))
        self.buttons.draw(self.display)
        if light_up_button:
            light = pygame.Surface(light_up_button.size)
            light.set_alpha(100)
            light.fill((0, 50, 155))
            self.display.blit(light, light_up_button.topleft)
        pygame.display.flip()
