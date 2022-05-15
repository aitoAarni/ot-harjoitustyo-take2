import pygame
from pygame.locals import *


class GameDisplay:
    """class for displaying the game
    """
    def __init__(self, display: pygame.display, sprites):
        """class constructor for GameDisplay

        Args:
            display (pygame.display): display for the game
            sprites (pygame.sprite.Group): all the spites that will be displayed 
        """
        self.display = display
        self.sprite_group = sprites

    def display_game(self):
        """displayes game sprites and updates the screen
        """
        self.display.fill((0, 0, 0))
        self.sprite_group.draw(self.display)
        pygame.display.flip()


class MenuDisplay:
    """class for displaying the menu
    """
    def __init__(self, display: pygame.display, display_group) -> None:
        """class constructor for MenuDisplay

        Args:
            display (pygame.display): display for the game
            display_group (pygame.sprite.Group): all the spirtes that will be displayed
        """
        self.display = display
        self.display_group = display_group

    def display_menu(self, light_up_button: pygame.Rect):
        """display sprites, draws surfaces and udates screen

        Args:
            light_up_button (pygame.Rect): surface to light up a button
        """
        self.display.fill((0, 0, 0))
        self.display_group.draw(self.display)
        if light_up_button:
            light = pygame.Surface(light_up_button.size)
            light.set_alpha(100)
            light.fill((0, 50, 155))
            self.display.blit(light, light_up_button.topleft)
        pygame.display.flip()
