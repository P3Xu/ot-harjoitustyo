from entities.user import User
from repositories.io import InputOutput

class UserRepository:
    """Luokka, joka hoitaa sovelluksen käyttäjiin liittyvät tietokantatoiminnot.

    Attributes:
        i_o: I/O, jolla hoidetaan kannan luku- ja kirjoitustoiminnot.
    """

    def __init__(self):
        """
        Konstruktori, alustaa attribuutin I/O-olion. I/O hoitaa keskitetysti repository-luokkien
        luku- ja kirjoitustoiminnot tietokannassa.
        """

        self.i_o = InputOutput()

    def add_user(self, username, password):
        """Metodi, joka lisää uuden käyttäjän tietokantaan.

        Args:
            username: käyttäjän käyttäjätunnus.
            password: käyttäjän salasana. Tässä tapauksessa valitettavasti ihan vain plaintextina.

        Returns:
            Palauttaa tietokantaan lisätyn rivin id-numeron.
        """

        query = "INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)"

        return self.i_o.write(query, [username, password])

    def empty_users_table(self):
        """Metodi tyhjentää kokonaan kannan users-taulun, käytetään lähinnä testauksessa."""

        self.i_o.run_command("DELETE FROM users")

    def find_all_users(self):
        """Metodilla haetaan kaikki lisätyt käyttäjät tietokannasta.

        Returns:
            Palauttaa listallisen User-olioita.
        """

        results = self.i_o.read("SELECT * FROM users")

        users = [User(user['username'], user['password'], user['id']) for user in results]

        return users

    def find_by_username(self, username):
        """Metodilla haetaan yksittäinen käyttäjä tietokannasta.

        Args:
            username: käyttäjätunnus, jota kannasta etsitään.

        Returns:
            Palauttaa joko etsityn käyttäjän User-oliona jos sellainen löytyy, tai muussa
            tapauksessa Nonen, mikäli käyttäjää ei löydy tai sattuu jokin poikkeus.
        """

        result = self.i_o.read("SELECT * FROM users WHERE username = ?", username)

        if isinstance(result, list) and len(result) > 0:
            result = result[0]

            return User(result['username'], result['password'], result['id'])

        return None
