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

        #self.meal_1 = Meal('Makaronilaatikko', [1,2,3,4], 1)
        #self.meal_2 = Meal('Uunimakkara', [4,5,6], 2)

        #self.insert_meal_1 = self.repository.insert_meal(self.meal_1.name)
        #self.insert_meal_2 = self.repository.insert_meal(self.meal_2.name)

        self.inserted_meals = [
            self.repository.insert_meal(meal.name) for meal in self.meals
        ]

        self.inserted_ingredients = [
            self.repository.insert_ingredient(ingredient.name)
            for ingredient in self.ingredients
        ]

        #self.meals = [self.meal_1, self.meal_2]

        self.relations = [
            (meal.db_id, ingredient)
            for meal in self.meals for ingredient in meal.ingredients
        ]

        self.repository.update_relations(self.relations)

    """def test_insert_meal(self):
        self.assertEqual(self.insert_meal_1, 1)
        self.assertEqual(self.insert_meal_2, 2)"""

    def test_insert_meal(self):
        for i in range(len(self.inserted_meals)):
            self.assertEqual(self.inserted_meals[i], i+1)

    def test_insert_ingredient(self):
        for i in range(len(self.inserted_ingredients)):
            self.assertEqual(self.inserted_ingredients[i], i+1)

    """def test_find_all_meals(self):
        meals = self.repository.find_all_meals()

        self.assertEqual(len(meals), 2)
        self.assertIsInstance(meals[0], Meal)
        self.assertEqual(meals[0].name, self.meal_1.name)"""

    def test_find_all_meals(self):
        meals = self.repository.find_all_meals()

        self.assertEqual(len(meals), 2)
        self.assertIsInstance(meals[0], Meal)
        self.assertEqual(meals[0].name, self.meals[0].name)

    """def test_find_single_meal(self):
        name = self.meal_1.name
        result = self.repository.find_single_meal(str(name))

        self.assertEqual(result.name, name)
        self.assertIsInstance(result, Meal)"""

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
        self.assertEqual(len(self.repository.find_meal_ingredients(self.meals[0].name)), len(self.meals[0].ingredients))



    """def test_find_meal_by_name(self):
        name = self.meal_1.name
        result = self.repository.find_meal_by_name(name)

        self.assertEqual(result[0]['name'], name)
        self.assertEqual(len(result), 1)
        self.assertIsInstance(result, list)

    def test_find_meal_by_id(self):
        result = self.repository.find_meal_by_id(1)

        self.assertIsInstance(result, Meal)
        self.assertEqual(result.name, self.insert_meal_1.name)"""



    #def empty_results(self):
    #    """Testataan jos kanta tyhjä, tähän
    #    """
