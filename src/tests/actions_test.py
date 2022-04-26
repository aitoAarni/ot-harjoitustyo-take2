import unittest
import pygame
from menu.actions import MenuActions
from menu.buttons import Button


class TestActions(unittest.TestCase):
    def setUp(self) -> None:
        b = Button(100, 100, 'Play')
        b.rect.topleft = (0, 0)
        button_group = pygame.sprite.Group(b)
        self.actions = MenuActions(button_group)

    def test_check_for_mouse_hover_when_on_button(self):
        result = self.actions.check_for_mouse_hover((5, 5))
        self.assertEqual(result, pygame.Rect(0, 0, 100, 100))

    def test_check_for_mouse_hover_when_not_on_button(self):
        result = self.actions.check_for_mouse_hover((200, 100))
        self.assertEqual(result, None)

    def test_mouse_click_on_button_when_on_button(self):
        answer = self.actions.mouse_click_on_button()
        self.assertEqual(answer, 'Play')

    def test_mouse_click_on_button_when_not_on_button(self):
        self.actions.mouse.rect.bottomleft = (200, 0)
        answer = self.actions.mouse_click_on_button()
        self.assertEqual(answer, None)
