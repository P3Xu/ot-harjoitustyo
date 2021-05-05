from entities.user import User
from repositories.io import InputOutput

class UserRepository:


    def __init__(self):
        self.i_o = InputOutput()

    def add_user(self, username, password):
        query = "INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)"

        return self.i_o.write(query, [username, password])

    def empty_table(self):
        self.i_o.run_command("DELETE FROM users")

    def find_all_users(self):
        results = self.i_o.read("SELECT * FROM users")

        users = [User(user['username'], user['password']) for user in results]

        return users
