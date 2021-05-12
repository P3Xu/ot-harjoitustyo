import unittest
from entities.user import User
from repositories.user_repository import UserRepository
from repositories.io import InputOutput as test_io

class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.i_o = test_io()
        self.repository = UserRepository(self.i_o)

        self.test_user1 = User("Paavo", "Pesusieni666_", 1)
        self.test_user2 = User("MacGyver", "_käpyKranaatti13", 2)

        self.repository.empty_users_table()

    def test_add_user(self):
        self.repository.add_user(self.test_user1.name, self.test_user1.password)

        user = self.repository.find_all_users()[0]

        self.assertEqual(user.name, self.test_user1.name)
        self.assertEqual(user.id, self.test_user1.id)

    def test_find_all_users(self):
        self.repository.add_user(self.test_user1.name, self.test_user1.password)
        self.repository.add_user(self.test_user2.name, self.test_user2.password)

        users = self.repository.find_all_users()

        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].name, self.test_user1.name)
        self.assertIsInstance(users[0], User)
        self.assertEqual(users[1].password, self.test_user2.password)
        self.assertEqual(users[1].id, self.test_user2.id)

    def test_find_by_username(self):
        self.repository.add_user(self.test_user1.name, self.test_user1.password)

        user = self.repository.find_by_username(self.test_user1.name)

        self.assertEqual(user.name, self.test_user1.name)
        self.assertEqual(user.password, self.test_user1.password)
        self.assertEqual(user.id, self.test_user1.id)
        self.assertIsNone(self.repository.find_by_username('Voldemort'))

    def test_empty_users_table(self):
        self.repository.add_user(self.test_user1.name, self.test_user1.password)
        self.assertEqual(len(self.repository.find_all_users()), 1)

        self.repository.empty_users_table()

        self.assertEqual(len(self.repository.find_all_users()), 0)
