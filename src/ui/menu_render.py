import pygame
from tools.storage_interface import get_map_stats


class MapStats(pygame.sprite.Sprite):
    def __init__(self, width, height, font='Helvetica.ttf') -> None:
        super().__init__()
        pygame.font.init()
        self.color = (0, 255, 0)
        self.__width = width
        self.__height = height
        self.font = pygame.font.Font('data/fonts/' + font, 32)
        self.image = pygame.Surface((round(width), round(height)))
        self.rect = self.image.get_rect()
        self.index = 0
        self.map_stats = get_map_stats()
        self.create_texts()

    def create_texts(self):
        self.image.fill((0, 0, 0))
        stats = self.map_stats[self.index]
        self.current_map = stats[0]
        text_map = self.font.render(stats[0], True, self.color)
        text1 = pygame.transform.scale(
            text_map, (self.__width / 2, self.__height / 2))
        self.image.blit(text1, (self.rect.width/2 - self.__width /
                        4, self.rect.height/2 - self.__height / 4))

        text_attempts = self.font.render(
            'Attempts: ' + str(stats[1]), True, self.color)
        text_wins = self.font.render(
            'Wins: ' + str(stats[2]), True, self.color)

        text2 = pygame.transform.scale(
            text_attempts, (self.__width / 4, self.__height / 4))
        text3 = pygame.transform.scale(
            text_wins, (self.__width / 4, self.__height / 4))

        self.image.blit(text2, (self.rect.width/2 - self.__width /
                        4 - 10, self.rect.height - self.__height / 4))
        self.image.blit(text3, (self.rect.width/2 + 10,
                        self.rect.height - self.__height / 4))

    def next_map(self):
        if self.index == len(self.map_stats) - 1:
            self.index = 0
        else:
            self.index += 1
        self.create_texts()

    def previous_map(self):
        if self.index == 0:
            self.index = len(self.map_stats) - 1
        else:
            self.index -= 1
        self.create_texts()

    def align(self, pos_x, pos_y):
        self.rect.midtop = (pos_x, pos_y)
