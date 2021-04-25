from tkinter import ttk, StringVar, Listbox, Scrollbar, Button, Frame, Label
from tkinter import LEFT, RIGHT, BOTH, BOTTOM, TOP, X, Y

class MenuView:
    def __init__(self, root, controller):
        self._root = root
        self._frame = None
        self.menu_frame = None
        self.ctrl = controller
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

        self._initialize()

    def pack(self):
        self._frame.pack() #fill?

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(self._root)

        self._view_menu()

        self._frame.pack()

    def _view_menu(self):
        self.menu_frame = ttk.LabelFrame(self._frame, text = "Ruokalista", padding = 10)
        menu_frame = self.menu_frame
        menu_items = self._generate_menu_view()

        if menu_items is None:
            msg = ttk.Label(menu_frame, text = "Generoi ruokalista ensin!")

            msg.pack()

        else:
            (label_frames, day_labels, meal_labels) = menu_items

            for i, (frame, day, meal) in enumerate(zip(label_frames, day_labels, meal_labels)):
                frame.grid(row = 0, column = i, padx = 5, pady = 5)
                day.grid(row = 0, column = i, padx = 5, pady = 5)
                meal.grid(row = 1, column = i, padx = 5, pady = 5)

        menu_frame.pack()

    def _generate_menu_view(self):
        menu = self.ctrl.fetch_menu()

        if menu is None:
            return None

        label_frames = [Frame(self.menu_frame) for day in self.days]
        day_labels = []
        meal_labels = []

        for day, frame in zip(self.days, label_frames):
            day_label = ttk.Label(frame, text = day)
            meal_variable = StringVar()
            meal_label = ttk.Label(frame, textvariable = meal_variable, padding = 10)

            day_labels.append(day_label)
            meal_labels.append(meal_label)
            self.meal_variables.append(meal_variable)

        for var, meal in zip(self.meal_variables, menu):
            var.set(meal.name)

        return (label_frames, day_labels, meal_labels)
