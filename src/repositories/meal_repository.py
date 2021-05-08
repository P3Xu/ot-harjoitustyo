from entities.meal import Meal
from entities.ingredient import Ingredient
from repositories.io import InputOutput

class MealRepository:
    """[summary]
    """

    def __init__(self):
        """[summary]
        """
        self.i_o = InputOutput()

    def find_all_meals(self):
        meals = self.i_o.read("SELECT * FROM meals")

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

        result = self.i_o.read(query, criterion)

        if len(result) > 0:
            result = result[0]

            return Meal(result['name'], self._find_meal_ingredients(result['id']), result['id'])

        return result

    def find_all_ingredients(self):
        ingredients = self.i_o.read("SELECT * FROM ingredients")

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

        result = self.i_o.read(query, criterion)

        if len(result) > 0:
            ingredient = result[0]

            return Ingredient(ingredient['name'], ingredient['id'])

        return result

    def insert_ingredient(self, ingredient):
        query = "INSERT OR IGNORE INTO ingredients (name) VALUES (?)"

        db_id = self.i_o.write(query, [ingredient.name])

        return Ingredient(ingredient.name, db_id)

    def insert_meal(self, meal):
        query = "INSERT OR IGNORE INTO meals (name) VALUES (?)"

        db_id = self.i_o.write(query, [meal.name])

        for ingredient in meal.ingredients:
            self._insert_relation((db_id, ingredient.db_id))

        return db_id

    def empty_tables(self):
        self.i_o.run_command("DELETE FROM meals")
        self.i_o.run_command("DELETE FROM meal_relations")
        self.i_o.run_command("DELETE FROM ingredients")

    def _find_meal_ingredients(self, meal_id):
        query = """SELECT I.id, I.name FROM ingredients I
            LEFT JOIN meal_relations R ON I.id = R.ingredientID
            LEFT JOIN meals M ON R.mealID = M.id
            WHERE M.id = ?"""

        items = self.i_o.read(query, meal_id)
        items = [Ingredient(item['name'], item['id']) for item in items]

        return items

    def _insert_relation(self, relation):
        query = "INSERT INTO meal_relations (mealID, ingredientID) VALUES (?, ?)"
        (meal_id, ingredient_id) = relation

        self.i_o.write(query, [meal_id, ingredient_id])
