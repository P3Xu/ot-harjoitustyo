"""Moduuli, joka alustaa määritellyn hakemiston sovelluksen tulostamille kauppalistoille.

Käytetään testaamisessa kauppalistan tulostamiseen.
"""

from pathlib import Path
from config import WISHLIST_DIR_PATH

def initialize_wishlist_dir():
    check = WISHLIST_DIR_PATH.split("/")

    if not "not_set" in check[-1]:
        dir_path = Path(WISHLIST_DIR_PATH)

        if not dir_path.is_dir():
            dir_path.mkdir()

if __name__ == "__main__":
    initialize_wishlist_dir()
