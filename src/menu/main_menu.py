import pygame
from menu.buttons import PlayButton
from menu.actions import MenuActions
from ui.game_display import MenuDisplay
from tools.events import MenuEvents


# pylint: disable=too-many-instance-attributes
# 11 attributes seem to be a reasonable amount in this case

class MainMenu:
    def __init__(self, screen, width, height, clock) -> None:
        self.display = screen
        self.width = width
        self.height = height
        self.clock = clock
        self.map_name = None
        self.light_up_button = None
        self.continue_looping = True
        self.create_buttons()
        self.events = MenuEvents()
        self.draw_menu = MenuDisplay(screen, self.buttons)
        self.actions = MenuActions(self.buttons)

    def create_buttons(self):
        play_button = PlayButton(self.width / 3, self.width / 15)
        self.buttons = pygame.sprite.Group(play_button)
        gap = self.height // 50
        for i, button in enumerate(self.buttons):
            button.align_button(self.width / 2, (i+1) *
                                (button.rect.height + gap))

    def button_actions(self):
        if self.events.mouse_movement_pos:
            self.light_up_button = self.actions.check_for_mouse_hover(
                self.events.mouse_movement_pos)
        if self.events.mouse_click:
            action = self.actions.mouse_click_on_button()
            if action:
                if action == 'play':
                    self.start_game()

    def start_game(self):
        self.continue_looping = False

    def loop(self):
        while self.continue_looping:
            self.events.events()
            self.button_actions()
            self.draw_menu.display_menu(self.light_up_button)
            self.clock.tick(60)
        return self.map_name
