from datetime import datetime
from pathlib import Path
from entities.meal import Meal
from config import DEFAULT_SET_FILE_PATH

class LibraryRepository:
    """Luokka, joka lukee CSV-muotoiset ruokalajien vakiokirjastot, sekä tulostaa kauppalistan.

    Luokka lukee joko .enviin määritellystä tai parametrina annetusta csv-tiedostosta käyttäjän
    vakiokirjastoon ruokalajit, sekä kirjoittaa parametrina saadun kauppalistan .envissa
    määriteltyyn hakemistoon .txt-tiedostoon.
    """

    def read_meals(self, csv_file=False):
        """Lukee määritellyn CSV-tiedoston.

        Parametrina annettava tiedosto täytyy olla jo valmiiksi _io.TextIOWrapper-luokan muodossa,
        eli käytännössä open()-metodi suoritettuna. CSV-tiedoston sisältö on oltava
        muodossa ruokalaji;raaka-aine. Näistä luodaan ruokalaji- ja raaka-aineilmentymiä, jotka
        palautetaan listana.

        Args:
            csv_file: oletuksena False jolloin luetaan .envissa määritellystä tiedostosta, tai
            sitten parametrina annetaan _io.TextIOWrapper-objekti.

        Returns:
            Palauttaa listallisen Meal-objekteja raaka-aineineen.
        """

        path = csv_file if csv_file else open(DEFAULT_SET_FILE_PATH, "r")
        meals = []

        with path as file:
            new_meal = None
            ingredients = []

            for row in file:

                row = row.replace('\n', '')
                parts = row.split(';')

                meal = parts[0]
                ingredient = parts[1]

                if not new_meal:
                    new_meal = meal

                if meal in new_meal:
                    ingredients.append(ingredient)
                else:
                    meals.append(Meal(new_meal, ingredients.copy()))
                    ingredients.clear()
                    new_meal = meal
                    ingredients.append(ingredient)

            meals.append(Meal(new_meal, ingredients))

        return meals

    def write_wishlist(self, items, directory):
        """Kirjoittaa kauppalistan tekstitiedostoon.

        Kirjoittaa parametrina annetun kauppalistan tekstitiedostoon, jonka nimi muodostuu
        merkkijonosta "kauppalista" sekä kirjoitushetken aikaleimasta, joka on
        muotoa päivä, kuukausi, tunti, minuutti sekä sekunnit. Ensin luodaan tiedosto
        ja sitten kirjoitetaan raaka-aineet perään.

        Args:
            items: kauppalistan raaka-aineet.

        Returns:
            Palauttaa kirjoitetun tiedoston nimen.
        """

        timestamp = datetime.now().strftime("%d_%m_%H%M%S")
        file_name = "/kauppalista"+timestamp+".txt"
        file_path = Path(directory+file_name)

        try:
            file_path.touch()

            with file_path.open(mode = "w") as file:
                for item in items:
                    file.write(f"{item}"+"\n")

            return directory+file_name

        except IOError as error:
            return error
