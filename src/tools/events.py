import sys
import pygame


class GameEvents:
    """class that facilitates input event detection while game is running
    """
    def __init__(self) -> None:
        """GameEvents constructor 
        """
        self.player_jump = False

    def events(self):
        """detects input events

        Returns:
            bool: if user exits game
        """
        exit_to_menu = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player_jump = True
                if event.key == pygame.K_ESCAPE:
                    exit_to_menu = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.player_jump = False
        return exit_to_menu


class MenuEvents:
    """facilitates event detection in the lobby
    """
    def __init__(self) -> None:
        """MenuEvents constructor
        """
        self.mouse_click = False
        self.mouse_movement_pos = None
        self.end_app = False

    def events(self):
        """detects input events
        """
        self.mouse_click = False
        self.mouse_movement_pos = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.end_app = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.end_app = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.mouse_click = True

            if event.type == pygame.MOUSEMOTION:
                self.mouse_movement_pos = event.pos
