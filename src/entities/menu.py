class Menu:
    def __init__(self, meals, date):
        self.meals = meals
        self.date = date

    def get_meals(self):
        return self.meals

    def get_date(self):
        return self.date
