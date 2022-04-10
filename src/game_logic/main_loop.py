from pygame.locals import *
from game_logic.level.level_object import Spike, Block
from ui.game_display import GameDisplay
from game_logic.player import Player
from game_logic.level.map import Map
from tools.events import GameEvents
from game_logic.detect_collisions import CheckCollisions


class GameInputLoop:
    def __init__(self, screen, w, h, clock, level) -> None:
        self.display = screen
        self.width = w
        self.height = h
        self.n = w // 20
        self.clock = clock
        self.exit_to_main_menu = False
        self.initialize_game(level=level)
        self.draw_game = GameDisplay(self.display, self.map.visible_sprites)
        self.game_over = False

    def initialize_game(self, level):
        self.map = Map(self.n, self.height, level=level)
        self.player = Player(self.n, self.width)
        self.player.position_player_for_start(self.height//2)
        self.events = GameEvents()
        self.collisions = CheckCollisions(
            self.player, self.map.visible_blocks, self.map.visible_spikes)

    def search_on_screen_sprites(self):
        self.map.visible_sprites.empty()
        self.map.visible_sprites.add(self.player)
        for sprite in self.map.map_objects:
            if 0 <= sprite.rect.right and self.width >= sprite.rect.left \
                    and 0 <= sprite.rect.bottom and self.height >= sprite.rect.top:
                self.map.visible_sprites.add(sprite)
                if isinstance(sprite, Block):
                    self.map.visible_blocks.add(sprite)
                elif isinstance(sprite, Spike):
                    self.map.visible_spikes.add(sprite)

    def move_sprites(self):
        if self.collisions.spike_collision():
            self.game_over = True
            return

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
        self.map.map_objects.update(self.player.speed_x)

    def move_screen(self):
        move_delta = (self.player.rect.y -
                      (self.height - self.height / 2)) / 10
        self.map.map_objects.update(y=-move_delta)
        self.player.update(y=-move_delta)

    def game_events(self):
        self.exit_to_main_menu = self.events.events()
        if not self.game_over:
            self.search_on_screen_sprites()
            self.move_sprites()
            self.move_screen()

    def loop(self):
        while not self.game_over and not self.exit_to_main_menu:
            print(13)
            if not self.game_over:
                self.draw_game.display_game()
            self.game_events()
            self.clock.tick(60)
