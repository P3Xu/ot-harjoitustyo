"""Moduuli, joka alustaa määritellyn hakemiston sovelluksen tulostamille kauppalistoille."""

from pathlib import Path
from config import WISHLIST_DIR_PATH

def initialize_wishlist_dir():
    dir_path = Path(WISHLIST_DIR_PATH)

    if not dir_path.is_dir():
        dir_path.mkdir()

if __name__ == "__main__":
    initialize_wishlist_dir()
