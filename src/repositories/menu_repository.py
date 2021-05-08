from entities.menu import Menu
from repositories.io import InputOutput

class MenuRepository:
    """[summary]
    """

    def __init__(self, meal_repository):
        """[summary]
        """
        self.i_o = InputOutput()
        self.meal_repo = meal_repository

    def initialize_menus(self, user):
        """Metodi taulun alustamiselle, joka ei toistaiseksi säilö aiempia ruokalistoja"""

        self.i_o.write("DELETE FROM menus WHERE userID = ?", [user.id])

    def empty_menu_table(self):
        """Metodi koko menu-taulun tyhjentämiselle, käytetään lähinnä testaamisessa."""

        self.i_o.run_command("DELETE FROM menus")

    def insert_menu(self, menu, user):
        values = [(meal.db_id, user.id, menu.date) for meal in menu.meals]

        self.initialize_menus(user)
        self.i_o.write("INSERT INTO menus (mealID, userID, date) VALUES (?, ?, ?)", values, False)

    def find_menu(self, user):
        meals = self.i_o.read("SELECT * FROM menus WHERE userID = ?", user.id)

        if len(meals) == 0:
            return -1

        date = meals[0]['date']
        meals = [self.meal_repo.find_single_meal(int(meal['mealID'])) for meal in meals]

        return Menu(meals, date)
