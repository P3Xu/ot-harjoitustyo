import unittest
from datetime import date
from repositories.io import InputOutput as test_io
from repositories.meal_repository import MealRepository
from services.generator import GeneratorService
from entities.menu import Menu
from entities.user import User
from entities.meal import Meal
from entities.ingredient import Ingredient
from entities.meal_set import MealSet as test_set

class TestGeneratorService(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.i_o = test_io()
        cls.meal_repository = MealRepository(cls.i_o)
        cls.meal_set = test_set(cls.meal_repository)

        cls.meal_repository.empty_tables()

        cls.test_user = User("Paavo", "Pesusieni", 1)
        cls.generator = GeneratorService(cls.meal_repository, cls.test_user)

        cls.meals = cls.meal_set.create_meals(cls.test_user)
        cls.ingredients = cls.meal_set.create_ingredients()
        
        cls.test_menu = cls.generator.generate()

    def test_generate_returns_correct_object(self):
        menu = self.test_menu

        self.assertIsInstance(menu, Menu)
        self.assertIsInstance(menu.user, User)
        self.assertIsInstance(menu.meals, list)
        self.assertIsInstance(menu.meals[0], Meal)
        self.assertIsInstance(menu.meals[0].ingredients[0], Ingredient)

        self.assertEqual(len(menu.meals), 7)
        self.assertEqual(menu.user.id, self.test_user.id)

    def test_generate_no_duplicate_meals(self):
        meals = set(self.test_menu.get_meals())

        self.assertEqual(len(meals), 7)

    def test_generate_correct_timestamp(self):
        self.assertEqual(self.test_menu.get_date(), date.today())

    def test_when_not_enough_meals(self):
        self.meal_repository.empty_tables()

        self.assertEqual(self.generator.generate(), -1)
