import pygame


class Player(pygame.sprite.Sprite):
    # pylint: disable=too-many-instance-attributes
    # disabled (12/8) because the used attributes seem convenient and expedient
    """Represents the player in the game

    Attributes:
        block_size (int): how big the player square is
        color (tuple, optional): player color. Defaults to (80, 255, 0).
    """
    def __init__(self, block_size, color=(80, 255, 0)) -> None:
        """Class constructor

        Args:
            block_size (int): how big the player square is
            color (tuple, optional): player color. Defaults to (80, 255, 0).
        """
        super().__init__()
        self.block_size = block_size
        self.image = pygame.Surface((block_size, block_size))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self._jump_velocity_index = 0
        self.falling_velocity_index = 0
        self.speed_y = 0
        self.__speed_x = block_size / 6
        self.do_jump = False
        self.falling_status = False
        self.__generate_vel()
        self.__create_rect(color)
        self.mask = pygame.mask.from_surface(self.image)

    def __generate_vel(self):
        self.jump_velocities = [self.block_size/(i//2) for i in range(8, 23)]
        self.falling_velocities = [
            self.block_size/(i//2) for i in range(8, 23)]
        self.falling_velocities.reverse()

    def __create_rect(self, color):
        pygame.draw.rect(self.image, color,
                         pygame.Rect(0, 0, self.block_size, self.block_size),
                         width=self.block_size//8)

    @property
    def speed_x(self):
        return self.__speed_x

    def position_player_for_start(self, height):
        """sets the y and x cordinates for the player

        Args:
            height (int): player's height
        """
        if self.block_size <= height:
            x_pos = self.block_size * 7
            y_pos = height-self.block_size
            self.rect.move_ip(x_pos, y_pos)

    def jump(self):
        """makes the player jump or end the jump
        """
        if self._jump_velocity_index == len(self.jump_velocities)-1:
            self._jump_velocity_index = 0
            self.do_jump = False
            return
        self.rect.y -= self.jump_velocities[self._jump_velocity_index]
        self._jump_velocity_index += 1
        self.do_jump = True
        return

    def falling(self):
        """makes the player fall
        """
        if self.falling_status:
            self.rect.y += self.falling_velocities[self.falling_velocity_index]
            if self.falling_velocity_index < len(self.falling_velocities)-1:
                self.falling_velocity_index += 1

    def next_position_while_falling(self):
        """gets the next position where the player will be while falling

        Returns:
            rect: returns player's next position's rect
        """
        down_by = self.falling_velocities[self.falling_velocity_index]
        rect = self.rect.copy()
        rect.x += self.speed_x
        rect.y += down_by
        return rect

    def update(self, y=None):  # pylint: disable=invalid-name
        # invalid-name disabled, because I think x and y are appropriate names in this instance
        # even though they are no snake_case
        """updates the y cordinate of the player

        Args:
            y (int, optional): updates the y cordinate of the player. Defaults to None.
        """
        if y:
            self.rect.y += y
