"""Meal set-moduuli, joka tarjoaa sovelluksen ruokalajien vakiokirjaston ja sen metodit."""

from entities.meal import Meal
from entities.ingredient import Ingredient
from repositories.meal_repository import MealRepository as default_repo

class MealSet():
    """MealSet-luokka tarjoaa listat ja metodit vakio-ruokalajeista raaka-aineineen.

    Metodeilla voidaan luoda ruokalajeista ja raaka-aineista ilmentymiä, tai listoja voidaan
    käyttää semmoisenaan, esimerkiksi testaamisessa. Listan ruokalajeista alustetaan myös
    sovelluksen käyttäjien vakiokirjasto, josta ruokalajit luetaan.
    """

    def __init__(self, repository=default_repo()):
        """Konstruktori, alustaa listat ja tarvittavan repository-luokan.

        Repository voidaan tarjota parametrina, tai sitten käytetään omaa importtia. Testeissä
        on kätevä tarjota parametrina sama repository-luokka, jota käytetään testaamiseen. Tällöin
        ruokalajit ja raaka-aineet ovat metodien pyytämisen jälkeen valmiiksi
        oikeassa tietokannassa.

        Args:
            repository: vapaaehtoinen repository-luokka, joka hoitaa tietokantatoiminnot.
        """

        self.repository = repository

        self.meals = [
            'Makaronilaatikko',
            'Kanasalaatti',
            'Uunimakkara',
            'Pizza',
            'Pinaattilätyt',
            'Kaalilaatikko',
            'Lihaa ja perunaa']

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
            'Pinaattilätyt',
            'Kaali',
            'Riisiä',
            'Liha',
            'Peruna']

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
        """Palauttaa luokan käyttämän repository-luokan."""

        return self.repository

    def create_meals(self, user):
        """Luo attribuutin ruokalajilistasta listallisen ruokalajien ilmentymiä.

        Ruokalajit lisätään samalla myös tietokantaan ja liitetään parametrina
        annettuun käyttäjään.

        Args:
            user: käyttäjä, johon ruokalajit liitetään.

        Returns:
            Palauttaa listan ruokalajien ilmentymiä, eli Meal-objekteja.
        """

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
        """Luo attribuutin listasta listallisen raaka-aineiden ilmentymiä.

        Returns:
            Palauttaa listallisen Ingredient-objekteja.
        """

        ingredients = []

        for ingredient in self.ingredients:
            ingredients.append(Ingredient(ingredient))

        return ingredients
