from tkinter import ttk, StringVar, Button, Frame, Label, Entry
from tkinter.filedialog import askopenfile

class CreateUserView:
    def __init__(self, root, controller, views):
        self._root = root
        self._ctrl = controller
        self._views = views

        self._frame = None
        self._wrapper = None
        self._config_file = None
        self._username = StringVar()
        self._password = StringVar()

        self._initialize()

    def pack(self):
        self._wrapper.pack()

    def destroy(self):
        self._wrapper.destroy()

    def _initialize(self):
        self._wrapper = Frame(self._root, padx = 20, pady = 20, bg = "#FFFFEA")
        border = Frame(self._wrapper, padx = 2, pady = 2, bg = "#000000")
        self._frame = Frame(border, padx = 40, pady = 50, bg = "#FFFFEA")

        self._header()
        self._directions()
        self._create_user_view()
        self._actions()

        self._frame.pack(expand=True)
        border.pack(expand=True)
        self._wrapper.pack(expand=True)

    def _header(self):
        header_frame = Frame(self._frame, bg = "#FFFFEA")

        header_label = Label(header_frame, text = "Luo uusi käyttäjä", pady = 30, bg = "#FFFFEA")
        header_label.configure(anchor = "center", font = "None 14")

        header_label.pack()
        header_frame.pack()

    def _directions(self):
        parent_frame = ttk.Frame(self._frame)

        text = "Käyttäjätunnuksen ja salasanan pituus on oltava vähintään viisi merkkiä.\n\n" + \
            "Mikäli haluat määritellä oman vakiokokoelman ruokalajeille, voit ladata sen " + \
            "painamalla \"Lataa .csv\"-painiketta.\nMuussa tapauksessa sovellus käyttää omaa " + \
            "oletuskokoelmaa."
        dir_label = Label(parent_frame, text = text, pady = 20, bg= "#FFFFEA")

        dir_label.pack()
        parent_frame.pack()

    def _create_user_view(self):
        parent_frame = Frame(self._frame, pady = 10, bg = "#FFFFEA")

        username_label = Label(parent_frame, text = "Käyttäjänimi:", bg = "#FFFFEA")
        username_entry = Entry(
            parent_frame,
            width = 20,
            bg = "#FFFFFF",
            textvariable = self._username)
        username_entry.focus_set()

        password_label = Label(parent_frame, text = "Salasana:", bg = "#FFFFEA")
        password_entry = Entry(
            parent_frame, show = "*",
            width = 20, bg = "#FFFFFF",
            textvariable = self._password)
        password_entry.bind("<Return>", lambda x: self._process_add_user())

        submit = Button(
            parent_frame, text = "Luo käyttäjä",
            height = 2,
            command = lambda: self._process_add_user(),
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")
        add_config = Button(
            parent_frame,
            text = "Lataa\n.csv",
            height = 2,
            command = lambda: self._process_add_config(),
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")

        username_label.grid(row = 0, column = 0, pady = 2)
        username_entry.grid(row = 0, column = 1, padx = 2)
        password_label.grid(row = 1, column = 0)
        password_entry.grid(row = 1, column = 1, padx = 2)
        add_config.grid(row = 0, column = 2, rowspan = 2)
        submit.grid(row = 0, column = 3, rowspan = 2)

        parent_frame.pack()

    def _actions(self):
        action_frame = Frame(self._frame, padx = 20, pady = 40, bg = "#FFFFEA")

        back = Button(
            action_frame,
            text = "Takaisin",
            command = self._views[4],
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

    def _process_add_config(self):
        file_path = askopenfile(mode="r", filetypes=(("CSV Files", "*.csv"),))

        self._config_file = file_path

    def _process_add_user(self):
        if (len(self._username.get()) < 5 or
            len(self._password.get()) < 5 or
            self._username.get() == len(self._username.get()) * " "):

            self._root.after(
                0,
                self._views[2]
                ("Käyttäjätunnuksen ja salasanan tulee olla vähintään 5 merkkiä pitkä!", 5))
        else:
            add = self._ctrl.add_user(self._username.get(), self._password.get(), self._config_file)

            if isinstance(add, int):
                self._root.after(0, self._views[2]("Tunnuksen luonti onnistui!", 4))
            elif not add:
                self._root.after(0, self._views[2]("Tunnus on jo olemassa, valitse toinen.", 5))
