from tkinter import ttk, StringVar
from services.controller import Controller

class MainUI:
    def __init__(self, root):
        self._root = root
        self.ctrl = Controller()
        self.meal_variables = []
        self.days = [
            "Maanantai:",
            "Tiistai:",
            "Keskiviikko:",
            "Torstai:",
            "Perjantai:",
            "Lauantai:",
            "Sunnuntai:"
        ]

    def start(self):
        self._menu()

    def _menu(self):
        menu = self.ctrl.fetch_menu()
        #f = tkinter.Frame(relief='flat')

        menu_frame = ttk.LabelFrame(
            self._root,
            text = "Ruokalista"
        )

        if len(menu) == 1:
            msg = ttk.Label(menu_frame, text = menu[0])

            menu_frame.grid(row = 0, column = 0)
            msg.grid(row = 1, column = 0)
        else:
            #frames = [ttk.LabelFrame(menu, labelwidget = f) for i in range(len(self.days))]

            frames = [ttk.LabelFrame(menu_frame) for i in range(len(self.days))]
            days = [ttk.Label(frames[i], text = self.days[i]) for i in range(len(frames))]

            self.meal_variables = [StringVar() for i in range(len(days))]

            meals = [
                ttk.Label(frames[i],
                textvariable = self.meal_variables[i]) for i in range(len(frames))
            ]

            for (var, meal) in zip(self.meal_variables, menu):
                var.set(meal.name)

            menu_frame.grid(row = 0, column = 0)

            for i, (frame, day, meal) in enumerate(zip(frames, days, meals)):
                frame.grid(row = 1, column = i)
                day.grid(row = 2, column = i)
                meal.grid(row = 3, column = i)
