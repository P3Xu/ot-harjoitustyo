'''import unittest
from datetime import date
from entities.meal import Meal
from entities.menu import Menu
from entities.user import User
from entities.ingredient import Ingredient
from entities.default_set import DefaultSet
from repositories.meal_repository import MealRepository
from repositories.menu_repository import MenuRepository

class TestMenuRepository(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.meal_repository = MealRepository()
        cls.menu_repository = MenuRepository(cls.meal_repository)
        cls.meal_repository.empty_tables()
        cls.mealset = DefaultSet().create_meals()
        cls.ingredients = DefaultSet().create_ingredients()
        cls.meals = cls._prepare_meal_repository()
        cls.test_user = User("Paavo", "Pesusieni", 1)

    @classmethod
    def _prepare_meal_repository(cls):
        meals = []

        for meal in cls.mealset:

            for i in range(len(meal.ingredients)):

                ingredient = cls.ingredients[meal.ingredients[i]]
                meal.ingredients[i] = cls.meal_repository.insert_ingredient(ingredient)

            meals.append(Meal(meal.name, meal.ingredients, cls.meal_repository.insert_meal(meal)))

        return meals

    def setUp(self):
        self.menu_repository.empty_menu_table()

    def test_insert_and_find_menu(self):
        """
            Toistaiseksi kaikki samassa, tämä on vielä niin pieni luokka että tuntui
            turhalta yrittää väkisin vääntää erillisiä testi-caseja tai pistää
            kumpaankin samanlaisia testejä.
        """
        meals = self.meals.copy()
        meals.pop()

        self.menu_repository.insert_menu(Menu(meals, date.today()), self.test_user)
        menu = self.menu_repository.find_menu(self.test_user)

        self.assertIsInstance(menu, Menu)
        self.assertIsInstance(menu.meals, list)
        self.assertIsInstance(menu.meals[0], Meal)
        self.assertIsInstance(menu.meals[0].ingredients[0], Ingredient)
        self.assertEqual(len(menu.meals), 7)
        self.assertEqual(len(menu.meals[0].ingredients), len(self.meals[0].ingredients))

    def test_empty_db(self):
        self.assertEqual(self.menu_repository.find_menu(self.test_user), -1)
'''