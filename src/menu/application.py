import pygame
from game_logic.main_loop import GameInputLoop
class Application:
    def __init__(self) -> None:
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen_info = pygame.display.Info()
        self.display = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        
    def run(self):
        game = GameInputLoop(self.display, self.screen_info.current_w, self.screen_info.current_h, self.clock, level=1)
        game.loop()