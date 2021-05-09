from entities.meal import Meal
from entities.ingredient import Ingredient

class DefaultSetRepository:
    def __init__(self, file_path):
        self._path = file_path

    def read_meals(self):
        meals = []

        with open(self._path) as file:
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
                    ingredients.append(Ingredient(ingredient))
                else:
                    meals.append(Meal(new_meal, ingredients.copy()))
                    ingredients.clear()
                    new_meal = meal
                    ingredients.append(Ingredient(ingredient))

            meals.append(Meal(new_meal, ingredients))

        return meals
