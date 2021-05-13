import unittest
from entities.meal import Meal
from entities.user import User
from entities.ingredient import Ingredient
from entities.meal_set import MealSet as test_set
from repositories.io import InputOutput as test_io
from repositories.meal_repository import MealRepository

class TestMealRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.i_o = test_io()
        cls.repository = MealRepository(cls.i_o)
        cls.meal_set = test_set(cls.repository)

        cls.repository.empty_tables()

        cls.test_user = User("Paavo", "Pesusieni", 1)
        cls.false_user = User("Darth", "Vader", 666)

        cls.meals = cls.meal_set.create_meals(cls.test_user)
        cls.ingredients = cls.meal_set.create_ingredients()

    def test_a_find_all_meals(self):
        meals = self.repository.find_all_meals(self.test_user)
        meal = meals[0]

        self.assertEqual(len(meals), len(self.meals))
        self.assertIsInstance(meal, Meal)
        self.assertEqual(meal.name, self.meals[0].name)
        self.assertIsInstance(meal.ingredients[0], Ingredient)
        self.assertEqual(meal.ingredients[0].name, self.ingredients[0].name)
        self.assertEqual(len(meal.ingredients), len(self.meals[0].ingredients))
        self.assertEqual(len(self.repository.find_all_meals(self.false_user)), 0)

    def test_b_find_single_meal_by_name(self):
        name = self.meals[0].name
        result = self.repository.find_single_meal(name, self.test_user)

        self.assertEqual(result.name, name)
        self.assertIsInstance(result, Meal)
        self.assertIsInstance(result.ingredients[0], Ingredient)
        self.assertEqual(len(result.ingredients), len(self.meals[0].ingredients))
        self.assertEqual(len(self.repository.find_single_meal('Surströmming', self.test_user)), 0)

    def test_c_find_single_meal_by_id(self):
        user = self.test_user
        result = self.repository.find_single_meal(1, user)

        self.assertEqual(result.db_id, 1)
        self.assertIsInstance(result, Meal)
        self.assertIsInstance(result.ingredients[0], Ingredient)
        self.assertIsNone(self.repository.find_single_meal(self.meals[0], user))
        self.assertEqual(len(self.repository.find_single_meal(666, user)), 0)

    def test_d_find_all_ingredients(self):
        ingredients = self.repository.find_all_ingredients(self.test_user)

        self.assertIsInstance(ingredients[0], Ingredient)
        self.assertEqual(len(ingredients), len(self.ingredients))
        self.assertEqual(ingredients[0].name, self.ingredients[0].name)
        self.assertEqual(len(self.repository.find_all_ingredients(self.false_user)), 0)

    def test_e_find_single_ingredient(self):
        user = self.test_user
        name = self.ingredients[0].name
        result = self.repository.find_single_ingredient(name, user)

        self.assertEqual(result.name, name)
        self.assertIsInstance(result, Ingredient)
        self.assertIsNone(self.repository.find_single_ingredient(self.meals[0], user))
        self.assertEqual(len(self.repository.find_single_ingredient('Mämmi', user)), 0)

    def test_f_insert_ingredient(self):
        self.repository.empty_tables()

        ingredient = self.ingredients[0]
        insert = self.repository.insert_ingredient(ingredient)

        self.assertEqual(insert.db_id, 1)
        self.assertIsInstance(insert, Ingredient)
        self.assertEqual(insert.name, ingredient.name)
        self.assertEqual(self.repository.fetch_item_id(ingredient.name, False), insert.db_id)

    def test_g_insert_meal(self):
        self.repository.empty_tables()

        meal = self.meals[0]
        ingredients = [self.repository.insert_ingredient(Ingredient(ingredient.name))
            for ingredient in meal.ingredients]

        db_id = self.repository.insert_meal(Meal(meal.name, ingredients), self.test_user)

        meals = self.repository.find_all_meals(self.test_user)

        self.assertEqual(len(meals), 1)
        self.assertEqual(meals[0].db_id, db_id)
        self.assertIsInstance(meals[0], Meal)
        self.assertEqual(meals[0].name, meal.name)
        self.assertIsInstance(meals[0].ingredients[0], Ingredient)

    def test_h_empty_tables_and_results(self):
        repo = self.repository
        user = self.test_user
        meals = repo.find_all_meals(user)
        ingredients = repo.find_all_ingredients(user)

        self.assertEqual(len(meals), 1)
        self.assertEqual(len(ingredients), 3)

        repo.empty_tables()

        self.assertEqual(len(repo.find_all_meals(user)), 0)
        self.assertEqual(len(repo.find_all_ingredients(user)), 0)
        self.assertEqual(len(repo.find_single_meal(meals[0].db_id, user)), 0)
        self.assertEqual(len(repo.find_single_meal(meals[0].name, user)), 0)
        self.assertEqual(len(repo.find_single_ingredient(ingredients[0].name, user)), 0)

    def test_i_no_overflows(self):
        self.repository.empty_tables()

        test_user1 = self.test_user
        test_user2 = self.false_user
        test_user3 = User("Paavo", "Väyrynen", 13)
        test_user4 = User("Hilarius", "Hiiri", 64)

        test_user_meals1 = self.meal_set.create_meals(test_user1)
        test_user_meals2 = self.meal_set.create_meals(test_user2)
        test_user_meals3 = self.meal_set.create_meals(test_user3)
        test_user_meals4 = self.meal_set.create_meals(test_user4)

        self.assertEqual(len(self.repository.find_all_meals(test_user1)), len(test_user_meals1))
        self.assertEqual(len(self.repository.find_all_meals(test_user2)), len(test_user_meals2))
        self.assertEqual(len(self.repository.find_all_meals(test_user3)), len(test_user_meals3))
        self.assertEqual(len(self.repository.find_all_meals(test_user4)), len(test_user_meals4))
        self.assertEqual(len(self.i_o.read("SELECT * FROM meal_relations")), 76)
