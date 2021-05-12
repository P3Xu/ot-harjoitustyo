from datetime import datetime
from pathlib import Path
from entities.meal import Meal
from config import DEFAULT_SET_FILE_PATH, WISHLIST_DIR_PATH

class LibraryRepository:

    def read_meals(self, csv_file=False):
        path = csv_file if csv_file else open(DEFAULT_SET_FILE_PATH, "r")
        meals = []

        with path as file:
            new_meal = None
            ingredients = []

            for row in file:

                row = row.replace('\n', '')
                parts = row.split(';')

                meal = parts[0]
                ingredient = parts[1]

                if not new_meal:
                    new_meal = meal

                if meal in new_meal:
                    ingredients.append(ingredient)
                else:
                    meals.append(Meal(new_meal, ingredients.copy()))
                    ingredients.clear()
                    new_meal = meal
                    ingredients.append(ingredient)

            meals.append(Meal(new_meal, ingredients))

        return meals

    def write_wishlist(self, items):
        timestamp = datetime.now().strftime("%d_%m_%H%M%S")
        file_name = "/kauppalista"+timestamp+".txt"
        file_path = Path(WISHLIST_DIR_PATH+file_name)

        file_path.touch()

        with file_path.open(mode = "w") as file:
            for item in items:
                file.write(f"{item}"+"\n")

        return file_name
