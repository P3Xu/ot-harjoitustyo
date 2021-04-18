import unittest
from entities.meal import Meal
from entities.menu import Menu
from entities.ingredient import Ingredient
from repositories.meal_repository import MealRepository
from repositories.menu_repository import MenuRepository

class TestMenuRepository(unittest.TestCase):
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

        self.relations = []

        for meal in self.meals:
            self.repository.insert_meal(meal.name)

            for ingredient in meal.ingredients:
                self.relations.append((meal.db_id, ingredient))

        for ingredient in self.ingredients:
            self.repository.insert_ingredient(ingredient.name)

        self.repository.update_relations(self.relations)

    def test_insert_meal(self):
        self.repository.empty_tables()

        insert = self.repository.insert_meal(self.meals[0].name)

        self.assertEqual(insert, 1)
        self.assertEqual(len(self.repository.find_all_meals()), 1)

    def test_insert_ingredient(self):
        self.repository.empty_tables()

        insert = self.repository.insert_ingredient(self.ingredients[0].name)

        self.assertEqual(insert, 1)
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

    def test_check_latest_id(self):
        id_ingredient = self.ingredients[-1].db_id
        id_meal = self.meals[-1].db_id
        check = self.repository.check_latest_id()[0]['id']

        self.assertEqual(self.repository.check_latest_id()[0]['id'], id_ingredient)
        self.assertEqual(self.repository.check_latest_id(True)[0]['id'], id_meal)

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
