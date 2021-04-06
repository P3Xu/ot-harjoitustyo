from database_connection import get_database_connection
from entities.ingredient import Ingredient
from entities.meal import Meal
from entities.menu import Menu

class GeneratorRepository:
    """[summary]
    """

    def __init__(self):
        """[summary]
        """
        self.connection = get_database_connection()

    def find_all_meals(self):
        meals = self._read("SELECT * FROM meals")

        meals = [
            Meal(
                meal['name'],
                self.find_meal_ingredients(meal['name']),
                meal['id']
            )
        for meal in meals]

        return meals

    def find_meal_by_name(self, name):
        meal = self._read("SELECT * FROM meals WHERE name = ?", name)[0]

        return Meal(meal['name'], self.find_meal_ingredients(meal['name']), meal['id'])

    def find_meal_by_id(self, meal_id):
        meal = self._read("SELECT * FROM meals WHERE id = ?", meal_id)[0]

        return Meal(meal['name'], self.find_meal_ingredients(meal['name']), meal['id'])

    def find_all_ingredients(self):
        ingredients = self._read("SELECT * FROM ingredients")

        ingredients = [
            Ingredient(
                ingredient['name'],
                ingredient['id'],
            )
        for ingredient in ingredients]

        return ingredients

    def find_ingredient(self, name):
        ingredient = self._read("SELECT * FROM ingredients WHERE name = ?", name)[0]

        return Ingredient(ingredient['name'], ingredient['id'])

    def find_meal_ingredients(self, meal):
        query = """SELECT I.id, I.name FROM ingredients I
            LEFT JOIN relations R ON I.id = R.ingredientID
            LEFT JOIN meals M ON R.mealID = M.id
            WHERE M.name = ?"""

        items = self._read(query, meal)
        items = [Ingredient(item['name'], item['id']) for item in items]

        return items

    def initialize_menus(self):
        self.connection.execute("DELETE FROM menus")
        self.connection.commit()

    def insert_menu(self, menu):
        values = [(meal.db_id,menu.get_date()) for meal in menu.get_meals()]

        self.initialize_menus()
        self._write("INSERT INTO menus (mealID, date) VALUES (?, ?)", values)

    def find_menu(self):
        meals = self._read("SELECT * FROM menus")

        if len(meals) == 0:
            return -1

        date = meals[0]['date']
        meals = [self.find_meal_by_id(i['mealID']) for i in meals]

        return Menu(meals, date)

    def _read(self, query, var=False):
        items = []

        try:
            with self.connection:
                if var is False:
                    results = self.connection.execute(query).fetchall()
                    items.append(results)
                    return results
                else:
                    results = self.connection.execute(query,[var]).fetchall()
                    items.append(results)
                    return results

        except self.connection.Error as error:
            return error

    def _write(self, query, values):
        cursor = self.connection.cursor()

        cursor.executemany(query, values)
        self.connection.commit()
