import unittest
from entities.meal import Meal
from entities.ingredient import Ingredient
from repositories.meal_repository import MealRepository

class TestMealRepository(unittest.TestCase):
    def setUp(self):
        self.repository = MealRepository()
        self.repository.empty_tables()

        self.ingredients = [
            Ingredient('Jauheliha'),
            Ingredient('Sipuli'),
            Ingredient('Makaroni'),
            Ingredient('Juusto'),
            Ingredient('Lenkkimakkara'),
            Ingredient('Ketsuppi')
        ]

        self.meals = [
            Meal('Makaronilaatikko', [0,1,2]),
            Meal('Uunimakkara', [3,4,5])
        ]

        for meal in self.meals:
            for i in range(len(meal.ingredients)):
                meal.ingredients[i] = self.repository.insert_ingredient(self.ingredients[i])

            self.repository.insert_meal(meal)

    def test_insert_meal(self):
        self.repository.empty_tables()

        meal = self.meals[0]
        ingredients = [
            self.repository.insert_ingredient(Ingredient(ingredient.name))
            for ingredient in meal.ingredients
        ]

        self.repository.insert_meal(Meal(meal.name, ingredients))

        meals = self.repository.find_all_meals()

        self.assertEqual(len(meals), 1)
        self.assertEqual(meals[0].db_id, 1)
        self.assertIsInstance(meals[0], Meal)
        self.assertEqual(meals[0].name, meal.name)
        self.assertEqual(len(meals[0].ingredients), len(meal.ingredients))
        self.assertEqual(meals[0].ingredients[0].name, meal.ingredients[0].name)

    def test_insert_ingredient(self):
        self.repository.empty_tables()

        insert = self.repository.insert_ingredient(self.ingredients[0])

        self.assertEqual(insert.db_id, 1)
        self.assertIsInstance(insert, Ingredient)
        self.assertEqual(insert.name, self.ingredients[0].name)
        self.assertEqual(len(self.repository.find_all_ingredients()), 1)

    def test_find_all_meals(self):
        meals = self.repository.find_all_meals()

        self.assertEqual(len(meals), 2)
        self.assertIsInstance(meals[0], Meal)
        self.assertEqual(meals[0].name, self.meals[0].name)

    def test_find_single_meal_by_name(self):
        name = self.meals[0].name
        result = self.repository.find_single_meal(str(name))

        self.assertEqual(result.name, name)
        self.assertIsInstance(result, Meal)
        self.assertEqual(len(self.repository.find_single_meal(str('Surströmming'))), 0)

    def test_find_single_meal_by_id(self):
        result = self.repository.find_single_meal(int(1))

        self.assertEqual(result.db_id, 1)
        self.assertIsInstance(result, Meal)
        self.assertIsNone(self.repository.find_single_meal(float(666)))

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
        self.assertEqual(len(self.repository.find_single_ingredient(str('Mämmi'))), 0)
        self.assertIsNone(self.repository.find_single_ingredient(self.meals[0]))

    def test_find_meal_ingredients(self):
        ingredients = self.repository.find_meal_ingredients(self.meals[0].name)

        self.assertIsInstance(ingredients[0], Ingredient)
        self.assertEqual(len(ingredients), len(self.meals[0].ingredients))

    def test_empty_tables(self):
        meals = self.repository.find_all_meals()
        ingredients = self.repository.find_all_ingredients()

        self.assertEqual(len(meals), len(self.meals))
        self.assertEqual(len(ingredients), len(self.ingredients))

        self.repository.empty_tables()

        self.assertEqual(len(self.repository.find_all_meals()), 0)
        self.assertEqual(len(self.repository.find_all_ingredients()), 0)

    #def empty_results(self):
    # Entäs jos kanta onkin tyhjä?
