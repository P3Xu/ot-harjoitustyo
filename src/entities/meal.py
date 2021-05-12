class Meal:
    """Luokka yksittäiselle ruokalajille.

    Attributes:
        name: ruokalajin nimi.
        ingredients: lista raaka-aineista, yleensä listallinen Ingredient-olioita.
        db_id: tietokannan id, mikäli olemassa. Vapaaehtoinen.
    """

    def __init__(self, name, ingredients, db_id=None):
        """Konstruktori, luo uuden ruokalajin.

        Args:
            name: ruokalajin nimi.
            ingredients: lista raaka-aineista, yleensä listallinen Ingredient-olioita.
            db_id: tietokannan id, mikäli olemassa. Vapaaehtoinen.
        """

        self.name = name
        self.ingredients = ingredients
        self.db_id = db_id

    def __str__(self):
        """Metodi, joka palauttaa olion nimen merkkijonona.

        Returns:
            Olion nimi merkkijonona.
        """
        return self.name
