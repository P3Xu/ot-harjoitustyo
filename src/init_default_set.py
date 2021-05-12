from pathlib import Path
from config import DEFAULT_SET_FILE_PATH
from tests.assets.meal_set import MealSet as default_set
from entities.user import User

def initialize_default_set():
    file_path = Path(DEFAULT_SET_FILE_PATH)

    if file_path.is_file():
        file_path.unlink()

    file_path.touch()

    with file_path.open(mode="w") as file:
        for meal in default_set().create_meals(User("Pelle", "Hermanni", 1)):
            for ingredient in meal.ingredients:
                file.write(f"{meal};{ingredient}"+"\n")

if __name__ == "__main__":
    initialize_default_set()
