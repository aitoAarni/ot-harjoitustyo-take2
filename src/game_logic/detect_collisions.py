from pygame.locals import *
import pygame


class CheckCollisions:
    def __init__(self, player, blocks, deadly=None):
        self.player = player
        self.blocks = blocks
        self.deadly = deadly

    def falling_collision_detection(self) -> int:
        next_pos = Object(self.player.next_position_while_falling())
        collision_blocks = pygame.sprite.spritecollide(next_pos, self.blocks, False)
        if collision_blocks:
            block = min(collision_blocks, key=lambda a: (a.rect.y, a.rect.x))  # leftmost and highest block
            # create linear funktio to see if block lands on the side of the block or on top of it
            k = (next_pos.rect.top-self.player.rect.top)/(next_pos.rect.left-self.player.rect.left)
            # we will see in which y coordinate the line is while it is at the same width as the block
            y_pos = k * (block.rect.left - next_pos.rect.right) + next_pos.rect.top
            
            if block.rect.top < y_pos:
                self.player.rect.bottom = next_pos.rect.bottom
                # this means game over, because the line goes under the topleft corner of the block
                return -1
            elif block.rect.top >= y_pos:  # player landed safely on a block
                self.player.rect.bottom = block.rect.top + 1
                # next_pos.rect.left + (block.rect.top-next_pos.rect.top)/k
                return 1
        return 0

    def detect_collision(self):
        collision_blocks = pygame.sprite.spritecollide(self.player, self.blocks, False)
        if collision_blocks:
            for block in collision_blocks:
                if block.rect.top+1 < self.player.rect.bottom:
                    return -1
            return 1
        else:
            return 0


class Object(pygame.sprite.Sprite):
    def __init__(self, rect) -> None:
        super().__init__()
        self.rect = rect