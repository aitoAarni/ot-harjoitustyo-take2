from pathlib import Path
from pygame.locals import *
import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, width, height, text, color=(0, 255, 0), font='Helvetica.ttf') -> None:
        super().__init__()
        pygame.font.init()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.__create_graphic(color, width, height)
        self.__create_text(color, self.rect.width-5, self.rect.height-5, text, font)

    def __create_graphic(self, color, width, height):
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height), width=3)

    def __create_text(self, color, width, height, text, font):
        font = pygame.font.Font('data/fonts/' + font, 32)
        text_original = font.render(text, True, color)
        text = pygame.transform.scale(text_original, (width / 2, height / 2))
        self.image.blit(text, (self.rect.width/2 - width/4, self.rect.height/2 - height / 4))

    def align_button(self, x, y):
        self.rect.midtop = (x, y)


    def button_active(self):
        surf = pygame.image((self.rect.size))
        surf.fill((255, 255, 255, 75))
        self.image.blit(surf, 0, 0)


class PlayButton(Button):
    def __init__(self, width, height, color=(0, 255, 0)) -> None:
        super().__init__(width, height, "Play",color)

class ArrowButton(Button):
    def __init__(self, width, height, color=(0, 255, 0)) -> None:
        super().__init__(width, height, color)
