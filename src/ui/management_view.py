from tkinter import ttk, StringVar, Listbox, Scrollbar, Button, Frame
from tkinter import constants
from ui.menu_view import MenuView

class ManagementView:
    def __init__(self, root, controller, views):
        self._root = root
        self._frame = None
        self._variables = None
        self._ctrl = controller
        self._views = views

        self._initialize()

    def pack(self):
        self._frame.pack() #fill?

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(self._root)

        self._variables = MenuView(self._frame, self._ctrl).meal_variables
        self._items_view()

        self._frame.pack()
        ### AAKKOSJÄRKKÄ RIKKOI TESTIT, TEE NIILLE JOTAIN

    def _items_view(self):
        items_frame = Frame(self._frame)
        meals_frame = Frame(items_frame)
        ingredients_frame = Frame(items_frame)

        #meals_box = Listbox(meals_frame)
        meals_box = self._generate_box(meals_frame)
        meals_scrollbar = Scrollbar(meals_frame)
        meals_box.config(yscrollcommand = meals_scrollbar.set)
        meals_scrollbar.config(command = meals_box.yview)

        ingredients_box = Listbox(ingredients_frame)
        ingredients_scrollbar = Scrollbar(ingredients_frame)
        ingredients_box.config(yscrollcommand = ingredients_scrollbar.set)
        ingredients_scrollbar.config(command = ingredients_box.yview)

        meals = self._ctrl.fetch_meals()
        ingredients = self._ctrl.fetch_ingredients()

        """for i, meal in enumerate(meals):
            meals_box.insert(i, meal.name)"""
        for i, ingredient in enumerate(ingredients):
            ingredients_box.insert(i, ingredient.name)

        meals_box.pack(side = constants.LEFT)
        meals_scrollbar.pack(side = constants.RIGHT, fill = constants.Y)
        meals_frame.pack(side = constants.LEFT)

        ingredients_box.pack(side = constants.LEFT)
        ingredients_scrollbar.pack(side = constants.RIGHT, fill = constants.Y)
        ingredients_frame.pack(side = constants.RIGHT)

        items_frame.pack()

    def _generate_box(self, parent, which=False):
        box = Listbox(parent)

        meals = self._ctrl.fetch_meals()

        for i, meal in enumerate(meals):
            box.insert(i, meal.name)

        box_scrollbar = Scrollbar(parent)
        box.config(yscrollcommand = box_scrollbar.set)
        box_scrollbar.config(command = box.yview)


        return box
