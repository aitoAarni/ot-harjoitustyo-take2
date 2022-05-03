import unittest
import pygame
from game_logic.game_loop import GameInputLoop


class GameLoopTest(unittest.TestCase):
    def setUp(self):
        self.game = GameInputLoop(pygame.display.set_mode(
        ), 1920, 1080, pygame.time.Clock(), ["        ", "--¤¤ff  "])

    def test_check_constructor_works(self):
        self.assertEqual(type(self.game), GameInputLoop)

    def test_search_on_screen_sprites(self):
        self.game.map.blocks.sprites()[0].rect.topleft = (2000, 0)
        self.game.map.spikes.sprites()[0].rect.topleft = (2000, 0)
        self.game.map.finish.sprites()[0].rect.topleft = (2000, 0)
        self.game._search_on_screen_sprites()
        self.assertEqual(len(self.game.map.visible_blocks.sprites()), 1)
        self.assertEqual(len(self.game.map.visible_spikes.sprites()), 1)
        self.assertEqual(len(self.game.map.visible_finish.sprites()), 1)

    def test_move_sprites_game_not_ending(self):
        self.game._search_on_screen_sprites()
        answers = []
        self.game.player.rect.topleft = (10, 15)

        self.game.events.player_jump = False
        self.game.player.falling_status = True
        self.game._move_sprites()
        answers.append(self.game.game_over)

        self.game.events.player_jump = False
        self.game.player.falling_status = True
        self.game.player.rect.topleft = (0, 0)
        self.game._move_sprites()
        answers.append(self.game.game_over)

        self.game.events.player_jump = False
        self.game.player.falling_status = False
        self.game.player.rect.topleft = (0, 0)
        self.game._move_sprites()
        answers.append(self.game.game_over)

        self.game.events.player_jump = True
        self.game.player.falling_status = False
        self.game.player.rect.topleft = (0, 0)
        self.game._move_sprites()
        answers.append(self.game.game_over)

        self.game.player.falling_status = False
        self.game.player.do_jump = False
        self.game.player.rect.topleft = (800, 0)
        self.game._move_sprites()
        answers.append(self.game.game_over)

        self.game.player.do_jump = False
        self.game.player.falling_status = False
        self.game._move_sprites()
        answers.append(self.game.game_over)

        self.assertListEqual(answers, [0, 0, 0, 0, 0, 0])
