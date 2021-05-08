from entities.meal import Meal
from entities.ingredient import Ingredient

class DefaultSet():
    """
    Luokka kovakoodatulle setille valmiita ruokalajeja raaka-aineineen.
    Luokkaa voidaan hyödyntää tietokannan alustuksen lisäksi testeissä, jolloin jokaiseen
    testiin ei tarvitse erikseen kirjoitella käsin lisättäviä ruokia tai raaka-aineita, vaan
    riittää importata tämä moduuli ja kutsua moduulin metodeja tai attribuutteja.

    Attributes:
        meals: kovakoodatut ruokalajit.
        ingredients: ruokalajien raaka-aineet.
        relations: ruokalajien ja raaka-aineiden relaatiot.
    """

    def __init__(self):
        """Luokan konstruktori, alustaa attribuutti-listat.
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
            (1, 0, 0),
            (1, 0, 1),
            (1, 0, 2),
            (1, 1, 3),
            (1, 1, 4),
            (1, 2, 5),
            (1, 2, 6),
            (1, 3, 7),
            (1, 3, 8),
            (1, 3, 9),
            (1, 3, 10),
            (1, 3, 11),
            (1, 4, 12),
            (1, 5, 0),
            (1, 5, 2),
            (1, 5, 13),
            (1, 5, 14),
            (1, 6, 15),
            (1, 6, 16),
            (1, 7, 17),
        ]

    def create_meals(self):
        """
        Luo meals-attribuutin ruokalaji-listasta Meal-olioita.

        Returns:
            Palauttaa listallisen Meal-olioita, joiden raaka-aineina on tässä vaiheessa raaka-aine
            -listan indeksejä.
        """

        meals = []

        for i in range(len(self.meals)):
            ingredients = []

            for relation in self.relations:
                (user_id, meal_id, ingredient_id) = relation

                if meal_id == i:
                    ingredients.append(ingredient_id)

            meals.append(
                Meal(self.meals[i], ingredients)
            )

        return meals

    def create_ingredients(self):
        """
        Luo ingredients-attribuutin raaka-ainelistasta Ingredient-olioita.

        Returns:
            Palauttaa listallisen Ingredient-olioita.
        """
        ingredients = []

        for ingredient in self.ingredients:
            ingredients.append(Ingredient(ingredient))

        return ingredients

    def create_db_relations(self):
        """
        Luo relations-attribuutin listasta uuden listan tupleja, joissa on päivitetty indeksointi
        alkamaan ykkösestä, kuten tietokannan id:kin. Käytetään tietokannan alustamisessa, jolloin
        saadaan suoraan oikeat raaka-aineet vastaamaan oikeita ruokalajeja.

        Returns:
            Palauttaa listallisen tupleja, joissa on korotettu jokaisen alkuperäisen tuplen
            arvoja yhdellä.
        """

        relations = []

        for relation in self.relations:
            (user_id, meal_id, ingredient_id) = relation

            relations.append((user_id, meal_id+1, ingredient_id+1))

        return relations
