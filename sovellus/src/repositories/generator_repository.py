from database_connection import get_database_connection

class GeneratorRepository:
    """[summary]
    """

    def __init__(self):
        """[summary]
        """
        self.connection = get_database_connection()

    def find_all_meals(self):
        return self._read("SELECT * FROM meals")

    def find_meal(self, meal):
        query = "SELECT * FROM meals WHERE name = ?"

        return self._read(query, meal)

    def find_all_ingredients(self):
        return self._read("SELECT * FROM ingredients")

    def find_ingredient(self, ingredient):
        query = "SELECT * FROM ingredients WHERE name = ?"

        return self._read(query, ingredient)

    def find_ingredients_of_meal(self,meal):
        query = '''SELECT I.name FROM ingredients I
            LEFT JOIN relations R ON I.id = R.ingredientID
            LEFT JOIN meals M ON R.mealID = M.id
            WHERE M.name = ?'''

        return self._read(query, meal)

    ### POISTHA!!!!
    def errorin_testaus(self):
        return self._read("SELECT * FROM neekeri")
    ### POISTHA!!!!

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

    def _write(self, query, var):
        cursor = self.connection.cursor()

        cursor.execute(query, var)
        self.connection.commit()
