class Meal:
    """Class for single meal,
    """

    def __init__(self, name, ingredients, db_id=None):
        """Konstruktori

        Args:
            name ([type]): [description]
            ingredients ([type]): [description]
        """
        self.name = name
        self.ingredients = ingredients
        self.db_id = db_id

    def __str__(self):
        return self.name
