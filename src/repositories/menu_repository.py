from database_connection import get_database_connection
from entities.menu import Menu

class MenuRepository:
    """[summary]
    """

    def __init__(self, meal_repository):
        """[summary]
        """
        self.connection = get_database_connection()
        self.meal_repo = meal_repository

    def initialize_menus(self):
        """Metodi taulun alustamiselle, joka ei toistaiseksi säilö aiempia ruokalistoja
        """
        self.connection.execute("DELETE FROM menus")
        self.connection.commit()

    def insert_menu(self, menu):
        values = [(meal.db_id,menu.date) for meal in menu.meals]

        self.initialize_menus()
        self._write("INSERT INTO menus (mealID, date) VALUES (?, ?)", values)

    def find_menu(self):
        meals = self._read("SELECT * FROM menus")

        if len(meals) == 0:
            return -1

        date = meals[0]['date']
        meals = [self.meal_repo.find_single_meal(int(meal['mealID'])) for meal in meals]

        return Menu(meals, date)

    def _read(self, query, var=False):
        try:
            with self.connection:
                if var is False:
                    results = self.connection.execute(query).fetchall()
                else:
                    results = self.connection.execute(query,[var]).fetchall()

                return results

        except self.connection.Error as error:
            return error

    def _write(self, query, values):
        cursor = self.connection.cursor()

        cursor.executemany(query, values)
        self.connection.commit()
