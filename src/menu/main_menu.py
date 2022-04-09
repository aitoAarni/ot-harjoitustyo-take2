from menu.buttons import PlayButton, ArrowButton
from ui.game_display import MenuDisplay
from menu.actions import MenuActions
from tools.events import MenuEvents
from tools.db_interface import get_map
import pygame

class MainMenu:
    def __init__(self, screen, w, h, clock) -> None:
        self.display = screen
        self.width = w
        self.height = h
        self.clock = clock
        self.map_name = None  # TODO
        self.light_up_button = None
        self.continue_looping = True
        self.create_buttons()
        self.events = MenuEvents()
        self.draw_menu = MenuDisplay(screen, self.buttons)
        self.actions = MenuActions(self.buttons)

    def create_buttons(self):
        p = PlayButton(self.width / 3, self.width / 15)
        self.buttons = pygame.sprite.Group(p)
        gap = self.height // 50
        for i, button in enumerate(self.buttons):
            button.align_button(self.width / 2, (i+1) * (button.rect.height + gap))
            

    def button_actions(self):
        if self.events.mouse_movement_pos:
            self.light_up_button =  self.actions.check_for_mouse_hover(self.events.mouse_movement_pos)
        if self.events.mouse_click:
            action = self.actions.mouse_click_on_button
        if action:
            if action == 'play':
                self.start_game()


    def start_game(self):
        self.continue_looping = False
        get_map(self.map_name)


    def loop(self):
        while self.continue_looping: 
            self.events.events()
            self.button_actions()
            self.draw_menu.display_menu(self.light_up_button)
            self.clock.tick(60)
