from entities.menu import Menu
from repositories.io import InputOutput as default_io

class MenuRepository:
    """[summary]
    """

    def __init__(self, meal_repository, i_o=default_io()):
        """[summary]
        """
        self.i_o = i_o
        self.meal_repo = meal_repository

    def empty_menu_table(self):
        """Metodi koko menu-taulun tyhjentämiselle, käytetään lähinnä testaamisessa."""

        self.i_o.run_command("DELETE FROM menus")

    def insert_menu(self, menu):
        user = menu.user
        values = [(meal.db_id, user.id, menu.date) for meal in menu.meals]

        self.initialize_menus(user)
        self.i_o.write("INSERT INTO menus (mealID, userID, date) VALUES (?, ?, ?)", values, False)

    def find_menu(self, user):
        menu = self.i_o.read("SELECT * FROM menus WHERE userID = ?", [user.id])

        if len(menu) == 0:
            return -1

        date = menu[0]['date']
        meals = [self.meal_repo.find_single_meal(int(meal['mealID']), user) for meal in menu]

        return Menu(meals, date, user)

    def initialize_menus(self, user):
        """Metodi taulun alustamiselle, joka ei toistaiseksi säilö aiempia ruokalistoja"""

        self.i_o.write("DELETE FROM menus WHERE userID = ?", [user.id])
