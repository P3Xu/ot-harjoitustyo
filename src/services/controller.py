from entities.meal import Meal
from entities.ingredient import Ingredient
from services.generator import GeneratorService
from repositories.meal_repository import MealRepository
from repositories.menu_repository import MenuRepository

class Controller:
    """Kontrolleri-luokka."""

    def __init__(self):
        self.meal_repository = MealRepository()
        self.menu_repository = MenuRepository(self.meal_repository)

    def generate_menu(self):
        menu = GeneratorService(self.meal_repository).generate()

        self.menu_repository.insert_menu(menu)

    def fetch_meals(self):
        return self.meal_repository.find_all_meals()

    def fetch_ingredients(self):
        return self.meal_repository.find_all_ingredients()

    def fetch_menu(self):
        menu = self.menu_repository.find_menu()

        if isinstance(menu, int):
            return None

        return menu.meals

    def add_ingredients(self, ingredients):
        inserted_ingredients = []

        for ingredient in ingredients:
            check = self._check_item(ingredient)

            if isinstance(check, list):
                inserted_ingredient = self.meal_repository.insert_ingredient(
                    Ingredient(ingredient.capitalize())
                )

                inserted_ingredients.append(inserted_ingredient)

            else:
                inserted_ingredients.append(check)

        return inserted_ingredients

    def add_meal(self, meal, ingredients):
        check = self._check_item(meal, True)

        if isinstance(check, list):
            ingredients = self.add_ingredients(ingredients)

            self.meal_repository.insert_meal(Meal(meal.capitalize(), ingredients))

            return 0

        return -1

    def add_user(self, username, password):
        pass

    def _check_item(self, item, which=False):
        if which is False:
            return self.meal_repository.find_single_ingredient(str(item))

        return self.meal_repository.find_single_meal(str(item))
