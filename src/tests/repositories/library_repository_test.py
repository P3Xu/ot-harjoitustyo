import unittest
from pathlib import Path
from config import WISHLIST_DIR_PATH
from repositories.library_repository import LibraryRepository
from entities.user import User
from entities.meal import Meal
from entities.meal_set import MealSet as test_set
from init_default_set import initialize_default_set
from tests.init_wishlist_dir import initialize_wishlist_dir

class TestLibraryRepository(unittest.TestCase):
    def setUp(self):
        self.user = User("Paavo", "Pesusieni", 1)
        self.repository = LibraryRepository()
        self.meals = test_set().create_meals(self.user)

        initialize_default_set()

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

    def test_write_wishlist(self):
        meal = self.meals[0]
        file_path = self.repository.write_wishlist(meal.ingredients, WISHLIST_DIR_PATH)
        path = Path(file_path)
        items = []

        with open(file_path) as file:
            for row in file:
                row = row.replace("\n", "")

                items.append(row)

        for i, ingredient in enumerate(meal.ingredients):
            self.assertEqual(items[i], ingredient.name)

        path.unlink()

        path = Path(WISHLIST_DIR_PATH)
        path.chmod(444)
        result = self.repository.write_wishlist(meal.ingredients, WISHLIST_DIR_PATH)

        self.assertIsInstance(result, IOError)

        path.chmod(755)

class TestInitDir(unittest.TestCase):
    def setUp(self):
        Path(WISHLIST_DIR_PATH).rmdir()

    def test_initialize_wishlist_dir(self):
        initialize_wishlist_dir()

        self.assertTrue(Path(WISHLIST_DIR_PATH).is_dir())
