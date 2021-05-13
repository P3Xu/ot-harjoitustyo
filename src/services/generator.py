"""Generator-moduuli, jonka GeneratorService-luokka toimittaa generoidun ruokalistan."""

import random
from datetime import date
from entities.menu import Menu

class GeneratorService:
    """Luokka palvelulle, joka generoi viikon ruokalistan."""

    def __init__(self, repository, user):
        """Konstruktori, alustaa generaattorin.

        Args:
            repository: repository-luokka, joka hoitaa ruokalajien tietokantatoiminnot.
            user: käyttäjä, johon luotu ruokalista liitetään.
        """

        self.repository = repository
        self.user = user

    def generate(self):
        """Metodi, joka generoi ruokalistan.

        Vaatimaton generointi-algoritmi, joka arpoo ruokalajeista viikon ruokalistan
        satunnaiseen järjestykseen, ilman duplikaatteja.

        Tarvitsee vähintään seitsemän eri ruokalajia voidakseen generoida listan.

        Returns:
            Palauttaa -1 jos tietokannassa ei ole tarpeeksi ruokalajeja, tai onnistuessaan
            Menu-olion, joka sisältää listan ruokalajit Meal-olioina.
        """

        generated = []
        source = self.repository.find_all_meals(self.user)

        if len(source) < 7:
            return -1

        while len(generated) < 7:
            item = source[random.randint(0, len(source)-1)]

            if item not in generated:
                generated.append(item)

        random.shuffle(generated)

        return Menu(generated, date.today(), self.user)
