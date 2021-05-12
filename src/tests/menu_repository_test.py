import unittest
from datetime import date
from entities.meal import Meal
from entities.menu import Menu
from entities.user import User
from entities.ingredient import Ingredient
from repositories.io import InputOutput as test_io
from repositories.meal_repository import MealRepository
from repositories.menu_repository import MenuRepository
from tests.assets.meal_set import MealSet as test_set

class TestMenuRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.i_o = test_io()
        cls.meal_repository = MealRepository()
        cls.menu_repository = MenuRepository(cls.meal_repository, cls.i_o)
        cls.meal_set = test_set(cls.meal_repository)

        cls.meal_repository.empty_tables()

        cls.test_user1 = User("Paavo", "Pesusieni", 1)
        cls.test_user2 = User("Matti", "Meikäläinen", 2)

        cls.meals = cls.meal_set.create_meals(cls.test_user1)

    def setUp(self):
        self.menu_repository.empty_menu_table()

    def test_insert_menu(self):
        self.menu_repository.insert_menu(Menu(self.meals, date.today(), self.test_user1))
        self.menu_repository.insert_menu(Menu(self.meals, date.today(), self.test_user2))

        menu_1 = self.menu_repository.find_menu(self.test_user1)
        menu_2 = self.menu_repository.find_menu(self.test_user2)

        self.assertEqual(len(menu_1.meals), 7)
        self.assertEqual(len(menu_2.meals), 7)
        self.assertEqual(menu_1.user.id, self.test_user1.id)
        self.assertEqual(menu_2.user.id, self.test_user2.id)

    def test_find_menu(self):
        self.menu_repository.insert_menu(Menu(self.meals, date.today(), self.test_user1))

        menu = self.menu_repository.find_menu(self.test_user1)

        self.assertIsInstance(menu, Menu)
        self.assertIsInstance(menu.user, User)
        self.assertIsInstance(menu.meals, list)
        self.assertIsInstance(menu.meals[0], Meal)
        self.assertIsInstance(menu.meals[0].ingredients[0], Ingredient)
        self.assertEqual(len(menu.meals[0].ingredients), len(self.meals[0].ingredients))

    def test_empty_and_init(self):
        self.assertEqual(self.menu_repository.find_menu(self.test_user1), -1)

        self.menu_repository.insert_menu(Menu(self.meals, date.today(), self.test_user1))
        self.menu_repository.insert_menu(Menu(self.meals, date.today(), self.test_user2))

        self.assertEqual(len(self.menu_repository.i_o.read("SELECT * FROM menus")), 14)

        self.menu_repository._initialize_menus(self.test_user2)
        self.assertEqual(len(self.menu_repository.i_o.read("SELECT * FROM menus")), 7)
