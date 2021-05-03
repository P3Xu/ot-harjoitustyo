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
                self._find_meal_ingredients(meal['id']),
                meal['id']
            )
        for meal in meals]

        return meals

    def find_single_meal(self, criterion):
        if isinstance(criterion, str):
            query = "SELECT * FROM meals WHERE name = ? LIMIT 1"
        elif isinstance(criterion, int):
            query = "SELECT * FROM meals WHERE id = ? LIMIT 1"
        else:
            return None

        result = self._read(query, criterion)

        if len(result) > 0:
            result = result[0]

            return Meal(result['name'], self._find_meal_ingredients(result['id']), result['id'])

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

    def find_single_ingredient(self, criterion):
        if isinstance(criterion, str):
            query = "SELECT * FROM ingredients WHERE name = ?"
        else:
            return None

        result = self._read(query, criterion)

        if len(result) > 0:
            ingredient = result[0]

            return Ingredient(ingredient['name'], ingredient['id'])

        return result

    def insert_ingredient(self, ingredient):
        query = "INSERT OR IGNORE INTO ingredients (name) VALUES (?)"

        db_id = self._write(query, [ingredient.name])

        return Ingredient(ingredient.name, db_id)

    def insert_meal(self, meal):
        query = "INSERT OR IGNORE INTO meals (name) VALUES (?)"

        db_id = self._write(query, [meal.name])

        for ingredient in meal.ingredients:
            self._insert_relation((db_id, ingredient.db_id))

        return db_id

    def empty_tables(self):
        self.connection.execute("DELETE FROM meals")
        self.connection.execute("DELETE FROM relations")
        self.connection.execute("DELETE FROM ingredients")
        self.connection.commit()

    def _find_meal_ingredients(self, meal_id):
        query = """SELECT I.id, I.name FROM ingredients I
            LEFT JOIN relations R ON I.id = R.ingredientID
            LEFT JOIN meals M ON R.mealID = M.id
            WHERE M.id = ?"""

        items = self._read(query, meal_id)
        items = [Ingredient(item['name'], item['id']) for item in items]

        return items

    def _insert_relation(self, relation):
        query = "INSERT INTO relations (mealID, ingredientID) VALUES (?, ?)"
        (meal_id, ingredient_id) = relation

        self._write(query, [meal_id, ingredient_id])

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

    def _write(self, query, value):
        cursor = self.connection.cursor()

        cursor.execute(query, value)
        self.connection.commit()

        return cursor.lastrowid
