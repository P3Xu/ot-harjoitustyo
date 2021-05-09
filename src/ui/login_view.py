from tkinter import ttk, StringVar, Listbox, Scrollbar, Button, Frame, Label, Entry, Text, constants
from entities.user import User

class LoginView:
    def __init__(self, root, controller, views):
        self._root = root
        self._ctrl = controller
        self._views = views

        self._frame = None
        self._username = StringVar()
        self._password = StringVar()

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(self._root, padx = 50, pady = 20)

        self._header()
        self._create_login_view()
        self._actions()

        self._frame.pack()

    def _header(self):
        header_frame = ttk.Frame(self._frame)

        header_label = Label(header_frame, text = "Tervetuloa!", pady = 30)
        header_label.configure(anchor = "center", font = "None 17")

        header_label.pack()
        header_frame.pack()

    def _create_login_view(self):
        parent_frame = ttk.Frame(self._frame)

        username_label = Label(parent_frame, text = "Käyttäjänimi:")
        username_entry = Entry(parent_frame, width = 20, bg = "#FFFFFF", textvariable = self._username)
        username_entry.focus_set()

        password_label = Label(parent_frame, text = "Salasana:", justify = constants.LEFT)
        password_entry = Entry(parent_frame, show = "*", width = 20, bg = "#FFFFFF", textvariable = self._password)
        password_entry.bind("<Return>", lambda x: self._process_login())
        
        submit = Button(parent_frame, text = "Kirjaudu sisään", height = 2, command = lambda: self._process_login())

        username_label.grid(row = 0, column = 0, pady = 2   )
        username_entry.grid(row = 0, column = 1, padx = 2)
        password_label.grid(row = 1, column = 0)
        password_entry.grid(row = 1, column = 1, padx = 2)
        submit.grid(row = 0, column = 2, rowspan = 2)
        parent_frame.pack()

    def _actions(self):
        action_frame = Frame(self._frame, padx = 20, pady = 40)

        back = ttk.Button(
            action_frame,
            text = "Luo uusi käyttäjä",
            command = self._views[5]
        )
        end_session = ttk.Button(
            action_frame,
            text = "Lopeta",
            command = self._views[3]
        )

        back.grid(row = 0, column = 0, padx = 15, pady = 5)
        end_session.grid(row = 0, column = 1, padx = 15, pady = 5)

        action_frame.pack()

    def _process_login(self):
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
                self._root.after(0, self._views[0])
            elif not status:
                self._root.after(0, self._views[2]("Virheellinen käyttäjätunnus tai salasana.", 4))

class CreateUserView:
    def __init__(self, root, controller, views):
        self._root = root
        self._ctrl = controller
        self._views = views

        self._frame = None
        self._username = StringVar()
        self._password = StringVar()
        self._config_file = StringVar()

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(self._root, padx = 50, pady = 20)

        self._header()
        self._directions()
        self._create_user_view()
        self._config_set()
        self._actions()

        self._frame.pack()

    def _header(self):
        header_frame = ttk.Frame(self._frame)

        header_label = Label(header_frame, text = "Luo uusi käyttäjä", pady = 30)
        header_label.configure(anchor = "center", font = "None 14")

        header_label.pack()
        header_frame.pack()

    def _directions(self):
        parent_frame = ttk.Frame(self._frame)

        text = "Käyttäjätunnuksen ja salasanan pituus on oltava vähintään viisi merkkiä."
        dir_label = Label(parent_frame, text = text, pady = 20)

        dir_label.pack()
        parent_frame.pack()

    def _create_user_view(self):
        parent_frame = Frame(self._frame)

        username_label = Label(parent_frame, text = "Käyttäjänimi:")
        username_entry = Entry(parent_frame, width = 20, bg = "#FFFFFF", textvariable = self._username)
        username_entry.focus_set()
        
        password_label = Label(parent_frame, text = "Salasana:")
        password_entry = Entry(parent_frame, show = "*", width = 20, bg = "#FFFFFF", textvariable = self._password)
        password_entry.bind("<Return>", lambda x: self._process_add_user())
        submit = Button(parent_frame, text = "Luo käyttäjä", height = 2, command = lambda: self._process_add_user())

        username_label.grid(row = 0, column = 0, pady = 2   )
        username_entry.grid(row = 0, column = 1, padx = 2)
        password_label.grid(row = 1, column = 0)
        password_entry.grid(row = 1, column = 1, padx = 2)
        submit.grid(row = 0, column = 2, rowspan = 2)
        parent_frame.pack()

    def _actions(self):
        action_frame = Frame(self._frame, padx = 20, pady = 40)

        back = ttk.Button(
            action_frame,
            text = "Takaisin",
            command = self._views[4]
        )
        end_session = ttk.Button(
            action_frame,
            text = "Lopeta",
            command = self._views[3]
        )

        back.grid(row = 0, column = 0, padx = 15, pady = 5)
        end_session.grid(row = 0, column = 1, padx = 15, pady = 5)

        action_frame.pack()

    def _config_set(self):
        parent_frame = ttk.Frame(self._frame)

        text = "Mikäli olet määritellyt oman ruokalajikokoelman, syötä tiedoston nimi:"
        conf_label = Label(parent_frame, text = text, pady = 20, justify = constants.CENTER)
        conf_entry = Entry(parent_frame, width = 20, bg = "#FFFFFF", textvariable = self._config_file)

        conf_label.pack()
        conf_entry.pack()
        parent_frame.pack()

    def _process_add_user(self):
        if (len(self._username.get()) < 5 or
            len(self._password.get()) < 5 or
            self._username.get() == len(self._username.get()) * " "):

            self._root.after(
                0,
                self._views[2]
                ("Käyttäjätunnuksen ja salasanan tulee olla vähintään 5 merkkiä pitkä!", 5))
        else:
            status = self._ctrl.add_user(self._username.get(), self._password.get())

            if isinstance(status, int):
                self._root.after(0, self._views[2]("Tunnuksen luonti onnistui!", 4))
            if not status:
                self._root.after(0, self._views[2]("Tunnus on jo olemassa, valitse toinen.", 5))
