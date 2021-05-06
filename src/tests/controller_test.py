import unittest
from entities.meal import Meal
from entities.menu import Menu
from entities.user import User
from entities.ingredient import Ingredient
from entities.default_set import DefaultSet
from repositories.meal_repository import MealRepository
from repositories.menu_repository import MenuRepository
from repositories.user_repository import UserRepository
from services.controller import Controller

class TestControllerRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.meal_repository = MealRepository()
        cls.user_repository = UserRepository()
        cls.menu_repository = MenuRepository(cls.meal_repository)
        cls.controller = Controller(cls.meal_repository, cls.menu_repository, cls.user_repository)

        cls.meals = DefaultSet().meals
        cls.ingredients = DefaultSet().ingredients
        cls.meal_relations = DefaultSet().relations

        cls.mealset = cls._prepare_meals()
        cls.users = cls._prepare_users()

    @classmethod
    def _prepare_meals(cls):
        meals = []

        for i, meal in enumerate(cls.meals):
            ingredients = []

            for relation in cls.meal_relations:
                (meal_id, ingredient_id) = relation

                if meal_id == i:
                    ingredients.append(cls.ingredients[ingredient_id])

            meals.append((meal, ingredients))

        return meals

    @classmethod
    def _prepare_users(cls):
        users = []

        users.append(User("Paavo", "Pesusieni666_"))
        users.append(User("MacGyver", "_Käpykranaatti13"))
        users.append(User("Gunnar", "Surströmming<3"))

        return users

    def test_a_empty_all(self):
        self.meal_repository.empty_tables()
        self.menu_repository.initialize_menus()
        self.user_repository.empty_users_table()

        self.assertIsNone(self.controller.fetch_menu())
        self.assertEqual(len(self.controller.fetch_meals()), 0)
        self.assertEqual(len(self.controller.fetch_ingredients()), 0)

    def test_b_add_meal(self):
        last_pieces = self.mealset.pop()
        (piece_meal, piece_ingredients) = last_pieces

        for pieces in self.mealset:
            (meal, ingredients) = pieces

            self.controller.add_meal(meal, ingredients)

        self.assertEqual(self.controller.add_meal(piece_meal, piece_ingredients), 0)
        self.assertEqual(self.controller.add_meal(piece_meal, piece_ingredients), -1)

        results = self.controller.fetch_meals()

        self.assertEqual(len(results), len(self.meals))
        self.assertEqual(results[0].name, self.meals[0])

    def test_c_add_ingredients(self):
        results = self.controller.fetch_ingredients()
        ingredients = self.ingredients

        self.assertEqual(len(results), len(ingredients))
        self.assertEqual(results[0].name, ingredients[0])
        self.assertIsInstance(self.controller.add_ingredients(ingredients), list)
        self.assertEqual(len(self.controller.add_ingredients(ingredients)), len(ingredients))

    def test_d_fetch_meals(self):
        results = self.controller.fetch_meals()
        (meal, ingredients) = self.mealset[0]

        self.assertIsInstance(results[0], Meal)
        self.assertEqual(results[0].name, meal)
        self.assertIsInstance(results[0].ingredients[0], Ingredient)
        self.assertEqual(len(results[0].ingredients), len(ingredients))
        self.assertEqual(results[0].ingredients[0].name, ingredients[0])

    def test_e_fetch_ingredients(self):
        results = self.controller.fetch_ingredients()

        self.assertIsInstance(results[0], Ingredient)
        self.assertEqual(results[-1].name, self.ingredients[-1])

    def test_f_generate_and_fetch_menu(self):
        self.controller.generate_menu()

        result = self.controller.fetch_menu()

        self.assertEqual(len(result.meals), 7)
        self.assertIsInstance(result, Menu)
        self.assertIsInstance(result.meals[0], Meal)
        self.assertIsInstance(result.meals[0].ingredients[0], Ingredient)

    def test_g_add_user(self):
        returns = [self.controller.add_user(user.name, user.password) for user in self.users]

        self.assertEqual(returns[0], 1)
        self.assertEqual(returns[1], 2)
        self.assertEqual(returns[2], 3)
        self.assertIsNone(self.controller.add_user(self.users[0].name, self.users[0].password))
        self.assertEqual(len(self.user_repository.find_all_users()), len(self.users))
