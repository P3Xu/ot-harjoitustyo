"""UI-moduuli, joka tarjoaa käyttäjän sisäänkirjautumiseen tarkoitetun näkymän."""

from tkinter import StringVar, Button, Frame, Label, Entry, constants

class LoginView:
    """Luokka näkymälle käyttäjän sisäänkirjautumista varten.

    Luokka tarjoaa käyttäjälle näkymän, jossa on kentät käyttäjätunnukselle ja salasanalle, sekä
    painikkeet joilla on mahdollista kirjautua sisään, siirtyä luomaan uutta käyttäjää tai lopettaa
    ohjelma.
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
        self._ctrl = controller
        self._views = views

        self._frame = None
        self._wrapper = None
        self._username = StringVar()
        self._password = StringVar()

        self._initialize()

    def pack(self):
        """Pakkaa pääkehyksen."""

        self._wrapper.pack()

    def destroy(self):
        """Tuhoaa pääkehyksen."""

        self._wrapper.destroy()

    def _initialize(self):
        """Alustaa näkymän.

        Kutsuu näkymän metodeja, jotka luovat näkymässä käytetyt komponentit.
        """

        self._wrapper = Frame(self._root, padx = 20, pady = 20, bg = "#FFFFEA")
        border = Frame(self._wrapper, padx = 2, pady = 2, bg = "#000000")
        self._frame = Frame(border, padx = 50, pady = 20, bg = "#FFFFEA")

        self._header()
        self._create_login_view()
        self._actions()

        self._frame.pack(expand=True)
        border.pack(expand=True)
        self._wrapper.pack(expand=True)

    def _header(self):
        """Näkymän otsikon rakentava metodi."""

        header_frame = Frame(self._frame, bg = "#FFFFEA")

        header_label = Label(
            header_frame, text = "Ruokalistageneraattori 1.0", pady = 40, bg = "#FFFFEA")
        header_label.configure(anchor = "center", font = "None 15")

        header_label.pack()
        header_frame.pack()

    def _create_login_view(self):
        """Sisäänkirjautumisen kentät ja painikkeen rakentava metodi."""

        parent_frame = Frame(self._frame, bg = "#FFFFEA")

        username_label = Label(parent_frame, text = "Käyttäjänimi:", bg = "#FFFFEA")
        username_entry = Entry(
            parent_frame, width = 20, bg = "#FFFFFF", textvariable = self._username)
        username_entry.focus_set()

        password_label = Label(
            parent_frame, text = "Salasana:", justify = constants.LEFT, bg = "#FFFFEA")
        password_entry = Entry(
            parent_frame, show = "*", width = 20, bg = "#FFFFFF", textvariable = self._password)
        password_entry.bind("<Return>", lambda x: self._process_login())

        submit = Button(parent_frame,
            text = "Kirjaudu sisään",
            height = 2,
            command = lambda: self._process_login(),
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")

        username_label.grid(row = 0, column = 0, pady = 2   )
        username_entry.grid(row = 0, column = 1, padx = 2)
        password_label.grid(row = 1, column = 0)
        password_entry.grid(row = 1, column = 1, padx = 2)
        submit.grid(row = 0, column = 2, rowspan = 2)
        parent_frame.pack()

    def _actions(self):
        """Muihin näkymiin siirtymiseen tarvittavat painikkeet luova metodi."""

        action_frame = Frame(self._frame, padx = 20, pady = 40, bg = "#FFFFEA")

        back = Button(
            action_frame,
            text = "Luo uusi käyttäjä",
            command = self._views[5],
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")
        end_session = Button(
            action_frame,
            text = "Lopeta",
            command = self._views[3],
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")

        back.grid(row = 0, column = 0, padx = 15, pady = 5)
        end_session.grid(row = 0, column = 1, padx = 15, pady = 5)

        action_frame.pack()

    def _process_login(self):
        """Prosessoi kirjautumisen.

        Metodi tarkistaa, että käyttäjätunnus ja salasana täyttää vaaditut kriteerit ja tulostaa
        virhetilanteissa käyttäjää informoivan viestin tilanteesta. Kirjautumisen onnistuessa
        siirrytään seuraavaan näkymään.
        """

        uname = self._username.get()
        pword = self._password.get()

        if (len(uname) < 5 or len(pword) < 5):
            self._root.after(
                0,
                self._views[2]
                ("Tarkista käyttäjätunnus ja salasana.", 4))
        else:
            status = self._ctrl.login_user(uname, pword)

            if isinstance(status, int):
                self._views[8].user = uname
                self._root.after(0, self._views[0])
            elif not status:
                self._root.after(0, self._views[2]("Virheellinen käyttäjätunnus tai salasana.", 4))
