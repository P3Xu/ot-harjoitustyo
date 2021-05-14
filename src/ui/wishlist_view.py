"""UI-moduuli, joka tarjoaa näkymän ruokalistan raaka-aineiden kauppalistalle."""

from tkinter import Frame, Label, Listbox, Scrollbar, Button, constants, LabelFrame
from ui.menu_view import MenuView

class WishlistView:
    """Luokka kauppalistanäkymälle.

    Tässä luokassa luodaan näkymä kauppalistanäkymälle, jossa näkyy viikon ruokalista, sekä
    ruokalistaan liittyvät raaka-aineet aakkosjärjestyksessä. Näkymässä on mahdollisuus tallentaa
    kauppalista tekstitiedostoon.
    """

    def __init__(self, root, controller, views):
        """Konstruktori, alustaa luokan attribuutit.

        Args:
            root: isäntäkehys, johon näkymän pääkehys kiinnitetään.
            controller: käytettävä controller-luokka.
            views: lista muista sovelluksen näkymistä, joihin voi siirtyä kutsumalla halutun
                näkymän numeroa listalta.
        """

        self._root = root
        self._views = views
        self._ctrl = controller

        self._frame = None
        self._wrapper = None
        self._variables = None
        self._wishlist = None

        self._initialize()

    def pack(self):
        """Pakkaa pääkehyksen."""

        self._wrapper.pack()

    def destroy(self):
        """Tuhoaa pääkehyksen."""

        self._wrapper.destroy()

    def _initialize(self):
        """Alustaa näkymän."""

        self._wrapper = Frame(self._root, padx = 20, pady = 20, bg = "#FFFFEA")
        border = Frame(self._wrapper, padx = 2, pady = 2, bg = "#000000")
        self._frame = Frame(border, padx = 40, pady = 50, bg = "#FFFFEA")

        self._variables = MenuView(self._frame, self._ctrl).meal_variables
        self._generate_wishlist()
        self._actions()

        self._frame.pack(expand=True)
        border.pack(expand=True)
        self._wrapper.pack(expand=True)

    def _generate_wishlist(self):
        """Luo näkymän kauppalista-osuuden.

        Metodi lisää näkymään listauskentän ja painikkeen listan tallentamiseksi.
        Kentän sisältö pyydetään toiselta metodilta.
        """

        parent_frame = LabelFrame(
            self._frame, text = "Kauppalista", padx = 150, pady = 30, bg = "#FFFFEA")
        wrapper = Frame(parent_frame, pady = 10, bg = "#FFFFEA")
        button_wrapper = Frame(parent_frame, pady = 20, bg = "#FFFFEA")

        item_label = Label(wrapper, text = "Ruokalistan raaka-aineet:", pady = 2, bg = "#FFFFEA")
        item_scroll = Scrollbar(wrapper, bg = "#FFFFEA")

        item_box = self._get_listbox(wrapper)
        save_button = Button(
            button_wrapper,
            text = "Tallenna kauppalista\ntiedostoon",
            command = lambda: self._process_save(),
            pady = 5,
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")

        item_box.config(yscrollcommand = item_scroll.set)
        item_scroll.config(command = item_box.yview)

        item_label.pack()

        item_box.pack(side = constants.LEFT)
        item_scroll.pack(side = constants.RIGHT, fill = constants.Y)

        save_button.pack()

        wrapper.pack()
        button_wrapper.pack()
        parent_frame.pack()

    def _get_listbox(self, parent):
        """Luo listauskentän ruokalistan raaka-aineille.

        Kenttään pyydetään controllerilta ruokalista, jonka ruokalajien raaka-aineiden nimet
        iteroidaan läpi ja lisätään settiin duplikaattien välttämiseksi. Tämän jälkeen setti
        käännetään listaksi ja järjestetään aakkosjärjestykseen, jonka jälkeen se syötetään
        kentän arvoiksi.

        Args:
            parent: isäntäkehys, johon kenttä sidotaan.

        Returns:
            Palauttaa valmiin listauskentän näkymään sijoitettavaksi.
        """

        menu = self._ctrl.fetch_menu()
        items = set()

        item_box = Listbox(parent, bg = "#FFFFFF")

        for meal in menu.meals:
            for ingredient in meal.ingredients:
                items.add(ingredient.name)

        items = list(items)
        items.sort()
        self._wishlist = items

        for i, item in enumerate(items):
            item_box.insert(i, item)

        return item_box

    def _actions(self):
        """Luo painikkeet muihin näkymiin siirtymiseksi."""

        wrapper = Frame(self._frame, pady = 30, bg = "#FFFFEA")
        action_frame = LabelFrame(wrapper, text = "Toiminnot", padx = 20, pady = 20, bg = "#FFFFEA")

        back = Button(
            action_frame,
            text = "Palaa takaisin",
            command = self._views[0],
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")
        end_session = Button(
            action_frame,
            text = "Lopeta",
            command = self._views[3],
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")
        logout = Button(
            action_frame,
            text = "Kirjaudu ulos",
            command = lambda: self._process_logout(),
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")

        back.grid(row = 0, column = 0, padx = 15)
        logout.grid(row = 0, column = 1, padx = 15)
        end_session.grid(row = 0, column = 2, padx = 15)

        action_frame.pack()
        wrapper.pack()

    def _process_save(self):
        """Prosessoi tallennuspyynnön.

        Tulostaa käyttäjälle tiedoston nimen, johon kauppalista tallennettiin.
        """

        file_name = self._ctrl.export_wishlist(self._wishlist)
        msg = "Kauppalista tallennettiin onnistuneesti tiedostoon "+file_name[1:]

        self._root.after(0, self._views[2](msg, 7))

    def _process_logout(self):
        """Prosessoi käyttäjän uloskirjautumisen."""

        self._ctrl.logout_user()

        self._root.after(0, self._views[4])
