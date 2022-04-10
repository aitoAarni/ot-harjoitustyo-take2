import pygame
from menu.main_menu import MainMenu
from game_logic.main_loop import GameInputLoop

class Application:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((1280, 720))
        self.wwidth, self.height = pygame.display.get_surface().get_size()

    def game(self, level):
        while True:
            game = GameInputLoop(self.display, self.wwidth,
                                 self.height, self.clock, level=level)
            game.loop()
            if game.exit_to_main_menu:
                break

    def menu(self):
        menu = MainMenu(self.display, self.wwidth, self.height, self.clock)
        map_name = menu.loop()
        return map_name

    def run(self):
        while True:
            map_name = self.menu()
            self.game(map_name)
