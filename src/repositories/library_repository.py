from entities.meal import Meal
from config import DEFAULT_SET_FILE_PATH

class LibraryRepository:

    def read_meals(self, csv_file=False):
        """LISÄTTY "R" POISTA JOS EI TOIMI"""
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
