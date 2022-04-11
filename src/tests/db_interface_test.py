import unittest
from tools.db_interface import get_map, get_map_names

class TestDBInterface(unittest.TestCase):
    
    def test_get_map_names(self):
        result = get_map_names()
        self.assertEqual(type(result), list)

    def test_get_map_with_valid_parameter(self):
        result = get_map()
        self.assertEqual(type(result), list)

    def test_get_map_with_invalid_parameter(self):
        result = get_map("")
        self.assertEqual(result, None)