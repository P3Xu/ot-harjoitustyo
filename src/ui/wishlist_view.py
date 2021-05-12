from tkinter import ttk, Frame, Label, Listbox, Scrollbar, Button, constants
from ui.menu_view import MenuView

class WishlistView:
    def __init__(self, root, controller, views):
        self._root = root
        self._views = views
        self._ctrl = controller

        self._frame = None
        self._variables = None
        self._wishlist = None

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(self._root, padx = 50, pady = 20)

        self._variables = MenuView(self._frame, self._ctrl).meal_variables
        self._generate_wishlist()
        self._actions()

        self._frame.pack()

    def _generate_wishlist(self):
        parent_frame = Frame(self._frame, pady = 15)
        wrapper = Frame(parent_frame, pady = 15)

        item_label = Label(wrapper, text = "Ruokalistan raaka-aineet:", pady = 2)
        item_scroll = Scrollbar(wrapper)

        item_box = self._get_listbox(wrapper)
        save_button = Button(
            parent_frame,
            text = "Tallenna kauppalista\ntiedostoon",
            command = lambda: self._process_save(),
            pady = 5)

        item_box.config(yscrollcommand = item_scroll.set)
        item_scroll.config(command = item_box.yview)

        item_label.pack()

        item_box.pack(side = constants.LEFT)
        item_scroll.pack(side = constants.RIGHT, fill = constants.Y)

        wrapper.pack()
        save_button.pack()
        parent_frame.pack()

    def _get_listbox(self, parent):
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
        wrapper = Frame(self._frame, pady = 20)
        action_frame = ttk.LabelFrame(wrapper, text = "Toiminnot", padding = 20)

        back = ttk.Button(
            action_frame,
            text = "Palaa takaisin",
            command = self._views[0]
        )
        end_session = ttk.Button(
            action_frame,
            text = "Lopeta",
            command = self._views[3]
        )
        logout = ttk.Button(
            action_frame,
            text = "Kirjaudu ulos",
            command = lambda: self._process_logout()
        )

        back.grid(row = 0, column = 0, padx = 15, pady = 5)
        logout.grid(row = 0, column = 1, padx = 15, pady = 5)
        end_session.grid(row = 0, column = 2, padx = 15, pady = 5)

        action_frame.pack()
        wrapper.pack()

    def _process_save(self):
        file_name = self._ctrl.export_wishlist(self._wishlist)
        msg = "Kauppalista tallennettiin onnistuneesti tiedostoon "+file_name[1:]

        self._root.after(0, self._views[2](msg, 7))

    def _process_logout(self):
        self._ctrl.logout_user()

        self._root.after(0, self._views[4])
