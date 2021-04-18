from repositories.meal_repository import MealRepository
from repositories.menu_repository import MenuRepository
from services.generator import GeneratorService

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
            return ["Generoi ruokalista ensin!"]

        return self.menu_repository.find_menu().get_meals()

    def add_ingredients(self, ingredients):
        ids = []

        for ingredient in ingredients:
            check = self._check_item(ingredient)

            if len(check) > 0:
                ids.append(check[0]['id'])
            else:
                ids.append(self.meal_repository.insert_ingredient(ingredient))

        return ids

    def add_meal(self, meal, ingredients):
        check = self._check_item(meal, True)

        if len(check) == 0:
            ingredient_ids = self.add_ingredients(ingredients)
            meal_id = self.meal_repository.insert_meal(meal)
            relations = [(meal_id, ingredient_id) for ingredient_id in ingredient_ids]

            self.meal_repository.update_relations(relations)

            return 0

        return -1

    def _check_item(self, item, which=False):
        if which is False:
            return self.meal_repository.find_single_ingredient(str(item))

        return self.meal_repository.find_single_meal(str(item))
