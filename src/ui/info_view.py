"""UI-moduuli, joka tarjoaa mahdollisuuden tulostaa viestejä käyttäjälle."""

from tkinter import Frame, Label, constants
from config import MESSAGE_SHOWTIME

class InfoView:
    """Luokka näkymälle, jolla viestitään käyttäjälle.

    Luokalle annetaan parametrien joukossa näytettävä viesti sekä näkymän numero, johon halutaan
    viestin näyttämisen jälkeen siirtyä. Viestin näkymisen kesto määritellään sovelluksen
    konfiguraatiossa.
    """

    def __init__(self, root, controller, views, message, view_number):
        """Konstruktori, alustaa luokan attribuutit.

        Args:
            root: isäntäkehys, johon näkymän pääkehys kiinnitetään.
            controller: käytettävä controller-luokka.
            views: lista muista sovelluksen näkymistä, joihin voi siirtyä kutsumalla halutun
            näkymän numeroa listalta.
        """

        self._root = root
        self._ctrl = controller
        self._views = views
        self._msg = message
        self._view_number = view_number
        self._frame = None

        self._initialize()

    def pack(self):
        """Pakkaa pääkehyksen"""

        self._frame.pack()

    def destroy(self):
        """Tuhoaa pääkehyksen"""

        self._frame.destroy()

    def _initialize(self):
        """Alustaa näkymän."""

        self._frame = Frame(self._root, padx = 50, pady = 40, bg = "#FFFFEA")

        self._show_information()
        self._frame.pack()

        self._root.after(MESSAGE_SHOWTIME, self._views[self._view_number])

    def _show_information(self):
        """Rakentaa labelin, johon käyttäjälle tulostettava viesti pakataan."""

        parent_frame = Frame(self._frame, padx = 20, pady = 20, bg = "#FFFFEA")

        status_label = Label(
            parent_frame,
            text = self._msg,
            padx = 10, pady = 10,
            justify = constants.CENTER,
            bg = "#FFFFEA")

        status_label.pack()
        parent_frame.pack()
