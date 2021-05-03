from tkinter import ttk, StringVar, Listbox, Scrollbar, Button, Frame, Label, Entry, Text, constants

class LoginView:
    def __init__(self, root, controller, views):
        self._root = root
        self._ctrl = controller
        self._views = views

        self._frame = None

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
        username_entry = Entry(parent_frame, width = 20, bg = "#FFFFFF")
        password_label = Label(parent_frame, text = "Salasana:", justify = constants.LEFT)
        password_entry = Entry(parent_frame, show = "*", width = 20, bg = "#FFFFFF")
        submit = Button(parent_frame, text = "Kirjaudu sisään", height = 2)

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

class CreateUserView:
    def __init__(self, root, controller, views):
        self._root = root
        self._ctrl = controller
        self._views = views

        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(self._root, padx = 50, pady = 20)

        self._header()
        self._create_user_view()
        self._actions()

        self._frame.pack()

    def _header(self):
        header_frame = ttk.Frame(self._frame)

        header_label = Label(header_frame, text = "Luo uusi käyttäjä", pady = 30)
        header_label.configure(anchor = "center", font = "None 12")

        header_label.pack()
        header_frame.pack()

    def _create_user_view(self):
        parent_frame = Frame(self._frame)

        username_label = Label(parent_frame, text = "Käyttäjänimi:")
        username_entry = Entry(parent_frame, width = 20, bg = "#FFFFFF")
        password_label = Label(parent_frame, text = "Salasana:")
        password_entry = Entry(parent_frame, show = "*", width = 20, bg = "#FFFFFF")
        submit = Button(parent_frame, text = "Luo käyttäjä", height = 2)

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
            command = self._views[0]
        )
        end_session = ttk.Button(
            action_frame,
            text = "Lopeta",
            command = self._views[3]
        )

        back.grid(row = 0, column = 0, padx = 15, pady = 5)
        end_session.grid(row = 0, column = 1, padx = 15, pady = 5)

        action_frame.pack()
