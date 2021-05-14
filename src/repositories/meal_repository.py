from entities.meal import Meal
from entities.ingredient import Ingredient
from repositories.io import InputOutput as default_io

class MealRepository:
    """Luokka, joka hoitaa kaikki ruojalajeihin ja raaka-aineisiin liittyvät tietokantatoiminnot.

    Attributes:
        i_o: I/O-luokka, joka tarjoaa tietokannan luku- ja kirjoitustoiminnot.
    """

    def __init__(self, i_o=default_io()):
        """Konstruktori, alustaa I/O-attribuutin.

        Args:
            i_o: I/O-luokka voidaan antaa parametrina, tai oletusarvoisesti käytetään importattua
            moduulia.
        """

        self.i_o = i_o

    def find_all_meals(self, user):
        """Etsii käyttäjän ruokalajit tietokannasta.

        Pyytää I/O-luokkaa lukemaan tietokannasta parametrina annettuun käyttäjään liitetyt
        ruokalajit, jotka tulevat listana str-muodossa. Jos hakutuloksia ei ole, palautetaan
        saatu tyhjä lista ja tuloksia saadessa luodaan riviobjekteista listallinen ruokalajin
        ilmentymiä. Ilmentymään liitetään myös raaka-aine-ilmentymät, jotka haetaan toisella
        luokan omalla find_meal_ingredients()-metodilla.

        Args:
            user: käyttäjän ilmentymä, johon ruokalajit on liitetty.

        Returns:
            Palauttaa joko I/O:lta saadun tyhjän listan tai listallisen ruokalajien ilmentymiä.
        """

        meals = self.i_o.read("""SELECT DISTINCT M.name, m.id FROM meals M LEFT JOIN
            meal_relations R ON M.id = R.mealID WHERE userID = ?""", [user.id])

        if len(meals) == 0:
            return meals

        meals = [
            Meal(
                meal['name'],
                self._find_meal_ingredients(meal['id'], user),
                meal['id'])
            for meal in meals]

        return meals

    def find_single_meal(self, criterion, user):
        """Etsii yksittäisen ruokalajin tietokannasta.

        Saadessaan str- tai int-muotoisen hakuparametrin, pyytää I/O-luokkaa lukemaan tietokannasta
        parametrina annettuun käyttäjään liitetyn yksittäisen ruokalajin. Mikäli hakuparametri
        on jokin muu ilmentymä, palautetaan None. Mikäli hakutulos löytyy, palautetaan niistä
        ensimmäinen ruokaljin ilmentymänä tai jos tuloksia ei löydy, palautetaan pelkkä I/O:lta
        saatu tyhjä lista.

        Args:
            criterion: str- tai int-muotoinen hakuparametri. Merkkijonolla etsitään ruokalajin
            nimen perusteella ja kokonaisluvulla ruokalajin tietokannan id-numeron perusteella.

            user: käyttäjän ilmentymä, johon ruokalajit on liitetty.

        Returns:
            Palauttaa vääräntyyppisen hakuparametrin tapauksessa suoraan Nonen, tai tuloksia
            löytyessä ruokalajin ilmentymän. Jos hakutuloksia ei löydy, välitetään vain I/O:lta
            saatu tyhjä lista eteenpäin.
        """

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

            return Meal(res['name'], self._find_meal_ingredients(res['id'],user), res['id'])

        return result

    def find_all_ingredients(self, user):
        """Etsii kaikki käyttäjän raaka-aineet tietokannasta.

        Pyytää I/O:ta lukemaan tietokannasta kaikki käyttäjään liitetyt raaka-aineet, jotka
        palautetaan listallisena raaka-aineen ilmentymiä. Jos hakutuloksia ei löydy, välitetään
        vain I/O:lta saatu tyhjä lista suoraan eteenpäin. Muutoin luodaan hakutuloksista ensin
        asianmukaiset ilmentymät ja laitetaan ne listana eteenpäin.

        Args:
            user: käyttäjä, johon raaka-aineet on liitetty.

        Returns:
            Palauttaa joko tyhjän listan, tai listallisen raaka-aineiden ilmentymiä.
        """

        ingredients = self.i_o.read("""SELECT DISTINCT I.name, I.id FROM meal_relations R LEFT JOIN
            ingredients I ON R.ingredientID = I.id WHERE R.userID = ?""", [user.id])

        if len(ingredients) == 0:
            return ingredients

        ingredients = [
            Ingredient(
                ingredient['name'],
                ingredient['id'],
            )
        for ingredient in ingredients]

        return ingredients

    def find_single_ingredient(self, criterion, user):
        """Etsii yksittäisen raaka-aineen tietokannasta.

        Saadessaan str-muotoisen hakuparametrin, pyytää I/O-luokkaa lukemaan tietokannasta
        parametrina annettuun käyttäjään liitetyn yksittäisen raaka-aineen. Mikäli hakuparametri
        on jokin muu ilmentymä, palautetaan None. Mikäli hakutulos löytyy, palautetaan niistä
        ensimmäinen raaka-aineen ilmentymänä tai jos tuloksia ei löydy, palautetaan pelkkä I/O:lta
        saatu tyhjä lista.

        Args:
            criterion: str-muotoinen hakuparametri. Merkkijonolla etsitään raaka-ainetta
            tietokannasta sen nimen perusteella.

            user: käyttäjän ilmentymä, johon raaka-aineet on liitetty.

        Returns:
            Palauttaa vääräntyyppisen hakuparametrin tapauksessa suoraan Nonen, tai tuloksia
            löytyessä ruokalajin ilmentymän. Jos hakutuloksia ei löydy, välitetään vain I/O:lta
            saatu tyhjä lista eteenpäin.
        """

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
        """Etsii ruokalajin tai raaka-aineen id-numeron nimen perusteella.

        Tällä metodilla saadaan haettua ruokalajien ja raaka-aineiden nimiä säilövistä
        tietokantatauluista haetulle nimelle kuuluva id-numero oikeanlaisten relaatiotietojen
        säilömiseksi.

        Args:
            item: etsittävän artikkelin nimi str-muotoisena.
            meal: vapaaehtoinen meal-parametri, oletuksena True eli oletuksena etsitään ruokalajin
            id-numeroa nimen perusteeella ja Falsena raaka-aineen id:tä.

        Returns:
            Palauttaa etsityn artikkelin id-numeron, tai Nonen mikäli artikkelia ei löydetä.
        """

        if meal:
            query = "SELECT * FROM meals WHERE name = ?"
        else:
            query = "SELECT * FROM ingredients WHERE name = ?"

        result = self.i_o.read(query, [item])

        if len(result) > 0:
            return result[0]['id']

        return None

    def insert_ingredient(self, ingredient):
        """Lisää raaka-aineen tietokantaan.

        Tällä metodilla lisätään parametrina annettu raaka-aine tietokantaan. Metodi ei tarkista
        duplikaatteja, vaan tarkistus on tehtävä ennen metodin kutsumista. Taulussa on käytössä
        UNIQUE-constraint. Parametrina annetaan raaka-aineen ilmentymä, josta puretaan nimi
        mukaan parametriksi tietokantakomennolle. Metodi ei tarvitse tietoa käyttäjästä,
        sillä raaka-aineet liitetään käyttäjään ainoastaan niiden id-numeron perusteella.

        Args:
            ingredient: kantaan lisättävän raaka-aineen ilmentymä.

        Returns:
            Palauttaa raaka-aineen ilmentymän, jolla on mukanaan myös tietokannan id-numero.
        """

        query = "INSERT INTO ingredients (name) VALUES (?)"

        db_id = self.i_o.write(query, [ingredient.name])

        return Ingredient(ingredient.name, db_id)

    def insert_meal(self, meal, user):
        """Lisää ruokalajin tietokantaan.

        Metodilla lisätään parametrina saatu ruokalaji tietokantaan. Metodi tarkistaa, onko
        ruokalaji jo olemassa ja hyödyntää sen id-numeroa, mikäli sellainen on jo tietokannassa.
        Kun ruokalaji on lisätty tietokantaan, ajetaan tarvittavat relaatiot käyttäjän,
        ruokalajien sekä raaka-aineiden suhteen tietokantaan kutsumalla luokan omaa
        _insert_relation()-metodia. Lopuksi palautetaan lisätyn ruokalajin id-numero.

        Args:
            meal: lisättävän ruokalajin ilmentymä.
            user: käyttäjän ilmentymä, johon ruokalaji liitetään.

        Returns:
            Palauttaa lisätyn ruokalajin id-numeron.
        """

        check = self.fetch_item_id(meal.name)

        query = "INSERT INTO meals (name) VALUES (?)"

        meal_db_id = check if check else self.i_o.write(query, [meal.name])

        for ingredient in meal.ingredients:
            self._insert_relation((user.id, meal_db_id, ingredient.db_id))

        return meal_db_id

    def remove_meal(self, meal, user):
        """Poistaa halutun ruokalajin tietokannasta.

        Metodi poistaa melko suoraviivaisesti parametrina annetun ruokalajin parametrina annetulta
        käyttäjältä. Huomattavaa on, että tietokannasta poistetaan ainoastaan kyseiseen ruokalajiin
        ja käyttäjään liitetty relaatio ja varsinainen ruokalajin nimi jää yhä tietokantaan, sillä
        samanniminen ruokalaji voi olla myös jollain toisella käyttäjällä.

        Args:
            meal: poistettavan ruokalajin ilmentymä.
            user: ruokalajiin liitetyn käyttäjän ilmentymä.

        Returns:
            Palauttaa viimeisimmän muokatun rivin id-numeron.
        """

        query = "DELETE FROM meal_relations WHERE userID = ? AND mealID = ?"

        return self.i_o.write(query, [user.id, meal.db_id])

    def empty_tables(self):
        """Tyhjentää kaikki luokan käyttämät tietokantataulut."""

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
