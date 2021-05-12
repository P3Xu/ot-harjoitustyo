import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

DATABASE_FILENAME = os.getenv('DATABASE_FILENAME') or 'food.db'
DATABASE_FILE_PATH = os.path.join(dirname, '..', 'data', DATABASE_FILENAME)

DEFAULT_SET_FILENAME = os.getenv('DEFAULT_SET_FILENAME') or 'default.csv'
DEFAULT_SET_FILE_PATH = os.path.join(dirname, '..', 'data', DEFAULT_SET_FILENAME)

WISHLIST_DIRNAME = os.getenv('WISHLIST_DIRNAME') or 'wishlists'
WISHLIST_DIR_PATH = os.path.join(dirname, '..', 'data', WISHLIST_DIRNAME)
