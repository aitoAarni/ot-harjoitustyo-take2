import unittest
from game_logic.level.level_object import Block, Spike

class TestBlocks(unittest.TestCase):
    def setUp(self):
        self.block = Block(50, 50, 0, 50)

    def test_constructor(self):
        self.assertTupleEqual(self.block.rect.topleft, (0, 0))

    def test_draw_works(self):
        self.block.draw_rect(50, 50)

    def test_update_method_works_with_values(self):
        self.block.update(50, 50)
        self.assertTupleEqual(self.block.rect.topleft, (-50, 50))

    def test_update_method_works_without_values(self):
        self.block.update()
        self.assertTupleEqual(self.block.rect.topleft, (0, 0))

class TestSpikes(TestBlocks):
    def setUp(self):
        self.block = Spike(50, 50, 0, 50)
    
    def test_draw_works(self):
        self.block.draw_tri((0, 255, 255))