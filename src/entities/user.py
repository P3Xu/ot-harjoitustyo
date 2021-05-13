class User:
    """Käyttäjän ilmentymä.

    Attributes:
        name: käyttäjänimi.
        password: salasana.
        db_id: käyttäjän id-numero tietokannassa.
    """

    def __init__(self, name, password, db_id):
        """Konstruktori, luo uuden käyttäjän

        Args:
            name: käyttäjänimi.
            password: salasana.
            db_id: tietokannan uniikki id-numero.
        """

        self.name = name
        self.password = password
        self.id = db_id
