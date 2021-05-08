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

        users.append(User("Paavo", "Pesusieni666_", 1))
        users.append(User("MacGyver", "_Käpykranaatti13", 2))
        users.append(User("Gunnar", "Surströmming<3", 3))

        return users

    def test_a_empty_all(self):
        self.meal_repository.empty_tables()
        self.menu_repository.empty_menu_table()
        self.user_repository.empty_users_table()

        self.controller.user = self.users[0]

        self.assertIsNone(self.controller.fetch_menu())
        self.assertEqual(len(self.controller.fetch_meals()), 0)
        self.assertEqual(len(self.controller.fetch_ingredients()), 0)

    def test_b_add_user(self):
        returns = [self.controller.add_user(user.name, user.password) for user in self.users]

        for i, user in enumerate(self.users):
            self.assertEqual(returns[i], user.id)

        self.assertIsNone(self.controller.add_user(self.users[0].name, self.users[0].password))
        self.assertEqual(len(self.user_repository.find_all_users()), len(self.users))

    def test_c_login_user(self):
        user = self.users[0]

        self.assertEqual(self.controller.login_user(user.name, user.password), 0)
        self.assertIsNone(self.controller.login_user(user.name, "Surströmming<3"))
        self.assertIsNone(self.controller.login_user("Lordi", "Voldemort"))

    def test_d_add_meal(self):
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

    def test_e_add_ingredients(self):
        results = self.controller.fetch_ingredients()
        ingredients = self.ingredients

        self.assertEqual(len(results), len(ingredients))
        self.assertEqual(results[0].name, ingredients[0])
        self.assertIsInstance(self.controller.add_ingredients(ingredients), list)
        self.assertEqual(len(self.controller.add_ingredients(ingredients)), len(ingredients))

    def test_f_fetch_meals(self):
        results = self.controller.fetch_meals()
        (meal, ingredients) = self.mealset[0]

        self.assertIsInstance(results[0], Meal)
        self.assertEqual(results[0].name, meal)
        self.assertIsInstance(results[0].ingredients[0], Ingredient)
        self.assertEqual(len(results[0].ingredients), len(ingredients))
        self.assertEqual(results[0].ingredients[0].name, ingredients[0])

    def test_g_fetch_ingredients(self):
        results = self.controller.fetch_ingredients()

        self.assertIsInstance(results[0], Ingredient)
        self.assertEqual(results[-1].name, self.ingredients[-1])

    def test_h_generate_and_fetch_menu(self):
        self.controller.generate_menu()

        result = self.controller.fetch_menu()

        self.assertEqual(len(result.meals), 7)
        self.assertIsInstance(result, Menu)
        self.assertIsInstance(result.meals[0], Meal)
        self.assertIsInstance(result.meals[0].ingredients[0], Ingredient)
