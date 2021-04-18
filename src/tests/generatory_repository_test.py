"""import unittest
from repositories import generator_repository

class TestGeneratorRepository(unittest.TestCase):
    def setUp(self):
        self.generator_repository = generator_repository.GeneratorRepository()

    def test_find_all_meals(self):
        meals = self.generator_repository.find_all_meals()
        
        self.assertEqual(len(meals), 8)
        self.assertEqual(meals[0]['name'], "Makaronilaatikko")
        self.assertEqual(meals[-1]['name'], "Kalapuikot")

    # REFAKTOROINNIN PAIKKA, VOISI OLLA VAIKKA MEAL_ID
    def test_find_meal(self):
        meal = self.generator_repository.find_meal("Makaronilaatikko")

        self.assertEqual(len(meal), 1)
        self.assertEqual(meal[0]['id'], 1)

    def test_find_all_ingredients(self):
        ingredients = self.generator_repository.find_all_ingredients()

        self.assertEqual"""