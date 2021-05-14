import unittest
from pathlib import Path
from datetime import datetime
from entities.meal import Meal
from entities.menu import Menu
from entities.user import User
from entities.ingredient import Ingredient
from entities.meal_set import MealSet as test_set
from services.controller import Controller
from config import DEFAULT_SET_FILE_PATH, WISHLIST_DIR_PATH

class TestControllerRepositoryAsIntegration(unittest.TestCase):
    """
    Tämä on lähes sama setti kuin kyseisen luokan yksikkötestitkin, mutta testattuna
    luokan omilla riippuvuuksilla ja joissain testimetodeissa on jonkin verran eroja.
    """

    @classmethod
    def setUpClass(cls):
        cls.controller = Controller()

        cls.meals = test_set().meals
        cls.ingredients = test_set().ingredients
        cls.meal_relations = test_set().relations

        cls.users = cls._prepare_users()
        cls.mealset = cls._prepare_meals()

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
        self.controller.meal_repository.empty_tables()
        self.controller.menu_repository.empty_menu_table()
        self.controller.user_repository.empty_users_table()

        self.controller.user = self.users[0]

        self.assertIsNone(self.controller.fetch_menu())
        self.assertEqual(len(self.controller.fetch_meals()), 0)
        self.assertEqual(len(self.controller.fetch_ingredients()), 0)

    def test_b_add_user(self):
        returns = [self.controller.add_user(user.name, user.password) for user in self.users]

        for i, user in enumerate(self.users):
            self.assertEqual(returns[i], user.id)

        self.assertIsNone(self.controller.add_user(self.users[0].name, self.users[0].password))
        self.assertEqual(len(self.controller.user_repository.find_all_users()), len(self.users))

        user = User("Matti", "Näsä", 4)
        add_user = self.controller.add_user(user.name, user.password, open(DEFAULT_SET_FILE_PATH))

        self.assertEqual(add_user, 4)

    def test_c_login_user(self):
        user = self.users[0]

        self.assertEqual(self.controller.login_user(user.name, user.password), 0)
        self.assertIsNone(self.controller.login_user(user.name, "Surströmming<3"))
        self.assertIsNone(self.controller.login_user("Lordi", "Voldemort"))

    def test_d_add_meal(self):
        self.controller.meal_repository.empty_tables()

        for pieces in self.mealset:
            (meal, ingredients) = pieces

            self.controller.add_meal(meal, ingredients)

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

        self.assertIsNotNone(results[0].db_id)
        self.assertIsInstance(results[0], Ingredient)
        self.assertEqual(results[-1].name, self.ingredients[-1])

    def test_h_generate_and_fetch_menu(self):
        self.controller.generate_menu()

        result = self.controller.fetch_menu()

        self.assertEqual(len(result.meals), 7)
        self.assertIsInstance(result, Menu)
        self.assertIsInstance(result.meals[0], Meal)
        self.assertIsInstance(result.meals[0].ingredients[0], Ingredient)

        self.controller.menu_repository.empty_menu_table()

        self.assertIsNone(self.controller.fetch_menu())

    def test_i_remove_meal(self):
        self.controller.generate_menu()

        self.assertIsInstance(self.controller.add_meal("Lihakeitto", ["Liha"]), int)

        test_meal1 = self.meals[0]
        get_meals = self.controller.fetch_meals()
        test_meal2 = get_meals[-1].name

        self.assertEqual(len(get_meals), len(self.meals)+1)

        self.controller.remove_meal(test_meal2)
        self.controller.remove_meal(test_meal1)

        results = self.controller.fetch_meals()
        meals = [meal.name for meal in results]

        self.assertNotIn(test_meal1, meals)
        self.assertNotIn(test_meal2, meals)
        self.assertEqual(len(results), len(self.meals)-1)
        self.assertIsNone(self.controller.remove_meal("Avaruusmössö"))

    def test_j_export_wishlist(self):
        timestamp = datetime.now().strftime("%d_%m_%H%M%S")
        file_name = "/kauppalista"+timestamp+".txt"
        wishlist = ["Makaroni", "Jauheliha", "Sipuli"]

        path = Path(WISHLIST_DIR_PATH+file_name)

        self.assertAlmostEqual(self.controller.export_wishlist(wishlist), file_name)
        self.assertTrue(path.is_file())

        path.unlink()
