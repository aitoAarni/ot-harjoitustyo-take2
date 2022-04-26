import unittest
import os
from tools.storage_interface import add_score, get_map, get_map_names, get_map_stats
from config import MAP_DIRECOTORY_PATH
from tools.database import get_database_connection, initialize_database


class TestStorageInterface(unittest.TestCase):
    def setUp(self) -> None:
        os.system(f"rm {MAP_DIRECOTORY_PATH}/*")
        os.system(f'echo "---" > {MAP_DIRECOTORY_PATH}/test_map')

    def test_get_map_stats(self):
        initialize_database()
        os.system(f"touch {MAP_DIRECOTORY_PATH}/level")
        add_score('level', 1, 1)
        maps = get_map_stats()
        self.assertListEqual(maps, [('level', 1, 1), ('test_map', 0, 0)])

    def test_get_map_names(self):
        result = get_map_names()[0]
        self.assertEqual(result, 'test_map')

    def test_get_map_with_valid_parameter(self):
        result = get_map('test_map')
        self.assertEqual(type(result), list)

    def test_get_map_with_invalid_parameter(self):
        result1 = get_map("")
        result2 = get_map("not_a_map")
        self.assertTupleEqual((result1, result2), (None, None))

    def test_add_score(self):
        initialize_database()
        add_score('level', 1, 1)
        add_score('level', 2, 2)
        conn = get_database_connection()
        cursor = conn.cursor()
        query = cursor.execute(
            "SELECT name, attempts, wins FROM stats WHERE name='level';").fetchall()
        stats = [(row['name'], row['attempts'], row['wins']) for row in query]
        self.assertListEqual(stats, [('level', 3, 3)])
