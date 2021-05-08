from entities.meal import Meal
from entities.ingredient import Ingredient
from services.generator import GeneratorService
from repositories.meal_repository import MealRepository
from repositories.menu_repository import MenuRepository
from repositories.user_repository import UserRepository

class Controller:
    """Kontrolleri-luokka."""

    def __init__(self, meal_repository = None, menu_repository = None, user_repository = None):
        if not meal_repository and not menu_repository and not user_repository:
            self.meal_repository = MealRepository()
            self.user_repository = UserRepository()
            self.menu_repository = MenuRepository(self.meal_repository)
        else:
            self.meal_repository = meal_repository
            self.menu_repository = menu_repository
            self.user_repository = user_repository

        self.user = None

    def generate_menu(self):
        menu = GeneratorService(self.meal_repository, self.user).generate()

        self.menu_repository.insert_menu(menu, self.user)

    def fetch_meals(self):
        return self.meal_repository.find_all_meals(self.user)

    def fetch_ingredients(self):
        return self.meal_repository.find_all_ingredients(self.user)

    def fetch_menu(self):
        menu = self.menu_repository.find_menu(self.user)

        if isinstance(menu, int):
            return None

        return menu

    def add_ingredients(self, ingredients):
        inserted_ingredients = []

        for ingredient in ingredients:
            check = self._check_duplicates_item(ingredient)

            if isinstance(check, list):
                inserted_ingredient = self.meal_repository.insert_ingredient(
                    Ingredient(ingredient.capitalize())
                )

                inserted_ingredients.append(inserted_ingredient)

            else:
                inserted_ingredients.append(check)

        return inserted_ingredients

    def add_meal(self, meal, ingredients):
        check = self._check_duplicates_item(meal, True)

        if isinstance(check, list):
            ingredients = self.add_ingredients(ingredients)

            self.meal_repository.insert_meal(Meal(meal.capitalize(), ingredients), self.user)

            return 0

        return -1

    def add_user(self, username, password):
        check = self._check_duplicates_username(username)

        if not check:
            return self.user_repository.add_user(username, password)

        return None

    def login_user(self, username, password):
        result = self.user_repository.find_by_username(username)

        if (not result or username not in result.name or password not in result.password):
            return None

        self.user = result

        return 0

    def _check_duplicates_item(self, item, which=False):
        if which is False:
            return self.meal_repository.find_single_ingredient(str(item), self.user)

        return self.meal_repository.find_single_meal(str(item), self.user)

    def _check_duplicates_username(self, username):
        return self.user_repository.find_by_username(username)
