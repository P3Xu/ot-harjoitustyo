import unittest
from pathlib import Path
from config import DEFAULT_SET_FILE_PATH
from repositories.library_repository import LibraryRepository
from tests.assets.meal_set import MealSet as test_set
from entities.user import User
from entities.meal import Meal

class TestLibraryRepository(unittest.TestCase):

    def setUp(self):
        self.user = User("Paavo", "Pesusieni", 1)
        self.repository = LibraryRepository()
        self.meals = test_set().create_meals(self.user)

        Path(DEFAULT_SET_FILE_PATH).touch()

        with open(DEFAULT_SET_FILE_PATH, "w") as file:
            for meal in self.meals:
                for ingredient in meal.ingredients:
                    row = f"{meal};{ingredient}"

                    file.write(row + "\n")

    def test_read_meals(self):
        csv_meals = self.repository.read_meals()
        csv_meal = csv_meals[0]
        meal = self.meals[0]

        self.assertEqual(len(csv_meals), len(self.meals))
        self.assertEqual(len(csv_meal.ingredients), len(meal.ingredients))
        self.assertEqual(csv_meal.name, meal.name)
        self.assertEqual(csv_meal.ingredients[0], meal.ingredients[0].name)
        self.assertIsInstance(csv_meal, Meal)
        self.assertEqual(csv_meals[-1].name, self.meals[-1].name)
        self.assertEqual(csv_meals[-1].ingredients[-1], self.meals[-1].ingredients[-1].name)
