from tkinter import N
import pygame
from pygame.locals import *
from ui.game_display import GameDisplay
from game_logic.player import Player
from game_logic.level.map import Map

class GameInputLoop:
    def __init__(self, screen, w, h, clock, level) -> None:
        self.display = screen
        self.width = w
        self.height = h
        self.n = w // 20
        self.clock = clock
        self.initialize_game(level=level)
        self.draw_game = GameDisplay(self.display, self.display_sprites)

    def initialize_game(self, level=1):
        self.map = Map(self.n, level=level)
        self.player = Player((255, 255, 255), self.n, self.width, self.height)
        self.player.position_player_for_start(self.height)
        self.generate_sprite_groups()
        

    def generate_sprite_groups(self):
        self.display_sprites = self.map.create_diplay_group()
        print(type(self.player))
        self.display_sprites.add(self.player)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
    def loop(self):
        while True:
            self.events()
            self.draw_game.display_game()
            self.clock.tick(60)