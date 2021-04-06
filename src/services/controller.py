from repositories import generator_repository
from services.generator import GeneratorService

class Controller:
    """Kontrolleri-luokka."""

    def __init__(self):
        self.gen_repository = generator_repository.GeneratorRepository()

    def generate_menu(self):
        menu = GeneratorService(self.gen_repository).generate()

        self.gen_repository.insert_menu(menu)

    def fetch_meals(self):
        return self.gen_repository.find_all_meals()

    def fetch_ingredients(self):
        return self.gen_repository.find_all_ingredients()

    def fetch_menu(self):
        menu = self.gen_repository.find_menu()

        if isinstance(menu, int):
            return ["Generoi ruokalista ensin!"]

        return self.gen_repository.find_menu().get_meals()
