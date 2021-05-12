from tkinter import ttk, Frame, Label
from ui.menu_view import MenuView

class MainView:
    def __init__(self, root, controller, views):
        self._root = root
        self._views = views
        self._ctrl = controller

        self._frame = None
        self._variables = None

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(self._root, padx = 50, pady = 20)

        self._header()
        self._variables = MenuView(self._frame, self._ctrl).meal_variables
        self._actions()

        self._frame.pack()

    def _generate_menu(self):
        self._ctrl.generate_menu()
        check_status = self._ctrl.fetch_menu()

        if not check_status:
            msg = "Kirjastossa ei ole tarpeeksi ruokia ruokalistan generoimiseen, generaattori" + \
                " tarvitsee vähintään seitsemän eri ruokalajia generoidakseen ruokalistan."
            self._root.after(0, self._views[2](msg, 0))
        else:
            self._root.after(0, self._views[0])

    def _header(self):
        header_frame = ttk.Frame(self._frame)

        header_label = Label(header_frame, text = "Tervetuloa!", pady = 30)
        header_label.configure(anchor = "center", font = "None 17")

        header_label.pack()
        header_frame.pack()

    def _actions(self):
        wrapper = Frame(self._frame, pady = 30)
        action_frame = ttk.LabelFrame(wrapper, text = "Toiminnot", padding = 20)

        generate_menu = ttk.Button(
            action_frame,
            text = "Generoi ruokalista",
            command = lambda: self._generate_menu()
        )
        manage_items = ttk.Button(
            action_frame,
            text = "Hallitse ruokia ja aineksia",
            command = self._views[1]
        )
        logout = ttk.Button(
            action_frame,
            text = "Kirjaudu ulos",
            command = lambda: self._process_logout()
        )
        end_session = ttk.Button(
            action_frame,
            text = "Lopeta",
            command = self._views[3]
        )
        wish_list = ttk.Button(
            action_frame,
            text = "Koosta kauppalista",
            command = self._views[7]
        )

        generate_menu.grid(row = 0, column = 0, padx = 10, pady = 5)
        wish_list.grid(row = 0, column = 1, padx = 10, pady = 5)
        manage_items.grid(row = 0, column = 2, padx = 10, pady = 5)
        logout.grid(row = 0, column = 3, padx = 10, pady = 5)
        end_session.grid(row = 0, column = 4, padx = 10, pady = 5)

        action_frame.pack()
        wrapper.pack()

    def _process_logout(self):
        self._ctrl.logout_user()

        self._root.after(0, self._views[4])
