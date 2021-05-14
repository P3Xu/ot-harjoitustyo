"""
Moduuli, joka huolehtii kaikista tarvittavista alustustoimenpiteistä ennen sovelluksen
ensimmäistä käynnistämistä.
"""

from init_database import initialize_database
from init_default_set import initialize_default_set
from init_wishlist_dir import initialize_wishlist_dir

def build():
    initialize_database()
    initialize_default_set()
    initialize_wishlist_dir()

if __name__ == "__main__":
    build()
