"""Moduuli, joka luo kaikille käyttäjille käytettävän CSV-oletuskirjaston ruokalajeille."""

from pathlib import Path
from config import DEFAULT_SET_FILE_PATH
from entities.user import User
from entities.meal_set import MealSet as default_set

def initialize_default_set():
    """Alustaa käytettävän CSV-tiedoston ja kirjoittaa vakio-ruokalajit sinne."""

    file_path = Path(DEFAULT_SET_FILE_PATH)

    if not file_path.is_file():
        file_path.touch()

    if len(file_path.read_bytes()) == 0:
        with file_path.open(mode="w") as file:
            for meal in default_set().create_meals(User("Pelle", "Hermanni", 1)):
                for ingredient in meal.ingredients:
                    file.write(f"{meal};{ingredient}"+"\n")

if __name__ == "__main__":
    initialize_default_set()
