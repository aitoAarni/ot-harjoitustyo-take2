import pygame
from menu.main_menu import MainMenu
from game_logic.game_loop import GameInputLoop
from tools.storage_interface import add_score


class Application:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((0, 0), flags=pygame.NOFRAME)
        self.width, self.height = pygame.display.get_surface().get_size()

    def game(self, level, level_name):
        map_level = level
        attempts = 0
        win = 0
        try:
            while True:
                game = GameInputLoop(self.display, self.width,
                                     self.height, self.clock, level=map_level[:])
                attempts += 1
                game.loop()
                if game.exit_to_main_menu:
                    break
        finally:
            if game.game_over == 2:
                win = 1
            add_score(level_name, attempts, win)

    def menu(self):
        menu = MainMenu(self.display, self.width, self.height, self.clock)
        map_level, level_name, end_app = menu.loop()
        return map_level, level_name, end_app

    def run(self):
        while True:
            map_level, level_name, end_app = self.menu()
            if end_app:
                break
            self.game(map_level, level_name)
