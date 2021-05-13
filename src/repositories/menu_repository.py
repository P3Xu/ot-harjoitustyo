from entities.menu import Menu
from repositories.io import InputOutput as default_io

class MenuRepository:
    """Luokka, joka hoitaa kaikki ruokalistoihin liittyvän tietokantatoiminnallisuuden.

    Attributes:
        i_o: I/O-luokka, joka tarjoaa tietokannan luku- ja kirjoitustoiminnot.
    """

    def __init__(self, meal_repository, i_o=default_io()):
        """Konstruktori, alustaa attribuutin I/O-objektin sekä käytettävän
        ruokalajien tietokanta-attribuutin.

        Sovellus käyttää ruokalajien tietokantaa liittääkseen ruokalistan ilmentymään oikeat
        ruokalaji-ilmentymät raaka-aineineen.
        """

        self.i_o = i_o
        self.meal_repo = meal_repository

    def empty_menu_table(self):
        """Metodi koko menu-taulun tyhjentämiselle, käytetään lähinnä testaamisessa."""

        self.i_o.run_command("DELETE FROM menus")

    def insert_menu(self, menu):
        """Lisää generoidun ruokalistan tietokantaan.

        Saa parametrina Menu-objektin, josta puretaan tarvittavat arvot tietokantakomennon
        parametreiksi ja syötetään tietokantaan. Ennen lisäystä poistetaan mahdollinen
        olemassaoleva ruokalista, sillä tällä hetkellä käyttäjällä voi olla vain yksi
        ruokalista kerrallaan.

        Args:
            menu: ruokalistan ilmentymä.
        """

        user = menu.user
        values = [(meal.db_id, user.id, menu.date) for meal in menu.meals]

        self.initialize_menus(user)
        self.i_o.write("INSERT INTO menus (mealID, userID, date) VALUES (?, ?, ?)", values, False)

    def find_menu(self, user):
        """Etsii käyttäjään liitetyn ruokalistan.

        Tietokannasta etsitään annettuun käyttäjään liittyvä ruokalista, joka palautetaan
        mikäli sellainen löytyy. Jos löytyy, noudetaan ruokalajien-tietokannasta oikeat
        ruokalaji-ilmentymät, jotka liitetään ruokalista-ilmentymään.

        Args:
            user: käyttäjä-ilmentymä.

        Returns:
            Palauttaa ruokalistan löytyessä ruokalistan ilmentymän, tai muussa tapauksessa
            negatiivisen kokonaisluvun -1.
        """

        menu = self.i_o.read("SELECT * FROM menus WHERE userID = ?", [user.id])

        if len(menu) == 0:
            return -1

        date = menu[0]['date']
        meals = [self.meal_repo.find_single_meal(int(meal['mealID']), user) for meal in menu]

        return Menu(meals, date, user)

    def initialize_menus(self, user):
        """Alustaa käyttäjän ruokalistan tietokannasta uutta ruokalistaa varten."""

        self.i_o.write("DELETE FROM menus WHERE userID = ?", [user.id])
