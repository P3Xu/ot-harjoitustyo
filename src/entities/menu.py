class Menu:
    """Viikon ruokalistan ilmentymä.

    Attributes:
        meals: lista ruokalajeja, Meal-olioiden muodossa.
        date: aikaleima ruokalistan luonnille.
        user: ruokalistan käyttäjä.
    """

    def __init__(self, meals, date, user):
        """Konstruktori, luo uuden ruokalistan.

        Args:
            meals: lista ruokalajeja, Meal-olioiden muodossa.
            date: aikaleima ruokalistan luonnille.
            user: käyttäjä, johon kyseinen ruokalista liitetään.
        """

        self.meals = meals
        self.date = date
        self.user = user

    def get_meals(self):
        """Metodi, jolla haetaan ruokalistan ruokalajit.

        Returns:
            Palauttaa ruokalistan ruokalajit, eli listallisen Meal-objekteja.
        """

        return self.meals

    def get_date(self):
        """Metodi, jolla haetaan ruokalistan aikaleima.

        Returns:
            Palauttaa ruokalistan aikaleiman.
        """

        return self.date
