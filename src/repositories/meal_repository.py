from entities.meal import Meal
from entities.ingredient import Ingredient
from database_connection import get_database_connection

class MealRepository:
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

    #def find_meal_by_name(self, name):
    #    return self._read("SELECT * FROM meals WHERE name = ?", name)

    """def find_meal_by_name(self, name):
        result = self._read("SELECT * FROM meals WHERE name = ?", name)

        if len(result) > 0:
            meal = result[0]

            return Meal(meal['name'], self.find_meal_ingredients(meal['name']), meal['id'])



    def find_meal_by_id(self, meal_id):
        result = self._read("SELECT * FROM meals WHERE id = ?", meal_id)

        if len(result) > 0:
            meal = result[0]

            return Meal(meal['name'], self.find_meal_ingredients(meal['name']), meal['id'])

        return result"""

    def find_single_meal(self, criterion):
        if type(criterion) is str:
            query = "SELECT * FROM meals WHERE name = ?"
        elif type(criterion) is int:
            query = "SELECT * FROM meals WHERE id = ?"

        result = self._read(query, criterion)

        if len(result) > 0:
            meal = result[0]

            return Meal(meal['name'], self.find_meal_ingredients(meal['name']), meal['id'])

        return result

    def find_all_ingredients(self):
        ingredients = self._read("SELECT * FROM ingredients")

        ingredients = [
            Ingredient(
                ingredient['name'],
                ingredient['id'],
            )
        for ingredient in ingredients]

        return ingredients

    def find_ingredient_by_name(self, ingredient):
        """POISTA DUPLIKAATIT, NYT SAMANLAINEN FIND_INGREDIENTIN KANSSA"""
        return self._read("SELECT * FROM ingredients WHERE name = ?", ingredient)

    def find_meal_ingredients(self, meal):
        query = """SELECT I.id, I.name FROM ingredients I
            LEFT JOIN relations R ON I.id = R.ingredientID
            LEFT JOIN meals M ON R.mealID = M.id
            WHERE M.name = ?"""

        items = self._read(query, meal)
        items = [Ingredient(item['name'], item['id']) for item in items]

        return items

    def insert_ingredient(self, ingredient):
        query = "INSERT INTO ingredients (name) VALUES (?)"

        return self._write(query, [ingredient])

    def insert_meal(self, meal):
        return self._write("INSERT INTO meals (name) VALUES (?)", [meal])

    def check_latest_id(self, which=False):
        if which is False:
            return self._read("SELECT id FROM ingredients ORDER BY id DESC LIMIT 1")

        return self._read("SELECT id FROM meals ORDER BY id DESC LIMIT 1")

    def update_relations(self, relations):
        query = "INSERT INTO relations (mealID, ingredientID) VALUES (?, ?)"

        for relation in relations:
            (meal_id, ingredient_id) = relation

            self._write(query, [meal_id, ingredient_id])

    def empty_tables(self):
        self.connection.execute("DELETE FROM meals")
        self.connection.execute("DELETE FROM relations")
        self.connection.execute("DELETE FROM ingredients")
        self.connection.commit()

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

    def _write(self, query, value):
        cursor = self.connection.cursor()

        cursor.execute(query, value)
        self.connection.commit()

        return cursor.lastrowid
