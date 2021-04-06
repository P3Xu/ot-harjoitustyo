class Ingredient:
    """Class for a single ingredient
    """

    def __init__(self, name, db_id=None, red_meat=False):
        """Konstruktori, luo uuden ainesosan.

        Args:
            name ([type]): [description]
            red_meat (bool, optional): [description]. Defaults to False.
        """
        self.name = name
        self.db_id = db_id
        self.meat = red_meat

    def __str__(self):
        return self.name
        