from tkinter import ttk, StringVar, Listbox, Scrollbar, Button, Frame, Label
from tkinter import LEFT, RIGHT, BOTH, BOTTOM, TOP, X, Y
from ui.menu_view import MenuView

class MainView:
    def __init__(self, root, controller, views):
        self._root = root
        self._frame = None
        self._variables = None
        self._ctrl = controller
        self._views = views

        self._initialize()

    def pack(self):
        self._frame.pack() #fill?

    def destroy(self):
        self._frame.destroy()

    def _generate_menu(self):
        self._ctrl.generate_menu()

        self._root.after(0, self._views[0])

    def _initialize(self):
        self._frame = Frame(self._root)

        self._header()
        self._variables = MenuView(self._frame, self._ctrl).meal_variables
        self._actions()

        self._frame.pack()

    def _header(self):
        header_frame = ttk.Frame(self._frame)

        header_label = Label(header_frame, text = "Tervetuloa!", padx = 10, pady = 10)
        header_label.configure(anchor = "center")

        header_label.pack()
        header_frame.pack()

    def _actions(self):
        action_frame = ttk.LabelFrame(self._frame, text = "Toiminnot")

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

        generate_menu.grid(row = 0, column = 0, padx = 5, pady = 5)
        manage_items.grid(row = 0, column = 1, padx = 5, pady = 5)

        action_frame.pack()
