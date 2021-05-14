"""UI-moduuli, joka tarjoaa sovelluksen päänäkymän."""

from tkinter import Frame, Label, LabelFrame, Button
from ui.menu_view import MenuView

class MainView:
    """Luokka sovelluksen päänäkymälle.

    Päänäkymässä on käyttäjän viimeisin ruokalista, sekä tarvittavat painikkeet sovelluken
    käyttämistä varten. Päänäkymästä on mahdollista siirtyä hallitsemaan ruoka-aineita tai
    tulostamaan generoidun ruokalistan raaka-aineet sisältävää kauppalistaa. Lisäksi päänäkymästä
    voidaan kirjautua ulos tai lopettaa ohjelma.
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

        self._initialize()

    def pack(self):
        """Pakkaa pääkehyksen."""

        self._wrapper.pack()

    def destroy(self):
        """Tuhoaa pääkehyksen."""

        self._wrapper.destroy()

    def _initialize(self):
        """Alustaa näkymän.

        Kutsuu näkymän metodeja, jotka luovat näkymässä käytettävät komponentit. Lisäksi kutsuu
        toisesta moduulista näkymää ruokalistalle.
        """

        self._wrapper = Frame(self._root, padx = 20, pady = 20, bg = "#FFFFEA")
        border = Frame(self._wrapper, padx = 2, pady = 2, bg = "#000000")
        self._frame = Frame(border, padx = 50, pady = 40, bg = "#FFFFEA")

        self._header()
        self._variables = MenuView(self._frame, self._ctrl).meal_variables
        self._actions()

        self._frame.pack(expand=True)
        border.pack(expand=True)
        self._wrapper.pack(expand=True)

    def _generate_menu(self):
        """Hoitaa ruokalistan prosessoinnin painiketta painettaessa.

        Pyytää controlleria luomaan ruokalistan ja sen jälkeen tarkistaa, löytyykö sellaista.
        Mikäli ei löydy, ei tietokannassa ollut tarpeeksi ruokalajeja ja metodi siirtyy
        viestinäkymään informoimaan käyttäjää asiasta. Muussa tapauksessa lataa uudestaan
        päänäkymän, jossa näkyy nyt äsken generoitu ruokalista.
        """

        self._ctrl.generate_menu()
        check_status = self._ctrl.fetch_menu()

        if not check_status:
            msg = "Kirjastossa ei ole tarpeeksi ruokalajeja ruokalistan generoimiseen, lisää" + \
                " ruokalajeja kirjastoon."
            self._root.after(0, self._views[2](msg, 0))
        else:
            self._root.after(0, self._views[0])

    def _header(self):
        """Näkymän otsikon rakentava metodi.

        Otsikko rakennetaan kolmesta palasta, joista yksi on käyttäjän käyttäjätunnus.
        """

        header_frame = Frame(self._frame, pady = 30, bg = "#FFFFEA")

        header_text = f"Tervetuloa {self._views[8].user}!"
        header_label = Label(header_frame, text = header_text, bg = "#FFFFEA")
        header_label.configure(anchor = "center", font = "None 17")

        header_label.pack()
        header_frame.pack()

    def _actions(self):
        """Tässä metodissa luodaan sovelluksen käyttämistä varten tarvittavat painikkeet, joilla
        voidaan siirtyä muihin näkymiin valinnan mukaan. Painikkeet ohjaavat joko suoraan toisiin
        näkymiin, tai kutsuvat ensin luokan prosessoivia metodeja, jotka ohjaavat lopulta eteenpäin.
        """

        wrapper = Frame(self._frame, pady = 40, bg = "#FFFFEA")
        action_frame = LabelFrame(wrapper, text = "Toiminnot", padx = 30, pady = 30, bg = "#FFFFEA")

        generate_menu = Button(
            action_frame,
            text = "Generoi ruokalista",
            command = lambda: self._generate_menu(),
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")
        manage_items = Button(
            action_frame,
            text = "Hallitse ruokia ja aineksia",
            command = self._views[1],
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")
        logout = Button(
            action_frame,
            text = "Kirjaudu ulos",
            command = lambda: self._process_logout(),
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")
        end_session = Button(
            action_frame,
            text = "Lopeta",
            command = self._views[3],
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")
        wish_list = Button(
            action_frame,
            text = "Koosta kauppalista",
            command = lambda: self._process_wishlist(),
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")

        generate_menu.grid(row = 0, column = 0, padx = 12)
        wish_list.grid(row = 0, column = 1, padx = 12)
        manage_items.grid(row = 0, column = 2, padx = 12)
        logout.grid(row = 0, column = 3, padx = 12)
        end_session.grid(row = 0, column = 4, padx = 12)

        action_frame.pack()
        wrapper.pack()

    def _process_logout(self):
        """Prosessoi käyttäjän uloskirjautumisen."""

        self._ctrl.logout_user()

        self._root.after(0, self._views[4])

    def _process_wishlist(self):
        """Prosessoi kauppalistan tulostuksen."""

        menu_status = self._ctrl.fetch_menu()

        if not menu_status:
            self._root.after(0, self._views[2]("Generoi ruokalista ensin!", 0))
        else:
            self._root.after(0, self._views[7])
