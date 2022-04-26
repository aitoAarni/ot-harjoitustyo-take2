import unittest
from game_logic.level.map import Map


class TestMap(unittest.TestCase):
    def setUp(self):
        self.map = Map(100, 100, ["-¤f "])

    def test_block_size_is_correct(self):
        self.assertEqual(self.map.block_size, 100)

    def test_map_generated_right(self):
        self.assertTupleEqual((len(self.map.blocks.sprites()), len(self.map.spikes.sprites()),
                               len(self.map.finish.sprites())), (1, 1, 1))
