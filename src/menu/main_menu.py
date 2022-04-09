from menu.buttons import PlayButton, ArrowButton
from ui.game_display import MenuDisplay
from tools.events import MenuEvents
import pygame

class MainMenu:
    def __init__(self, screen, w, h, clock) -> None:
        self.display = screen
        self.width = w
        self.height = h
        self.clock = clock
        self.create_buttons()
        self.events = MenuEvents()
        self.draw_menu = MenuDisplay(screen, self.buttons)

    def create_buttons(self):
        p = PlayButton(self.width / 3, self.width / 15)
        self.buttons = pygame.sprite.Group(p)
        gap = self.height // 50
        for i, button in enumerate(self.buttons):
            button.align_button(self.width / 2, (i+1) * (button.rect.height + gap))
            
    def loop(self):
        while True: 
            self.events.events()
            self.draw_menu.display_menu()
            self.buttons.sprites()[0].button_active()
            self.clock.tick(60)
