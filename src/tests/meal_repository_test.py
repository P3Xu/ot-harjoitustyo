import unittest
from entities.meal import Meal
from entities.ingredient import Ingredient
from entities.default_set import DefaultSet
from repositories.meal_repository import MealRepository

class TestMealRepository(unittest.TestCase):
    def setUp(self):
        self.repository = MealRepository()
        self.ingredients = DefaultSet().create_ingredients()
        self.meals = DefaultSet().create_meals()

        self.repository.empty_tables()

        for meal in self.meals:
            for i in range(len(meal.ingredients)):
                ingredient = self.ingredients[meal.ingredients[i]]
                meal.ingredients[i] = self.repository.insert_ingredient(ingredient)

            self.repository.insert_meal(meal)

    def test_insert_meal(self):
        self.repository.empty_tables()

        meal = self.meals[0]
        ingredients = [
            self.repository.insert_ingredient(Ingredient(ingredient.name))
            for ingredient in meal.ingredients
        ]

        db_id = self.repository.insert_meal(Meal(meal.name, ingredients))

        meals = self.repository.find_all_meals()

        self.assertEqual(len(meals), 1)
        self.assertEqual(meals[0].db_id, db_id)
        self.assertIsInstance(meals[0], Meal)
        self.assertEqual(meals[0].name, meal.name)

    def test_insert_ingredient(self):
        self.repository.empty_tables()

        insert = self.repository.insert_ingredient(self.ingredients[0])

        self.assertEqual(insert.db_id, 1)
        self.assertIsInstance(insert, Ingredient)
        self.assertEqual(insert.name, self.ingredients[0].name)
        self.assertEqual(len(self.repository.find_all_ingredients()), 1)

    def test_find_all_meals(self):
        meals = self.repository.find_all_meals()
        meal = meals[0]

        self.assertEqual(len(meals), len(self.meals))
        self.assertIsInstance(meal, Meal)
        self.assertEqual(meal.name, self.meals[0].name)
        self.assertIsInstance(meal.ingredients[0], Ingredient)
        self.assertEqual(meal.ingredients[0].name, self.ingredients[0].name)
        self.assertEqual(len(meal.ingredients), len(self.meals[0].ingredients))

    def test_find_single_meal_by_name(self):
        name = self.meals[0].name
        result = self.repository.find_single_meal(str(name))

        self.assertEqual(result.name, name)
        self.assertIsInstance(result, Meal)
        self.assertIsInstance(result.ingredients[0], Ingredient)
        self.assertEqual(len(result.ingredients), len(self.meals[0].ingredients))
        self.assertEqual(len(self.repository.find_single_meal(str('Surströmming'))), 0)

    def test_find_single_meal_by_id(self):
        result = self.repository.find_single_meal(int(1))

        self.assertEqual(result.db_id, 1)
        self.assertIsInstance(result, Meal)
        self.assertIsInstance(result.ingredients[0], Ingredient)
        self.assertIsNone(self.repository.find_single_meal(self.meals[0]))
        self.assertEqual(len(self.repository.find_single_meal(int(666))), 0)

    def test_find_all_ingredients(self):
        ingredients = self.repository.find_all_ingredients()

        self.assertIsInstance(ingredients[0], Ingredient)
        self.assertEqual(len(ingredients), len(self.ingredients))
        self.assertEqual(ingredients[0].name, self.ingredients[0].name)

    def test_find_single_ingredient(self):
        name = self.ingredients[0].name
        result = self.repository.find_single_ingredient(str(name))

        self.assertEqual(result.name, name)
        self.assertIsInstance(result, Ingredient)
        self.assertIsNone(self.repository.find_single_ingredient(self.meals[0]))
        self.assertEqual(len(self.repository.find_single_ingredient(str('Mämmi'))), 0)

    def test_empty_tables_and_results(self):
        repo = self.repository
        meals = repo.find_all_meals()
        ingredients = repo.find_all_ingredients()

        self.assertEqual(len(meals), len(self.meals))
        self.assertEqual(len(ingredients), len(self.ingredients))

        repo.empty_tables()

        self.assertEqual(len(repo.find_all_meals()), 0)
        self.assertEqual(len(repo.find_all_ingredients()), 0)
        self.assertEqual(len(repo.find_single_meal(int(meals[0].db_id))), 0)
        self.assertEqual(len(repo.find_single_meal(str(meals[0].name))), 0)
        self.assertEqual(len(repo.find_single_ingredient(str(ingredients[0].name))), 0)
