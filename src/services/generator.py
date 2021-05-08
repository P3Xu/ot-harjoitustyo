"""
    Generator-moduuli, jonka GeneratorService-luokka huolehtii
    ruokalistan generoinnista.
"""
import random
from datetime import date
from entities.menu import Menu

class GeneratorService:
    """Luokka palvelulle, joka generoi listan."""

    def __init__(self, repository, user):
        """Luokan konstruktori. Luo kyseisen palvelun.

        Args:
            repository: saa parametrina Repository-olion,
            joka suorittaa tietokantatoiminnot.
        """
        self.repository = repository
        self.user = user

    def generate(self):
        """Vaatimaton generointi-algoritmi, joka arpoo ruokalajeista
           viikon ruokalistan satunnaisessa järjestyksessä.

        Returns:
            Palauttaa Menu-oliona viikon ruokalistan.
        """

        generated = []
        source = self.repository.find_all_meals(self.user)

        while len(generated) < 7:
            item = source[random.randint(0,len(source)-1)]

            if item not in generated:
                generated.append(item)

        random.shuffle(generated)

        return Menu(generated, date.today())
