import unittest
import sqlite3
from repositories.io import InputOutput
from entities.default_set import DefaultSet
from init_database import initialize_database as init

class TestInputOutput(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init()

        cls.io = InputOutput()
        cls.meals = DefaultSet().meals
        cls.ingredients = DefaultSet().ingredients

    def test_a_write(self):
        pop_meal = self.meals.pop()
        meals = [(meal,) for meal in self.meals]
        query = "INSERT INTO meals (name) VALUES (?)"

        self.assertIsNone(self.io.write(query, meals, False))
        self.assertEqual(self.io.write(query, [pop_meal]), len(self.meals)+1)

        pop_ingredient = self.ingredients.pop()
        ingredients = [(ingredient,) for ingredient in self.ingredients]
        query = "INSERT INTO ingredients (name) VALUES (?)"

        self.assertIsNone(self.io.write(query, ingredients, False))
        self.assertEqual(self.io.write(query, [pop_ingredient]), len(self.ingredients)+1)

        query = "INSERT INTO macgyver (cones) VALUES (?)"
        self.assertIsInstance(self.io.write(query, meals, False), sqlite3.OperationalError)

    def test_b_read(self):
        meal_query = "SELECT * FROM meals WHERE id = ?"
        meals_query = "SELECT * FROM meals"
        ingredient_query = "SELECT * FROM ingredients WHERE id = ?"
        ingredients_query = "SELECT * FROM ingredients"

        meal_result = self.io.read(meal_query, [1])
        meals_result = self.io.read(meals_query)
        ingredient_result = self.io.read(ingredient_query, [1])
        ingredients_result = self.io.read(ingredients_query)

        self.assertEqual(meal_result[0]['name'], self.meals[0])
        self.assertEqual(meals_result[0]['name'], self.meals[0])
        self.assertEqual(ingredient_result[0]['name'], self.ingredients[0])
        self.assertEqual(ingredients_result[0]['name'], self.ingredients[0])

    def test_c_run_command(self):
        self.assertIsNone(self.io.run_command("DELETE FROM meals"))
        self.assertIsInstance(self.io.run_command("DELETE FROM macgyver"), sqlite3.OperationalError)

        self.io.run_command("CREATE TABLE kurkkumopo (id INTEGER, name TEXT)")
        self.assertEqual(len(self.io.read("SELECT * FROM kurkkumopo")), 0)

    def test_d_empty(self):
        self.assertEqual(len(self.io.read("SELECT * FROM meals")), 0)
        self.assertEqual(len(self.io.read("SELECT * FROM meals WHERE id = ?", [666])), 0)

        query = "SELECT * FROM macgyver"
        self.assertIsInstance(self.io.read(query), sqlite3.OperationalError)
