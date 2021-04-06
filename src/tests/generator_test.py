import unittest
from datetime import date
from repositories.generator_repository import GeneratorRepository
from services.generator import GeneratorService
from entities.menu import Menu

class TestGeneratorService(unittest.TestCase):
    def setUp(self):
        self.repository = GeneratorRepository()
        self.generator = GeneratorService(self.repository)
        self.test_menu = self.generator.generate()

    def test_generate_returns_correct_object(self):
        self.assertIsInstance(self.test_menu, Menu)

    def test_generate_no_duplicate_meals(self):
        meals = set(self.test_menu.get_meals())

        self.assertEqual(len(meals), 7)

    def test_generate_correct_timestamp(self):
        self.assertEqual(self.test_menu.get_date(), date.today())
