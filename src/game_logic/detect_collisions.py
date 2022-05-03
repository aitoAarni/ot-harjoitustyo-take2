import pygame


class CheckCollisions:
    """Class for checking collisions between sprites

    Attributes:
        player (Sprite): the player object
        blocks (spirte.Group): sprite group of bocks
        spikes (sprite.Group): sprite group of spikes
        finish (sprite.Group): spirte group of finishes
    """
    def __init__(self, player, blocks, spikes, finish):
        """Class constructor

        Args:
            player (Sprite): the player object
            blocks (spirte.Group): sprite group of bocks
            spikes (sprite.Group): sprite group of spikes
            finish (sprite.Group): spirte group of finishes
        """
        self.player = player
        self.blocks = blocks
        self.spikes = spikes
        self.finish = finish

    def falling_collision_detection(self) -> int:
        """When player is falling this will detect if the player hits a block and
            does the game end because of that hit

        Returns:
            int: 0 means no hit, 1 means landed on top of a block, -1 means hit the side of the block
        """
        next_pos = Object(self.player.next_position_while_falling())
        collision_blocks = pygame.sprite.spritecollide(
            next_pos, self.blocks, False)
        if collision_blocks:
            block = min(collision_blocks, key=lambda a: (
                a.rect.y, a.rect.x))  # leftmost and highest block
            # create linear funktio to see if block lands on the side of the block or on top of it
            k = (next_pos.rect.top-self.player.rect.top) / \
                (next_pos.rect.left-self.player.rect.left)
            # we will see in which y coordinate the line is
            # while it is at the same width as the block
            y_pos = k * (block.rect.left - next_pos.rect.right) + \
                next_pos.rect.bottom

            if block.rect.top < y_pos:
                self.player.rect.bottom = next_pos.rect.bottom
                # this means game over, because the line goes under the topleft corner of the block
                return -1
            # player landed safely on a block
            self.player.rect.bottom = block.rect.top + 1
            # next_pos.rect.left + (block.rect.top-next_pos.rect.top)/k
            return 1
        return 0

    def detect_collision(self) -> int:
        """Detects if player collides whit blocks

        Returns:
            int: 0 means no collision, 1 means block is on top of a block, -1 player hit the side of a block
        """
        # detect if the player hits hits a block
        collision_blocks = pygame.sprite.spritecollide(
            self.player, self.blocks, False)
        if collision_blocks:
            for block in collision_blocks:
                if block.rect.top+1 < self.player.rect.bottom:
                    return -1
            return 1
        return 0

    def spike_collision(self) -> bool:
        """detects if player collides with a spike

        Returns:
            bool: returns boolean if the player collided with a spike
        """
        if pygame.sprite.spritecollide(
                self.player, self.spikes, False, collided=pygame.sprite.collide_mask):
            return True
        return False

    def finish_collision(self) -> bool:
        """detects if player collides with a finish block

        Returns:
            bool: returns boolean if the player collided with a finish block
        """
        if pygame.sprite.spritecollide(self.player, self.finish, False):
            return True
        return False


class Object(pygame.sprite.Sprite):
    """Class to represent the next position of the player object

    
    Attributes:
        rect (tuple): represents the players cordinates and size
    """
    def __init__(self, rect) -> None:
        """class constructor

        Args:
            rect (tuple): represents the players cordinates and size
        """
        super().__init__()
        self.rect = rect
