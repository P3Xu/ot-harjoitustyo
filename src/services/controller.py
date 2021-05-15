"""Controller-moduuli, toimittaa rajapinnan sovelluksen tiedonhallintaan."""

from entities.user import User
from entities.meal import Meal
from entities.menu import Menu
from entities.ingredient import Ingredient
from services.generator import GeneratorService
from repositories.meal_repository import MealRepository
from repositories.menu_repository import MenuRepository
from repositories.user_repository import UserRepository
from repositories.library_repository import LibraryRepository

class Controller:
    """Controller-luokka tarjoaa rajapinnan sovelluksen tietokohteisiin ja pysyväistallennuksiin.

    Controllerin tehtävä on tarjota käyttöliittymälle kaikki tarvittavat operaatiot sovelluksen
    tietojen käsittelyyn ja pysyväistallennukseen.
    """

    def __init__(self,
        meal_repository = MealRepository(),
        menu_repository = None,
        user_repository = UserRepository(),
        library_repository = LibraryRepository()):

        """Konstruktori, alustaa controllerin tarvitsemat repository-luokat, sekä pitää kirjaa
        siitä, minkä käyttäjän tietoja kulloinkin käsitellään.
        """

        self.meal_repository = meal_repository
        self.menu_repository = menu_repository
        self.user_repository = user_repository
        self.lib_repository = library_repository

        if not self.menu_repository:
            self.menu_repository = MenuRepository(self.meal_repository)

        self.user = None

    def generate_menu(self):
        """Metodi, joka pyytää GeneratorService-luokkaa generoimaan uuden menun.

        Metodi tarkistaa, että saatu objekti on varmasti Menu-objekti, ennen sen lähettämistä
        tallennettavaksi tietokantaan.
        """

        menu = GeneratorService(self.meal_repository, self.user).generate()

        if isinstance(menu, Menu):
            self.menu_repository.insert_menu(menu)

    def fetch_meals(self):
        """Pyytää kaikki käyttäjän ruokalajit tietokannasta.

        Returns:
            Palauttaa listallisen Meal-objekteja, mikäli tietokannasta löytyy tuloksia. Muuten
            palauttaa tyhjän listan.
        """

        return self.meal_repository.find_all_meals(self.user)

    def fetch_ingredients(self):
        """Pyytää kaikki käyttäjän ruokalajien raaka-aineet tietokannasta.

        Returns:
            Palauttaa listallisen Ingredient-objekteja, tai hakutulosten puuttuessa tyhjän listan.
        """

        return self.meal_repository.find_all_ingredients(self.user)

    def fetch_menu(self):
        """Pyytää tietokannasta käyttäjän viimeisimmän ruokalistan, mikäli sellainen on generoitu.

        Returns:
            Palauttaa Menu-objektin, tai hakutuloksen puuttuessa Nonen.
        """

        menu = self.menu_repository.find_menu(self.user)

        if isinstance(menu, int):
            return None

        return menu

    def add_ingredients(self, ingredients):
        """Lisää tietokantaan yhden ruokalajin raaka-aineet.

        Saa argumenttina listallisen raaka-aineita str-muodossa, jotka iteroidaan läpi ja lisätään
        yksitellen tietokantaan. Jokaisen kohdalla tarkistetaan, onko merkkijono tyhjä sekä
        löytyykö ingredients-taulusta jo samanniminen raaka-aine ja matchin sattuessa luodaan
        Ingredient-objekti, jolle annetaan saatu tietokannan id. Muutoin tallennetaan uusi
        raaka-aine tietokantaan, jonka jälkeen luodaan Ingredient-objekti, jolle annetaan saatu
        tietokanta-id mukaan. Lopuksi tallennetaan kummassa tahansa tapauksessa luotu
        objekti palautettavaan listaan.

        Args:
            ingredients: lista yhden ruokalajin raaka-aineita str-muodossa.

        Returns:
            Palauttaa listan, joka sisältää ruokalajin raaka-aineiden ilmentymiä. Tai Nonen,
            mikäli lista on tyhjä.
        """

        inserted_ingredients = []

        for ingredient in ingredients:
            if len(ingredient.strip()) == 0:
                continue

            ingredient = ingredient.capitalize()
            check = self.meal_repository.fetch_item_id(ingredient, False)

            if check:
                db_ingredient = Ingredient(ingredient, check)
            else:
                db_ingredient = self.meal_repository.insert_ingredient(
                    Ingredient(ingredient))

            inserted_ingredients.append(db_ingredient)

        return None if len(inserted_ingredients) == 0 else inserted_ingredients

    def add_meal(self, meal, ingredients):
        """Lisää tietokantaan ruokalajin.

        Metodi lisää tietokantaan annetun ruokalajin. Metodi ei erikseen tarkista ruokalajin
        olemassaoloa tietokannassa, vaan laittaa Meal-objektin raaka-aineet saatuaan suoraan
        eteenpäin repository-luokalle. Mikäli raaka-aineita ei ole, keskeytyy suoritus ja
        palautetaan None.

        Args:
            meal: lisättävän ruokalajin nimi str-muotoisena.
            ingredients: lisättävän ruokalajin raaka-aineet listana str-muodossa.

        Returns:
            Palauttaa tietokantaan lisätyn ruokalajin id-numeron, tai Nonen mikäli raaka-aineita
            ei ole.
        """

        db_ingredients = self.add_ingredients(ingredients)

        if not db_ingredients:
            return None

        meal = self.meal_repository.insert_meal(
            Meal(meal.capitalize(), db_ingredients), self.user)

        return meal

    def add_user(self, username, password, config_file=False):
        """Lisää uuden käyttäjän tietokantaan.

        Metodi tarkistaa ensiksi, löytyykö tietokannasta jo samannimistä käyttäjää ja jos löytyy,
        niin palauttaa suoraan Nonen. Mikäli duplikaattia ei löydy, tarkistetaan seuraavaksi, onko
        annettu parametrina oma vakiokirjasto ruokalajeille. Jos ei ole, käytetään järjestelmän
        omaa vakiokirjastoa. Tämän jälkeen lisätään käyttäjä tietokantaan ja asetetaan käyttäjä
        luokan käyttäjäksi. Sen jälkeen lisätään käyttäjälle vakio-ruokalajit tietokantaan.

        Args:
            username: käyttäjätunnus str-muotoisena.
            password: salasana str-muotoisena.
            config_file: vapaaehtoinen ruokalajikirjasto, käytetään jos annettu, muutoin
            käytetään järjestelmän omaa kirjastoa.

        Returns:
            Palauttaa joko käyttäjälle annetun tietokannan id-numeron tai Nonen, mikäli
            käyttäjätunnus on jo olemassa.
        """

        check = self._check_duplicates_username(username)

        if not check:
            if config_file:
                meals = self.lib_repository.read_meals(config_file)
            else:
                meals = self.lib_repository.read_meals()

            uid = self.user_repository.add_user(username, password)

            self.user = User(username, password, uid)
            self._insert_default_meals(meals)

            return uid

        return None

    def login_user(self, username, password):
        """Kirjaa käyttäjän sisään.

        Metodilla kirjataan käyttäjä sisään, jolloin käyttäjä asetetaan luokan käyttäjäksi
        ja luokan toiminnot suoritetaan kyseiseen käyttäjään liittäen.

        Args:
            username: käyttäjätunnus str-muotoisena.
            password: salasana str-muotoisena.

        Returns:
            Jos käyttäjätunnusta ei ole olemassa, tai salasana ei täsmää, palautetaan None.
            Muutoi palautetaan kokonaisluku 0.
        """

        result = self.user_repository.find_by_username(username)

        if (not result or username not in result.name or password not in result.password):
            return None

        self.user = result

        return 0

    def logout_user(self):
        """Kirjaa käyttäjän ulos.

        Kirjaamalla käyttäjän ulos varmistetaan, ettei kyseiseen käyttäjään liittyviä tietoja enää
        vahingossa käsitellä.
        """

        self.user = None

    def remove_meal(self, meal):
        """Poistaa annetun ruokalajin käyttäjältä.

        Ennen poistoa haetaan tietokannasta poistettava ruokalaji, sekä käyttäjän ruokalista,
        mikäli generoitu. Tarkistetaan, että onko kyseinen ruokalaji arvottu ruokalistalle ja jos
        on, niin poistetaan myös ruokalista ruokalajin lisäksi, sillä poistettu ruokalaji ei voi
        olla enää ruokalistalla.

        Args:
            meal: ruokalajin nimi str-muotoisena.
        """

        get_meal = self.meal_repository.find_single_meal(meal, self.user)
        get_menu = self.fetch_menu()

        if get_meal:
            if get_menu:
                menu_meals = [meal.name for meal in get_menu.meals]

                if get_meal.name in menu_meals:
                    self.menu_repository.initialize_menus(self.user)

            self.meal_repository.remove_meal(get_meal, self.user)

    def export_wishlist(self, wishlist, directory):
        """Pyytää kirjasto-repositorya tulostamaan ruokalistan raaka-aineet.

        Generoidun ruokalistan raaka-aineet tulostetaan tekstitiedostoon.

        Args:
            wishlist: ruokalistan raaka-aineiden nimet str-muotoisena listassa.
        Returns:
            Palauttaa generoidun tekstitiedoston polun merkkijonona.
        """

        return self.lib_repository.write_wishlist(wishlist, directory)

    def _insert_default_meals(self, meals):
        for meal in meals:
            self.add_meal(meal.name, meal.ingredients)

    def _check_duplicates_username(self, username):
        return self.user_repository.find_by_username(username)
