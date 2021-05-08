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

    def find_all_meals(self, user):
        """EN OLE VARMA TUOSTA DISTINCTISTA, KATSELLAAN SITÄ VIELÄ"""

        meals = self.i_o.read("""SELECT DISTINCT M.name, m.id FROM meals M LEFT JOIN
            meal_relations R ON M.id = R.mealID WHERE userID = ?""", [user.id])

        meals = [
            Meal(
                meal['name'],
                self._find_meal_ingredients(meal['id'], user),
                meal['id']
            )
        for meal in meals]

        return meals

    def find_single_meal(self, criterion, user):
        if isinstance(criterion, str):
            query = """SELECT M.name, M.id FROM meals M LEFT JOIN meal_relations R ON
                M.id = R.mealID WHERE M.name = ? AND R.userID = ?"""
        elif isinstance(criterion, int):
            query = """SELECT M.name, M.id FROM meals M LEFT JOIN meal_relations R ON
                M.id = R.mealID WHERE M.id = ? AND R.userID = ?"""
        else:
            return None

        result = self.i_o.read(query, [criterion, user.id])

        if len(result) > 0:
            res = result[0]

            return Meal(res['name'],self._find_meal_ingredients(res['id'],user), res['id'])

        return result

    def find_all_ingredients(self, user):
        ingredients = self.i_o.read("""SELECT * FROM ingredients I LEFT JOIN meal_relations R ON
            I.id = R.ingredientID WHERE R.userID = ?""", [user.id])

        ingredients = [
            Ingredient(
                ingredient['name'],
                ingredient['id'],
            )
        for ingredient in ingredients]

        return ingredients

    def find_single_ingredient(self, criterion, user):
        if isinstance(criterion, str):
            query = """SELECT * FROM ingredients I LEFT JOIN meal_relations R ON
                I.id = R.ingredientID WHERE I.name = ? AND R.userID = ?"""
        else:
            return None

        result = self.i_o.read(query, [criterion, user.id])

        if len(result) > 0:
            ingredient = result[0]

            return Ingredient(ingredient['name'], ingredient['id'])

        return result

    def insert_ingredient(self, ingredient):
        query = "INSERT OR IGNORE INTO ingredients (name) VALUES (?)"

        db_id = self.i_o.write(query, [ingredient.name])

        return Ingredient(ingredient.name, db_id)

    def insert_meal(self, meal, user):
        query = "INSERT OR IGNORE INTO meals (name) VALUES (?)"

        db_id = self.i_o.write(query, [meal.name])

        for ingredient in meal.ingredients:
            self._insert_relation((db_id, user.id, ingredient.db_id))

        return db_id

    def empty_tables(self):
        self.i_o.run_command("DELETE FROM meals")
        self.i_o.run_command("DELETE FROM meal_relations")
        self.i_o.run_command("DELETE FROM ingredients")

    def _find_meal_ingredients(self, meal_id, user):
        query = """SELECT I.id, I.name FROM ingredients I
            LEFT JOIN meal_relations R ON I.id = R.ingredientID
            LEFT JOIN meals M ON R.mealID = M.id
            WHERE M.id = ? AND R.userID = ?"""

        items = self.i_o.read(query, [meal_id, user.id])
        items = [Ingredient(item['name'], item['id']) for item in items]

        return items

    def _insert_relation(self, relation):
        query = "INSERT INTO meal_relations (mealID, userID, ingredientID) VALUES (?, ?, ?)"
        (meal_id, user_id, ingredient_id) = relation

        self.i_o.write(query, [meal_id, user_id, ingredient_id])
