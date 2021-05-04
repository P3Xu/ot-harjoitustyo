class User:
    """Luokka käyttäjälle.

    Attributes:
        name: käyttäjänimi.
        password: salasana.
    """

    def __init__(self, name, password):
        """Konstruktori, luo uuden käyttäjän

        Args:
            name: käyttäjänimi.
            password: salasana.
        """

        self.name = name
        self.password = password
