from tkinter import ttk, StringVar, Frame, constants

class MenuView:
    def __init__(self, root, controller):
        self._root = root
        self.ctrl = controller

        self._frame = None
        self._menu_frame = None
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
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(self._root, padx = 30, pady = 10)

        self._view_menu()

        self._frame.pack()

    def _view_menu(self):
        self._menu_frame = ttk.LabelFrame(self._frame, text = "Ruokalista", padding = 10)
        menu_items = self._generate_menu_view()

        if menu_items is None:
            msg = ttk.Label(self._menu_frame, text = "Generoi ruokalista ensin!")

            msg.pack()

        else:
            (day_frames, meal_frames, day_labels, meal_labels) = menu_items

            for i, (day_frame, meal_frame, day, meal) in enumerate(
                zip(day_frames, meal_frames, day_labels, meal_labels)):

                day_frame.grid(row = 0, column = i, padx = 5)
                day.grid(row = 0, column = i)
                meal_frame.grid(row = 1, column = i, padx = 5)
                meal.grid(row = 1, column = i)

        self._menu_frame.pack()

    def _generate_menu_view(self):
        if not self.ctrl.fetch_menu():
            return None

        menu = self.ctrl.fetch_menu().meals

        day_frames = [Frame(self._menu_frame) for day in self.days]
        meal_frames = [Frame(self._menu_frame) for day in self.days]
        day_labels = []
        meal_labels = []

        for day, day_frame, meal_frame in zip(self.days, day_frames, meal_frames):
            day_label = ttk.Label(day_frame, text = day)
            meal_variable = StringVar()
            meal_label = ttk.Label(meal_frame, textvariable = meal_variable, padding = 10, justify = constants.CENTER)

            day_labels.append(day_label)
            meal_labels.append(meal_label)
            self.meal_variables.append(meal_variable)

        for var, meal in zip(self.meal_variables, menu):
            var.set((meal.name.replace(' ', '\n')))

        return (day_frames, meal_frames, day_labels, meal_labels)
