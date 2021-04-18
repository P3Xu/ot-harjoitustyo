import unittest
from entities.meal import Meal
from entities.ingredient import Ingredient
from repositories.meal_repository import MealRepository

class TestMealRepository(unittest.TestCase):
    def setUp(self):
        self.repository = MealRepository()
        self.repository.empty_tables()

        self.ingredients = [
            Ingredient('Jauheliha', 1),
            Ingredient('Sipuli', 2),
            Ingredient('Makaroni', 3),
            Ingredient('Juusto', 4),
            Ingredient('Lenkkimakkara', 5),
            Ingredient('Ketsuppi', 6)
        ]

        self.meals = [
            Meal('Makaronilaatikko', [1,2,3,4], 1),
            Meal('Uunimakkara', [4,5,6], 2)
        ]

        self.inserted_meals = [
            self.repository.insert_meal(meal.name) for meal in self.meals
        ]

        self.inserted_ingredients = [
            self.repository.insert_ingredient(ingredient.name)
            for ingredient in self.ingredients
        ]

        self.relations = [
            (meal.db_id, ingredient)
            for meal in self.meals for ingredient in meal.ingredients
        ]

        self.repository.update_relations(self.relations)

    def test_insert_meal(self):
        for i in range(len(self.inserted_meals)):
            self.assertEqual(self.inserted_meals[i], i+1)

    def test_insert_ingredient(self):
        for i in range(len(self.inserted_ingredients)):
            self.assertEqual(self.inserted_ingredients[i], i+1)

    def test_find_all_meals(self):
        meals = self.repository.find_all_meals()

        self.assertEqual(len(meals), 2)
        self.assertIsInstance(meals[0], Meal)
        self.assertEqual(meals[0].name, self.meals[0].name)

    def test_find_single_meal(self):
        name = self.meals[0].name
        result = self.repository.find_single_meal(str(name))

        self.assertEqual(result.name, name)
        self.assertIsInstance(result, Meal)

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

    def test_find_meal_ingredients(self):
        ingredients = self.repository.find_meal_ingredients(self.meals[0].name)

        self.assertIsInstance(ingredients[0], Ingredient)
        self.assertEqual(len(ingredients), len(self.meals[0].ingredients))

    def test_check_latest_id(self):
        id_ingredient = self.ingredients[-1].db_id
        self.assertEqual(self.repository.check_latest_id()[0]['id'], id_ingredient)

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
