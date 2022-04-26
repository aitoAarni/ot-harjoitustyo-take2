import os
from dotenv import load_dotenv


dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass


MAP_DIRECOTRY = os.getenv('MAP_DIRECTORY') or 'maps'

MAP_DIRECOTORY_PATH = os.path.join(dirname, '..', 'data', MAP_DIRECOTRY)

DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'database.sqlite'
DATABASE_FILENAME_PATH = os.path.join(dirname, '..', 'data', DATABASE_FILENAME)
