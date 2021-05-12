from tkinter import ttk, StringVar, Listbox, Scrollbar, Button, Frame, Label, Entry, Text, constants
from ui.menu_view import MenuView

class ManagementView:
    def __init__(self, root, controller, views):
        self._root = root
        self._ctrl = controller
        self._views = views

        self._frame = None
        self._menu_variables = None
        self._entry_variables = {
            "entry state": True,
            "text state": True,
            "entry": StringVar(),
            "textbox": None,
        }

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(self._root, padx = 50, pady = 20)

        self._menu_variables = MenuView(self._frame, self._ctrl).meal_variables
        self._items_view()
        self._insert_meal_view()
        self._actions()

        self._frame.pack()

    def _items_view(self):
        parent_frame = Frame(self._frame)

        self._generate_items_view(parent_frame)
        self._generate_items_view(parent_frame, False)

        parent_frame.pack()

    def _generate_items_view(self, parent, meal=True):
        parent_frame = Frame(parent, pady = 30)

        if meal is True:
            items_box = self._generate_listbox(parent_frame)
            view_side = constants.LEFT
            item_label = Label(parent_frame, text = "Lisätyt ruokalajit:", pady = 2)
        else:
            items_box = self._generate_listbox(parent_frame, False)
            view_side = constants.RIGHT
            item_label = Label(parent_frame, text = "Lisätyt raaka-aineet:", pady = 2)

        items_scrollbar = Scrollbar(parent_frame)
        items_box.config(yscrollcommand = items_scrollbar.set)
        items_scrollbar.config(command = items_box.yview)

        item_label.pack()
        items_box.pack(side = constants.LEFT)
        items_scrollbar.pack(side = constants.RIGHT, fill = constants.Y)
        parent_frame.pack(side = view_side)

    def _generate_listbox(self, parent, meal=True):
        if meal is not True:
            items = self._ctrl.fetch_ingredients()
            items.sort(key = lambda x: x.name)
        else:
            items = self._ctrl.fetch_meals()
            items.sort(key = lambda x: x.name)

        items_box = Listbox(parent, bg = "#FFFFFF")

        for i, item in enumerate(items):
            items_box.insert(i, item.name)

        return items_box

    def _insert_meal_view(self):
        parent_frame = Frame(self._frame, pady = 15)

        entry_var = self._entry_variables['entry']
        entry_var.set("Kirjoita tähän ruokalajin nimi")

        meal_entry = Entry(parent_frame, width = 30, textvariable = entry_var, bg = "#FFFFFF")
        meal_entry.focus_set()
        meal_entry.bind("<Button-1>", lambda x: self._entry_event())

        self._entry_variables['textbox'] = Text(parent_frame, height = 10, width = 35, bg="#FFFFFF")
        ingredients_entry = self._entry_variables['textbox']

        default_text = "Kirjoita tähän ruokalajin aineosat rivinvaihdolla eroteltuna"
        ingredients_entry.insert(constants.END, default_text)

        ingredients_entry.focus_set()
        ingredients_entry.bind("<Button-1>", lambda x: self._entry_event(False))
        ingredients_entry.bind("<Key>", lambda x: self._entry_event(False))

        submit = Button(parent_frame, text = "Lisää", command = lambda: self._insert_meal_to_db())
        header_label = Label(parent_frame, text = "Lisää uusi ruokalaji:", pady = 2)

        header_label.pack()
        meal_entry.pack()
        ingredients_entry.pack()
        submit.pack()
        parent_frame.pack()

    def _insert_meal_to_db(self):
        """PÄÄSTÄÄ TOISTAISEKSI MYÖS TYHJÄT MERKKIJONOT JA RIVINVAIHDOT LÄPI, KORJATAAN MYÖHEMMIN"""

        meal = self._entry_variables['entry'].get()
        ingredients = self._entry_variables['textbox'].get(0.0, constants.END).splitlines()

        if meal in "Kirjoita tähän ruokalajin nimi":
            self._root.after(0, self._views[1])
        elif ingredients[0] in "Kirjoita tähän ruokalajin aineosat rivinvaihdolla eroteltuna":
            self._root.after(0, self._views[1])
        else:
            self._ctrl.add_meal(meal, ingredients)
            self._views[2]("Ruokalaji lisättiin kirjastoon!", 1)

    def _entry_event(self, entry=True):
        if self._entry_variables['text state'] and not entry:
            self._entry_variables['textbox'].delete(0.0, constants.END)
            self._entry_variables['text state'] = False

        if entry and self._entry_variables['entry state']:
            self._entry_variables['entry'].set("")
            self._entry_variables['entry state'] = False

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
        end_session.grid(row = 0, column = 2, padx = 15, pady = 5)
        logout.grid(row = 0, column = 1, padx = 15, pady = 5)

        action_frame.pack()
        wrapper.pack()

    def _process_logout(self):
        self._ctrl.logout_user()

        self._root.after(0, self._views[4])
