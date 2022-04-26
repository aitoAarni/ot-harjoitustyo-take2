import unittest
from game_logic.level.level_object import Block, Spike, Finish


class TestBlocks(unittest.TestCase):
    def setUp(self):
        self.block = Block(50, 50, 0, 50)

    def test_constructor(self):
        self.assertTupleEqual(self.block.rect.topleft, (0, 0))

    def test_draw_works(self):
        self.block._draw_rect(50, 50)

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
        self.block._draw_tri((0, 255, 255))


class TestFinish(unittest.TestCase):
    def setUp(self) -> None:
        self.finish = Finish(100, 0, 0)

    def test_update_func_move(self):
        self.finish.update(10, 10)
        self.assertTupleEqual(self.finish.rect.bottomleft, (-10, 10))

    def test_update_func_without_move(self):
        self.finish.update()
        self.assertTupleEqual(self.finish.rect.bottomleft, (0, 0))
