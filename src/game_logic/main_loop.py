from pygame.locals import *
from ui.game_display import GameDisplay
from game_logic.player import Player
from game_logic.level.map import Map
from tools.events import GameEvents
from game_logic.detect_collisions import CheckCollisions
import pygame

class GameInputLoop:
    def __init__(self, screen, w, h, clock, level) -> None:
        self.display = screen
        self.width = w
        self.height = h
        self.n = w // 20
        self.clock = clock
        self.initialize_game(level=level)
        self.draw_game = GameDisplay(self.display, self.display_sprites)
        self.game_over = False

    def initialize_game(self, level=1):
        self.map = Map(self.n, self.height, level=level)
        self.player = Player((255, 255, 255), self.n, self.width)
        self.player.position_player_for_start(self.height//2)
        self.generate_sprite_groups()
        self.events = GameEvents()
        self.collisions = CheckCollisions(self.player, self.map.blocks)

        

    def generate_sprite_groups(self):
        self.display_sprites = self.map.create_diplay_group()
        self.display_sprites.add(self.player)

            
    def move_sprites(self):
        if self.player.falling_status:
            outcome = self.collisions.falling_collision_detection()
            if outcome == 1:
                self.player.falling_status = False
                self.player._falling_velocity_index = 0
            elif outcome == -1:
                self.game_over = True
            else:
                self.player.falling_status = True
                self.player.falling()
        else:
            outcome2 = self.collisions.detect_collision()
            if outcome2 == -1:  # player hit a block
                print('shee')
                self.game_over = True

            elif outcome2 == 1:  # player travelling on a block
                if self.events.player_jump:
                    self.player.do_jump = True
                    self.player.jump()
            else:
                if self.player.do_jump:
                    self.player.jump()
                else:
                    self.player.falling_status = True  # player isn't touching a block
        self.map.blocks.update(self.player.speed_x)
    
    def move_screen(self):
        move_delta = (self.player.rect.y - (self.height - self.height / 3)) / 10
        self.display_sprites.update(y=-move_delta)

    def game_events(self):
        self.events.events()
        if not self.game_over:
            self.move_sprites()
            self.move_screen()

    def loop(self):
        while True:
            if not self.game_over:
                self.draw_game.display_game()
            self.game_events()
            self.clock.tick(60)