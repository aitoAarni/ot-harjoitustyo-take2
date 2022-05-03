import pygame


class Block(pygame.sprite.Sprite):
    """Class which represents a block in the game

    Attributes:
        width: block's width
        height: block's height
        pos_x: block's x cordinate
        pos_y: block's y cordinate
        color: block's color
    """
    def __init__(self, width, height, pos_x, pos_y, color=(255, 255, 0)) -> None:
        """class constructor

        Args:
            width: block's width
            height: block's height
            pos_x: block's x cordinate
            pos_y: block's y cordinate
            color: block's color Defaults to (255, 255, 0)
        """
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.color = color
        self.rect.bottomleft = (pos_x, pos_y)
        self._draw_rect(width, height)

    def _draw_rect(self, width, height):
        pygame.draw.rect(self.image, self.color,
                         pygame.Rect(0, 0, width, height), width=1)

    def update(self, x=None, y=None):  # pylint: disable=invalid-name
        # to me x and y are appropriate names here even though they are not snake case
        """method for moving the object's rectangle attribute

        Args:
            x (int, optional): How much the x cordinate will be moved. Defaults to None.
            y (int, optional): How much the y cordinate will be moved. Defaults to None.
        """
        if x:
            self.rect.x -= x
        if y:
            self.rect.y += y


class Spike(pygame.sprite.Sprite):
    """Represents an spike object in the game

    Attributes:
        width (int): width of the spike
        height (int): height of the spike
        pos_x (int): x cordinate of the spike
        pos_y (int): y cordinate of the spike
        color (tuple, optional): color of the spike. Defaults to (0, 255, 255).
    """
    def __init__(self, width, height, pos_x, pos_y, color=(0, 255, 255)) -> None:
        """Class constructor

        Args:
            width (int): width of the spike
            height (int): height of the spike
            pos_x (int): x cordinate of the spike
            pos_y (int): y cordinate of the spike
            color (tuple, optional): color of the spike. Defaults to (0, 255, 255).
        """
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (pos_x, pos_y)
        self._draw_tri(color)
        self.mask = pygame.mask.from_surface(self.image)

    def _draw_tri(self, color):
        pygame.draw.polygon(self.image, color, ((self.rect.width / 2, self.rect.height / 2),
                                                (0, self.rect.height),
                                                (self.rect.width, self.rect.height)), width=1)

    def update(self, x=None, y=None):  # pylint: disable=invalid-name
        # to me x and y are appropriate names here even though they are not snake case
        """method for moving the object's rectangle attribute

        Args:
            x (int, optional): How much the x cordinate will be moved. Defaults to None.
            y (int, optional): How much the y cordinate will be moved. Defaults to None.
        """
        if x:
            self.rect.x -= x
        if y:
            self.rect.y += y
        


class Finish(pygame.sprite.Sprite):
    """Represents the finish in the game

    Attributes:
        edge (int): the width and length of the class
        x_pos (int): x cordinate of the class
        y_pos (int): y codinate of the class
    """
    def __init__(self, edge, x_pos, y_pos) -> None:
        """Class construcotr

        Args:
            edge (int): the width and length of the class
            x_pos (int): x cordinate of the class
            y_pos (int): y codinate of the class
        """

        super().__init__()
        self.image = pygame.Surface((edge, edge))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (x_pos, y_pos)
        self.image.set_alpha(100)
        self.image.fill((0, 255, 0))

    def update(self, x=None, y=None):  # pylint: disable=invalid-name
        # to me x and y are appropriate names here even though they are not snake case
        """method for moving the object's rectangle attribute

        Args:
            x (int, optional): How much the x cordinate will be moved. Defaults to None.
            y (int, optional): How much the y cordinate will be moved. Defaults to None.
        """
        if x:
            self.rect.x -= x
        if y:
            self.rect.y += y
