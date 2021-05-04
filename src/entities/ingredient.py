class Ingredient:
    """
    Luokka yksittäiselle raaka-aineelle.

    Attributes:
        name: raaka-aineen nimi.
        db_id: tietokannan id, mikäli olemassa. Vapaaehtoinen.
    """

    def __init__(self, name, db_id=None):
        """
        Konstruktori, luo uuden raaka-aineen.

        Args:
            name: raaka-aineen nimi.
            db_id: tietokannan id, mikäli sellainen on olemassa. Ei pakollinen.
        """

        self.name = name
        self.db_id = db_id

    def __str__(self):
        """Metodi, joka palauttaa olion nimen merkkijonona.

        Returns:
            Olion nimi merkkijonona.
        """

        return self.name
