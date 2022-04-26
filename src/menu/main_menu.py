import pygame
from menu.buttons import Button
from menu.actions import MenuActions
from tools.storage_interface import get_map
from tools.events import MenuEvents
from ui.game_display import MenuDisplay
from ui.menu_render import MapStats


class MainMenu:
    # pylint: disable=too-many-instance-attributes
    # 11 attributes seem to be a reasonable amount in this case
    def __init__(self, screen, width, height, clock) -> None:
        self.display = screen
        self.width = width
        self.height = height
        self.clock = clock
        self.light_up_button = None
        self.continue_looping = True
        self.create_buttons()
        self.events = MenuEvents()
        self.draw_menu = MenuDisplay(screen, self.display_group)
        self.actions = MenuActions(self.buttons)
        self.map_level = None

    def create_buttons(self):
        play_button = Button(self.width / 3, self.width / 15, 'Play')
        self.map_stats = MapStats(self.width / 3, self.height / 10)
        map_left = Button(self.width / 15, self.width / 15, '<')
        map_right = Button(self.width / 15, self.width / 15, '>')
        quit_game = Button(self.width / 3, self.width / 15, 'Quit')

        self.buttons = pygame.sprite.Group(
            play_button, map_left, map_right, quit_game)
        self.display_group = pygame.sprite.Group(
            (self.map_stats, play_button, quit_game))

        gap = self.height // 10
        current_height = self.width / 15
        for sprite in self.display_group:
            sprite.align(self.width / 2, current_height)
            current_height += sprite.rect.height
            current_height += gap
        self.display_group.add(map_left, map_right)
        map_left.rect.topright = (
            self.map_stats.rect.left - gap, self.map_stats.rect.top)
        map_right.rect.topleft = (
            self.map_stats.rect.right + gap, self.map_stats.rect.top)

    def button_actions(self):
        if self.events.mouse_movement_pos:
            self.light_up_button = self.actions.check_for_mouse_hover(
                self.events.mouse_movement_pos)
        if self.events.mouse_click:
            action = self.actions.mouse_click_on_button()
            if action:
                action = action.lower()
                if action == 'play':
                    self.start_game()
                elif action == '<':
                    self.map_stats.previous_map()
                elif action == '>':
                    self.map_stats.next_map()
                elif action == "quit":
                    self.events.end_app = True

    def start_game(self):
        self.map_level = get_map(self.map_stats.current_map)
        self.continue_looping = False

    def loop(self):
        while self.continue_looping and not self.events.end_app:
            self.events.events()
            self.button_actions()
            self.draw_menu.display_menu(self.light_up_button)
            self.clock.tick(60)
        return self.map_level, self.map_stats.current_map, self.events.end_app
