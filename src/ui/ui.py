"""
    Alkuun deadlineja/testailua varten nopeasti tehty tekstipohjainen käyttis,
    joka korvataan myöhemmin graafisella ja koodataan siis täysin uusiksi.
"""

from services import controller

COMMANDS = {
    0: "0: Lopeta",
    1: "1: Generoi ruokalista",
    2: "2: Näytä ruokalista",
    3: "3: Näytä ruokalajit",
    4: "4: Näytä ruoka-aineet",
    5: "5: Lisää ruokalaji",
}

DAYS = {
    0: "Maanantai:",
    1: "Tiistai:",
    2: "Keskiviikko:",
    3: "Torstai:",
    4: "Perjantai:",
    5: "Lauantai:",
    6: "Sunnuntai:"
}

class UI:
    """Käyttöliittymäluokka"""

    def __init__(self):
        self.items = None
        self.ctrl = controller.Controller()

    def start(self):
        print("\nTervetuloa!")

        while True:
            print()
            for value in COMMANDS.values():
                print(value)

            command = input("\nValitse komento: ")
            print()

            if command == "0":
                print("Näkemiin!\n")
                break

            elif command == "1":
                self.ctrl.generate_menu()

                print("Ruokalista generoitu!")

            elif command == "2":
                menu = self.ctrl.fetch_menu()

                if len(menu) == 1:
                    print(menu[0])
                else:
                    for i, day in DAYS.items():
                        print(f"{day: <13}{menu[i]}")

            elif command == "3":
                meals = self.ctrl.fetch_meals()

                for meal in meals:
                    print(meal)

            elif command == "4":
                ingredients = self.ctrl.fetch_ingredients()

                for ingredient in ingredients:
                    print(ingredient)

            elif command == "5":
                ingredients = []
                meal_name = input("Syötä ruokalajin nimi: ")
                first_ingredient = input("\nSyötä vähintään yhden raaka-aineen nimi: ")

                ingredients.append(first_ingredient)

                while True:
                    ask_more = str(input("\nOnko raaka-aineita enemmän, K/E? "))

                    if ask_more in ('K', 'k'):
                        ingredient = input("\nSyötä raaka-aineen nimi: ")
                        ingredients.append(ingredient)
                    else:
                        if self.ctrl.add_meal(meal_name, ingredients) == 0:
                            print("\nRuokalaji lisätty onnistuneesti kirjastoon!")
                            break
                        else:
                            print("\nRuokalaji löytyy jo kirjastosta.")
                            break

            else:
                print("Virheellinen komento, valitse uudestaan:")
