from entities.user import User
from entities.meal import Meal
from entities.menu import Menu
from entities.ingredient import Ingredient
from services.generator import GeneratorService
from repositories.meal_repository import MealRepository
from repositories.menu_repository import MenuRepository
from repositories.user_repository import UserRepository
from repositories.library_repository import LibraryRepository

class Controller:
    """Kontrolleri-luokka."""

    def __init__(self,
        meal_repository = MealRepository(),
        menu_repository = None,
        user_repository = UserRepository(),
        library_repository = LibraryRepository()):

        self.meal_repository = meal_repository
        self.menu_repository = menu_repository
        self.user_repository = user_repository
        self.lib_repository = library_repository

        if not self.menu_repository:
            self.menu_repository = MenuRepository(self.meal_repository)

        self.user = None

    def generate_menu(self):
        menu = GeneratorService(self.meal_repository, self.user).generate()

        if isinstance(menu, Menu):
            self.menu_repository.insert_menu(menu)

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
            ingredient = ingredient.capitalize()
            check = self.meal_repository.fetch_item_id(ingredient, False)

            if check:
                db_ingredient = Ingredient(ingredient, check)
            else:
                db_ingredient = self.meal_repository.insert_ingredient(
                    Ingredient(ingredient)
                )

            inserted_ingredients.append(db_ingredient)

        return inserted_ingredients

    def add_meal(self, meal, ingredients):
        db_ingredients = self.add_ingredients(ingredients)

        meal = self.meal_repository.insert_meal(
            Meal(meal.capitalize(), db_ingredients),
            self.user
        )

        return meal

    def add_user(self, username, password, config_file=False):
        check = self._check_duplicates_username(username)

        if not check:
            if config_file:
                meals = self.lib_repository.read_meals(config_file)
            else:
                meals = self.lib_repository.read_meals()

            uid = self.user_repository.add_user(username, password)

            self.user = User(username, password, uid)
            self._insert_default_meals(meals)

            return uid

        return None

    def login_user(self, username, password):
        result = self.user_repository.find_by_username(username)

        if (not result or username not in result.name or password not in result.password):
            return None

        self.user = result

        return 0

    def _insert_default_meals(self, meals):
        for meal in meals:
            self.add_meal(meal.name, meal.ingredients)

    def _check_duplicates_username(self, username):
        return self.user_repository.find_by_username(username)
