from game_logic.level.level_object import Spike, Block
from game_logic.player import Player
from game_logic.detect_collisions import CheckCollisions
from game_logic.level.map import Map
from tools.events import GameEvents
from ui.game_display import GameDisplay


class GameInputLoop:
    # pylint: disable=too-many-instance-attributes
    # exit_to_main_menu and game_over seem pretty handy attributes to me
    # that's why there are 10 instead of 8 instance attributes
    """Class that manages the game, while it is played

    Attributes:
        screen (pygame.display): the display for the game
        width (int): screen width
        height (int): screen height
        clock (pygame.time.clock): the clock object, that will manage the tickrate
        level (list): the map for the game
    """
    def __init__(self, screen, width, height, clock, level) -> None:
        """Class constructor

        Args:
            screen (pygame.display): the display for the game
            width (int): screen width
            height (int): screen height
            clock (pygame.time.clock): the clock object, that will manage the tickrate
            level (list): the map for the game
        """
        self.width = width
        self.height = height
        self.clock = clock
        self.exit_to_main_menu = False
        self.__initialize_game(width // 20, level=level)
        self.draw_game = GameDisplay(screen, self.map.visible_sprites)
        self.game_over = 0

    def __initialize_game(self, block_size, level):
        self.map = Map(block_size, self.height, level=level)
        self.player = Player(block_size)
        self.player.position_player_for_start(self.height//2)
        self.events = GameEvents()
        self.collisions = CheckCollisions(
            self.player, self.map.visible_blocks, self.map.visible_spikes, self.map.visible_finish)

    def _search_on_screen_sprites(self):
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
                else:
                    self.map.visible_finish.add(sprite)

    def _move_sprites(self):
        if self.collisions.spike_collision():
            self.game_over = 1
            return

        if self.collisions.finish_collision():
            self.game_over = 2
            self.exit_to_main_menu = True
            return

        if self.player.falling_status:
            outcome = self.collisions.falling_collision_detection()
            if outcome == 1:
                self.player.falling_status = False
                self.player.falling_velocity_index = 0
            elif outcome == -1:
                self.game_over = 1
            else:
                self.player.falling_status = True
                self.player.falling()
        else:
            outcome2 = self.collisions.detect_collision()
            if outcome2 == -1:  # player hit a block
                self.game_over = 1

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

    def __move_screen(self):
        move_delta = (self.player.rect.y -
                      (self.height - self.height / 2)) / 10
        self.map.map_objects.update(y=-move_delta)
        self.player.update(y=-move_delta)

    def __game_events(self):
        self.exit_to_main_menu = self.events.events()
        if not self.game_over:
            self._search_on_screen_sprites()
            self._move_sprites()
            self.__move_screen()

    def loop(self):
        """Loops the game, untile the map is completed of player exits
        """
        while not self.game_over and not self.exit_to_main_menu:
            self.__game_events()
            if not self.game_over:
                self.draw_game.display_game()
            self.clock.tick(60)
