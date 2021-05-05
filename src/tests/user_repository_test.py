import unittest
import sqlite3
from repositories.io import InputOutput
from entities.user import User
from init_database import drop_tables, create_tables
from repositories.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.repository = UserRepository()
        self.user_1 = User("Paavo", "Pesusieni666_")
        self.user_2 = User("MacGyver", "_käpyKranaatti13")

        self.repository.empty_table()

    def test_add_user(self):
        self.repository.add_user(self.user_1.name, self.user_1.password)

        user = self.repository.find_all_users()[0]

        self.assertEqual(user.name, self.user_1.name)

    def test_find_all_users(self):
        self.repository.add_user(self.user_1.name, self.user_1.password)
        self.repository.add_user(self.user_2.name, self.user_2.password)

        users = self.repository.find_all_users()
        user = users[0]

        self.assertEqual(len(users), 2)
        self.assertEqual(user.name, self.user_1.name)
        self.assertIsInstance(user, User)
        self.assertEqual(users[1].password, self.user_2.password)
