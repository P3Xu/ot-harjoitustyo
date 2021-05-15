"""Moduuli, joka määrittelee käytettävät konfiguraatiot .env-tiedoston pohjalta."""

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

WISHLIST_DIRNAME = os.getenv('WISHLIST_DIRNAME') or 'not_set'
WISHLIST_DIR_PATH = os.path.join(dirname, '..', 'data', WISHLIST_DIRNAME)

ICON_NAME = os.getenv('ICON_NAME') or 'none'
ICON_PATH = os.path.join(dirname, ICON_NAME)

MESSAGE_SHOWTIME = os.getenv('MESSAGE_SHOWTIME') or 4500
