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

        """TÄNNEKIN VOISI HARKITA OMAA USERS-ATTRIBUUTTIA???"""


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
        ingredients = self.i_o.read("""SELECT DISTINCT I.name, I.id FROM meal_relations R LEFT JOIN
            ingredients I ON R.ingredientID = I.id WHERE R.userID = ?""", [user.id])

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

    def fetch_item_id(self, item, meal=True):
        if meal:
            query = "SELECT * FROM meals WHERE name = ?"
        else:
            query = "SELECT * FROM ingredients WHERE name = ?"

        result = self.i_o.read(query, [item])

        if len(result) > 0:
            return result[0]['id']

        return None

    def insert_ingredient(self, ingredient):
        query = "INSERT INTO ingredients (name) VALUES (?)"

        db_id = self.i_o.write(query, [ingredient.name])

        return Ingredient(ingredient.name, db_id)

    def insert_meal(self, meal, user):
        check = self.fetch_item_id(meal.name)

        query = "INSERT INTO meals (name) VALUES (?)"

        meal_db_id = check if check else self.i_o.write(query, [meal.name])

        for ingredient in meal.ingredients:
            self._insert_relation((user.id, meal_db_id, ingredient.db_id))

        return meal_db_id

    def empty_tables(self):
        self.i_o.run_command("DELETE FROM meals")
        self.i_o.run_command("DELETE FROM meal_relations")
        self.i_o.run_command("DELETE FROM ingredients")

    def _find_meal_ingredients(self, meal_id, user):
        query = """SELECT I.id, I.name FROM ingredients I
            LEFT JOIN meal_relations R ON I.id = R.ingredientID
            LEFT JOIN meals M ON R.mealID = M.id
            WHERE M.id = ? AND R.userID = ?"""

        results = self.i_o.read(query, [meal_id, user.id])
        items = [Ingredient(item['name'], item['id']) for item in results]

        return items

    def _insert_relation(self, relation):
        query = "INSERT OR IGNORE INTO meal_relations (userID, mealID, ingredientID) VALUES (?,?,?)"
        (user_id, meal_id, ingredient_id) = relation

        self.i_o.write(query, [user_id, meal_id, ingredient_id])
