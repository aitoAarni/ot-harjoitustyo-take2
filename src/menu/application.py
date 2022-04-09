from menu.main_menu import MainMenu
from game_logic.main_loop import GameInputLoop
import pygame

class Application:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((1280, 720))
        self.w, self.h = pygame.display.get_surface().get_size()
        print(self.w, self.h)
        self.play_game = True        

    def game(self, level=1):
        game = GameInputLoop(self.display, self.w, self.h, self.clock, level=1)
        game.loop()
        self.play_game = game.game_over


    def menu(self):
        menu = MainMenu(self.display, self.w, self.h, self.clock)
        menu.loop()

    def run(self):
        while True:
            if self.play_game:
                self.game()
                self.menu()
