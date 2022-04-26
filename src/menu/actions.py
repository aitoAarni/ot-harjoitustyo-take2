import pygame


class MenuActions:
    def __init__(self, buttons) -> None:
        self.buttons = buttons
        self.mouse = Mouse()

    def check_for_mouse_hover(self, mouse_movement):
        rect = None
        self.mouse.rect.center = mouse_movement
        active_button = pygame.sprite.spritecollide(
            self.mouse, self.buttons, False)
        if active_button:
            rect = active_button[0].rect
        return rect

    def mouse_click_on_button(self):
        pressed_button = pygame.sprite.spritecollide(
            self.mouse, self.buttons, False)
        if pressed_button:
            return pressed_button[0].action
        return None


class Mouse(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.rect = pygame.Rect(0, 0, 1, 1)
