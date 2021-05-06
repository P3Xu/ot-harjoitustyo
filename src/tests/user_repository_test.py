"""import unittest
from entities.user import User
from repositories.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.repository = UserRepository()
        self.user_1 = User("Paavo", "Pesusieni666_")
        self.user_2 = User("MacGyver", "_käpyKranaatti13")

        self.repository.empty_users_table()

    def test_add_user(self):
        self.repository.add_user(self.user_1.name, self.user_1.password)

        user = self.repository.find_all_users()[0]

        self.assertEqual(user.name, self.user_1.name)

    def test_find_all_users(self):
        self.repository.add_user(self.user_1.name, self.user_1.password)
        self.repository.add_user(self.user_2.name, self.user_2.password)

        users = self.repository.find_all_users()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].name, self.user_1.name)
        self.assertIsInstance(users[0], User)
        self.assertEqual(users[1].password, self.user_2.password)

    def test_find_by_username(self):
        self.repository.add_user(self.user_1.name, self.user_1.password)

        user = self.repository.find_by_username(self.user_1.name)

        self.assertEqual(user.name, self.user_1.name)
        self.assertEqual(user.password, self.user_1.password)
        self.assertIsNone(self.repository.find_by_username('Voldemort'))

    def test_empty_users_table(self):
        self.repository.add_user(self.user_1.name, self.user_1.password)
        self.assertEqual(len(self.repository.find_all_users()), 1)

        self.repository.empty_users_table()

        self.assertEqual(len(self.repository.find_all_users()), 0)
"""