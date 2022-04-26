import unittest
import pygame
from game_logic.detect_collisions import *
from game_logic.level.level_object import Block, Spike, Finish
from game_logic.player import Player


class CollisionsTest(unittest.TestCase):
    def setUp(self):
        self.player = Player(100)
        blocks = pygame.sprite.Group(Block(100, 100, 0, 100))
        spike = pygame.sprite.Group(Spike(100, 100, 0, 50))
        finish = pygame.sprite.Group(Finish(100, 0, 100))
        self.cols = CheckCollisions(self.player, blocks, spike, finish)

    def test_falling_collision_detection_no_hit(self):
        self.player.rect.topleft = (500, 500)
        answer = self.cols.falling_collision_detection()
        self.assertEqual(answer, 0)

    def test_falling_collision_detection_landed_on_top(self):
        self.player.rect.bottomright = (5, -5)
        answer = self.cols.falling_collision_detection()
        self.assertEqual(answer, 1)

    def test_falling_collision_detection_landed_on_side(self):
        self.player.rect.bottomright = (-10, -5)
        answer = self.cols.falling_collision_detection()
        self.assertEqual(answer, -1)

    def test_detect_collision_no_hit(self):
        self.player.rect.topleft = (500, 500)
        answer = self.cols.detect_collision()
        self.assertEqual(answer, 0)

    def test_detect_collision_on_top(self):
        self.player.rect.bottomright = (50, 1)
        answer = self.cols.detect_collision()
        self.assertEqual(answer, 1)

    def test_detect_collision_hit_to_side(self):
        self.player.rect.bottomright = (5, 100)
        answer = self.cols.detect_collision()
        self.assertEqual(answer, -1)

    def test_spike_collision_no_hit(self):
        self.player.rect.bottomright = (200, 100)
        answer = self.cols.spike_collision()
        self.assertEqual(answer, False)

    def test_spike_collision_hit(self):
        self.player.rect.bottomright = (50, 100)
        answer = self.cols.spike_collision()
        self.assertEqual(answer, True)

    def test_finish_collision_no_hit(self):
        self.player.rect.bottomright = (200, 100)
        answer = self.cols.finish_collision()
        self.assertEqual(answer, False)

    def test_finish_collision_hit(self):
        self.player.rect.bottomright = (50, 100)
        answer = self.cols.finish_collision()
        self.assertEqual(answer, True)
