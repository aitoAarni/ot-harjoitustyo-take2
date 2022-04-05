import pygame
from game_logic.main_loop import GameInputLoop
class Application:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((700,500))
        self.w, self.h = pygame.display.get_surface().get_size()
        
    def run(self):
        game = GameInputLoop(self.display, self.w, self.h, self.clock, level=1)
        game.loop()