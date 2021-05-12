class User:
    """Luokka käyttäjälle.

    Attributes:
        name: käyttäjänimi.
        password: salasana.
    """

    def __init__(self, name, password, db_id):
        """Konstruktori, luo uuden käyttäjän

        Args:
            name: käyttäjänimi.
            password: salasana.
        """

        self.name = name
        self.password = password
        self.id = db_id
