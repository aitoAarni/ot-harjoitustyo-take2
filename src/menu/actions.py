import pygame


class MenuActions:
    """Class to detect actions in the menu
    
       Attributes:
            buttons (pygame.sprite.Sprite): an object to track the mouse
    """
    def __init__(self, buttons) -> None:
        """MenuActions' constructor

        Args:
            buttons (pygame.sprite.Sprite): an object to track the mouse
        """
        self.buttons = buttons
        self.mouse = Mouse()

    def check_for_mouse_hover(self, mouse_movement):
        """see if mouse is hovering on top of a button

        Args:
            mouse_movement (tuple): mouse's position

        Returns:
            pygame.sprite.Rect: returns the button that has been hovered over
        """
        rect = None
        self.mouse.rect.center = mouse_movement
        active_button = pygame.sprite.spritecollide(
            self.mouse, self.buttons, False)
        if active_button:
            rect = active_button[0].rect
        return rect

    def mouse_click_on_button(self):
        """Detects if a click is on a button

        Returns:
            str: returns the button object's action string that defines what actions should be taken
        """
        pressed_button = pygame.sprite.spritecollide(
            self.mouse, self.buttons, False)
        if pressed_button:
            return pressed_button[0].action
        return None


class Mouse(pygame.sprite.Sprite):
    """Sprite for the mouse
    """
    def __init__(self) -> None:
        self.rect = pygame.Rect(0, 0, 1, 1)
