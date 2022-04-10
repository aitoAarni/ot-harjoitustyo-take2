import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, width, height, text, color=(0, 255, 0), font='Helvetica.ttf') -> None:
        super().__init__()
        pygame.font.init()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.__create_graphic(color, width, height)
        self.__create_text(color, self.rect.width-5,
                           self.rect.height-5, text, font)

    def __create_graphic(self, color, width, height):
        pygame.draw.rect(self.image, color, pygame.Rect(
            0, 0, width, height), width=3)

    def __create_text(self, color, width, height, text, font):
        font = pygame.font.Font('data/fonts/' + font, 32)
        text_original = font.render(text, True, color)
        text = pygame.transform.scale(text_original, (width / 2, height / 2))
        self.image.blit(text, (self.rect.width/2 - width /
                        4, self.rect.height/2 - height / 4))

    def align_button(self, pos_x, pos_y):
        self.rect.midtop = (pos_x, pos_y)


class PlayButton(Button):
    def __init__(self, width, height, color=(0, 255, 0)) -> None:
        super().__init__(width, height, "Play", color)
        self.action = "play"


class ArrowButton(Button):
    def __init__(self, width, height, color=(0, 255, 0)) -> None:
        super().__init__(width, height, color)
