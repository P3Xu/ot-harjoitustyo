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

            label_frames = []
            day_labels = []
            meal_labels = []

            for day in self.days:
                label_frame = ttk.LabelFrame(menu_frame)
                day_label = ttk.Label(label_frame, text = day)
                meal_variable = StringVar()
                meal_label = ttk.Label(label_frame, textvariable = meal_variable)

                label_frames.append(label_frame)
                day_labels.append(day_label)
                self.meal_variables.append(meal_variable)
                meal_labels.append(meal_label)

            for (var, meal) in zip(self.meal_variables, menu):
                var.set(meal.name)

            menu_frame.grid(row = 0, column = 0)

            for i, (frame, day, meal) in enumerate(zip(label_frames, day_labels, meal_labels)):
                frame.grid(row = 1, column = i)
                day.grid(row = 2, column = i)
                meal.grid(row = 3, column = i)
