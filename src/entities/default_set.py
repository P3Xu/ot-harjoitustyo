from entities.meal import Meal
from entities.ingredient import Ingredient

class DefaultSet():
    """[summary]
    """

    def __init__(self):
        """[summary]
        """

        self.meals = [
            'Makaronilaatikko',
            'Kanasalaatti',
            'Uunimakkara',
            'Pizza',
            'Pinaattilätyt',
            'Kaalilaatikko',
            'Possuwokki',
            'Kalapuikot'
        ]

        self.ingredients = [
            'Jauheliha',
            'Makaroni',
            'Sipuli',
            'Kanan fileesuikale',
            'Salaatti',
            'Lenkkimakkara',
            'Juusto',
            'Kinkkusuikale',
            'Ananaspalat',
            'Aurajuusto',
            'Pizzajauhot',
            'Hiiva',
            'Pinaattilätty',
            'Kaali',
            'Riisiä',
            'Possun fileesuikale',
            'Wokkivihannekset',
            'Kalapuikot'
        ]

        self.relations = [
            (0, 0),
            (0, 1),
            (0, 2),
            (1, 3),
            (1, 4),
            (2, 5),
            (2, 6),
            (3, 7),
            (3, 8),
            (3, 9),
            (3, 10),
            (3, 11),
            (4, 12),
            (5, 0),
            (5, 2),
            (5, 13),
            (5, 14),
            (6, 15),
            (6, 16),
            (7, 17),
        ]

    def create_meals(self):
        meals = []

        for i in range(len(self.meals)):
            ingredients = []

            for relation in self.relations:
                (meal_id, ingredient_id) = relation

                if meal_id == i:
                    ingredients.append(ingredient_id)

            meals.append(
                Meal(self.meals[i], ingredients)
            )

        return meals

    def create_ingredients(self):
        ingredients = []

        for ingredient in self.ingredients:
            ingredients.append(Ingredient(ingredient))

        return ingredients

    def create_db_relations(self):
        relations = []

        for relation in self.relations:
            (meal_id, ingredient_id) = relation

            relations.append((meal_id+1, ingredient_id+1))

        return relations
