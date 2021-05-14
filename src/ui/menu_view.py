"""UI-moduuli, joka tarjoaa sovelluksen ruokalistanäkymän."""

from tkinter import StringVar, Frame, constants, LabelFrame, Label

class MenuView:
    """Luokka ruokalistanäkymälle.

    Tässä luokassa koostetaan generoitu ruokalista paikoilleen näkymään. Näkymä voidaan liittää
    helposti osaksi muita näkymiä sen ollessa oma itsenäinen kokonaisuutensa.
    """

    def __init__(self, root, controller):
        """Konstruktori, alustaa luokan attribuutit.

        Args:
            root: isäntäkehys, johon näkymän pääkehys kiinnitetään.
            controller: käytettävä controller-luokka.
        """

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
        """Pakkaa pääkehyksen."""

        self._frame.pack()

    def destroy(self):
        """Tuhoaa pääkehyksen."""

        self._frame.destroy()

    def _initialize(self):
        """Alustaa näkymän."""

        self._frame = Frame(self._root, padx = 30, pady = 30, bg = "#FFFFEA")

        self._view_menu()

        self._frame.pack()

    def _view_menu(self):
        """Rakentaa ruokalistanäkymän."""

        self._menu_frame = LabelFrame(
            self._frame, text = "Ruokalista", padx = 30, pady = 20, bg = "#FFFFEA")
        menu_items = self._generate_menu_view()

        if menu_items is None:
            msg = Label(self._menu_frame, text = "Generoi ruokalista ensin!", bg = "#FFFFEA")

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
        """Generoi ruokalistanäkymän sisällön näkymään.

        Metodi pyytää ruokalistan ilmentymän controllerilta ja asettelee ruokalajit
        paikoilleen näkymään.

        Returns:
            Palauttaa monikon listoja, joissa on tarvittavat Labelit ja Framet näkymän
            muodostamiseksi.
        """

        if not self.ctrl.fetch_menu():
            return None

        menu = self.ctrl.fetch_menu().meals

        day_frames = [Frame(self._menu_frame) for day in self.days]
        meal_frames = [Frame(self._menu_frame) for day in self.days]
        day_labels = []
        meal_labels = []

        for day, day_frame, meal_frame in zip(self.days, day_frames, meal_frames):
            day_label = Label(day_frame, text = day, bg = "#FFFFEA")
            meal_variable = StringVar()
            meal_label = Label(
                meal_frame,
                textvariable = meal_variable,
                padx = 10, pady = 10,
                justify = constants.CENTER,
                bg = "#FFFFEA")

            day_labels.append(day_label)
            meal_labels.append(meal_label)
            self.meal_variables.append(meal_variable)

        for var, meal in zip(self.meal_variables, menu):
            var.set((meal.name.replace(' ', '\n')))

        return (day_frames, meal_frames, day_labels, meal_labels)
