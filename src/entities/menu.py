class Menu:
    """Luokka viikon ruokalistalle.

    Attributes:
        meals: lista ruokalajeja, Meal-olioiden muodossa.
        date: aikaleima ruokalistan luonnille.
    """

    def __init__(self, meals, date):
        """Konstruktori, luo uuden ruokalistan.

        Args:
            meals: lista ruokalajeja, Meal-olioiden muodossa.
            date: aikaleima ruokalistan luonnille.
        """

        self.meals = meals
        self.date = date

    def get_meals(self):
        """Metodi, jolla haetaan ruokalistan ruokalajit.

        Returns:
            Palauttaa ruokalistan ruokalajit, eli listallisen Meal-olioita.
        """

        return self.meals

    def get_date(self):
        """Metodi, jolla haetaan ruokalistan aikaleima.

        Returns:
            Palauttaa ruokalistan aikaleiman.
        """

        return self.date
