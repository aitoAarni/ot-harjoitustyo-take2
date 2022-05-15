import pygame


class Button(pygame.sprite.Sprite):
    """Class that represents buttons
    """
    def __init__(self, width, height, text, color=(0, 255, 0), font='Helvetica.ttf') -> None:
        """Class constructor for Button

        Args:
            width (int): screen width
            height (int): screen height
            text (str): defines button's use
            color (tuple, optional): color of the button. Defaults to (0, 255, 0).
            font (str, optional): font used on the button's text. Defaults to 'Helvetica.ttf'.
        """
        super().__init__()
        pygame.font.init()
        self.image = pygame.Surface((width, height))
        self.action = text
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

    def align(self, pos_x, pos_y):
        """aligns the button midtop on the screen

        Args:
            pos_x (int): x position
            pos_y (int): y position
        """
        self.rect.midtop = (pos_x, pos_y)
