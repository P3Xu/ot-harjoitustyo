from entities.meal import Meal
from entities.ingredient import Ingredient
from repositories.meal_repository import MealRepository as default_repo

class MealSet():
    def __init__(self, repository=default_repo()):
        self.repository = repository

        self.meals = [
            'Makaronilaatikko',
            'Kanasalaatti',
            'Uunimakkara',
            'Pizza',
            'Pinaattilätyt',
            'Kaalilaatikko',
            'Possuwokki']

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
            'Wokkivihannekset']

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
            (6, 16)]

    def get_repository(self):
        return self.repository

    def create_meals(self, user):
        meals = []

        for i in range(len(self.meals)):
            ingredients = []

            for relation in self.relations:
                (meal_id, ingredient_id) = relation

                if meal_id == i:
                    check = self.repository.fetch_item_id(self.ingredients[ingredient_id], False)

                    if check:
                        db_ingredient = Ingredient(self.ingredients[ingredient_id], check)
                    else:
                        db_ingredient = self.repository.insert_ingredient(
                            Ingredient(self.ingredients[ingredient_id]))

                    ingredients.append(db_ingredient)

            meal = Meal(self.meals[i], ingredients)
            meal.db_id = self.repository.insert_meal(meal, user)

            meals.append(meal)

        return meals

    def create_ingredients(self):
        ingredients = []

        for ingredient in self.ingredients:
            ingredients.append(Ingredient(ingredient))

        return ingredients
