import os
from os import listdir
from os.path import isfile, join
from tools.database import get_database_connection
from config import MAP_DIRECOTORY_PATH


def get_map_stats():
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT name, attempts, wins FROM stats;')
    stats = cursor.fetchall()
    names = get_map_names()
    maps_list = [(row['name'], row['attempts'], row['wins']) for row in stats]
    map_names = [row['name'] for row in stats]

    for name in names:
        if name not in map_names:
            maps_list.append((name, 0, 0))
    maps_list.sort()
    return maps_list


def get_map_names():
    path = MAP_DIRECOTORY_PATH
    maps = [f for f in listdir(path) if isfile(join(path, f))]
    return maps


def get_map(name: str):
    if name:
        path = os.path.join(MAP_DIRECOTORY_PATH, name)
        level = []
        try:
            with open(path, encoding="utf-8") as file:
                for line in file:
                    level.append(line[:-1])
            return level
        except FileNotFoundError:
            return None
    return None


def add_score(name: str, attempts: int, win: int):
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT attempts, wins FROM stats WHERE name='{name}';")
    result = cursor.fetchone()
    if result:
        old_attempts, old_wins = result['attempts'], result['wins']
        attempts += old_attempts
        win += old_wins
        cursor.execute(
            f"UPDATE stats SET attempts={attempts}, wins={win} WHERE name='{name}';")
    else:
        cursor.execute(
            f"INSERT INTO stats (name, attempts, wins) VALUES ('{name}', {attempts}, {win});")
    connection.commit()
