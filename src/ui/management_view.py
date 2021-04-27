from tkinter import ttk, StringVar, Listbox, Scrollbar, Button, Frame, Label, Entry, Text
from tkinter import constants
from time import time
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
        self._frame.pack() #fill?

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(self._root)

        self._menu_variables = MenuView(self._frame, self._ctrl).meal_variables
        self._items_view()
        self._insert_view()
        self._insert_meal_view()

        self._frame.pack()

    def _items_view(self):
        items_frame = Frame(self._frame)

        self._generate_items_view(items_frame)
        self._generate_items_view(items_frame, False)

        items_frame.pack()

    def _generate_items_view(self, parent, meal=True):
        items_frame = Frame(parent)

        if meal is True:
            items_box = self._generate_listbox(items_frame)
            view_side = constants.LEFT
            item_label = Label(items_frame, text = "Lisätyt ruokalajit:", padx = 10, pady = 10)
        else:
            items_box = self._generate_listbox(items_frame, False)
            view_side = constants.RIGHT
            item_label = Label(items_frame, text = "Lisätyt raaka-aineet:", padx = 10, pady = 10)

        items_scrollbar = Scrollbar(items_frame)
        items_box.config(yscrollcommand = items_scrollbar.set)
        items_scrollbar.config(command = items_box.yview)

        item_label.pack()
        items_box.pack(side = constants.LEFT)
        items_scrollbar.pack(side = constants.RIGHT, fill = constants.Y)
        items_frame.pack(side = view_side)

    def _generate_listbox(self, parent, meal=True):
        if meal is not True:
            items = self._ctrl.fetch_ingredients()
        else:
            items = self._ctrl.fetch_meals()

        items_box = Listbox(parent)

        for i, item in enumerate(items):
            items_box.insert(i, item.name)

        return items_box

    def _insert_view(self):
        parent_frame = Frame(self._frame)

        header_label = Label(parent_frame, text = "Lisää uusi ruokalaji:", padx = 10, pady = 10)

        header_label.pack()
        parent_frame.pack()

    def _insert_meal_view(self):
        parent_frame = ttk.Frame(self._frame, padding = 10)

        entry_var = self._entry_variables['entry']
        entry_var.set("Kirjoita tähän ruokalajin nimi")

        meal_entry = Entry(parent_frame, width = 30, textvariable = entry_var)
        meal_entry.focus_set()
        meal_entry.bind("<Button-1>", lambda x: self._entry_event())

        self._entry_variables['textbox'] = Text(parent_frame, height = 10, width = 35)
        ingredients_entry = self._entry_variables['textbox']

        default_text = "Kirjoita tähän ruokalajin aineosat rivinvaihdolla eroteltuna"
        ingredients_entry.insert(constants.END, default_text)
        ingredients_entry.focus_set()
        ingredients_entry.bind("<Button-1>", lambda x: self._entry_event(False))
        submit = Button(parent_frame, text = "Lisää", command = lambda: self._insert_meal_to_db())

        meal_entry.pack()
        ingredients_entry.pack()
        submit.pack()
        parent_frame.pack()

    def _insert_meal_to_db(self):
        meal = self._entry_variables['entry'].get()
        ingredients = self._entry_variables['textbox'].get(0.0, constants.END).splitlines()

        status = self._ctrl.add_meal(meal, ingredients)

        self._views[2](status)

    def _entry_event(self, entry=True):
        if self._entry_variables['text state'] and not entry:
            self._entry_variables['textbox'].delete(0.0, constants.END)
            self._entry_variables['text state'] = False

        if entry and self._entry_variables['entry state']:
            self._entry_variables['entry'].set("")
            self._entry_variables['entry state'] = False

class InfoView:
    def __init__(self, root, controller, views, msg):
        self._root = root
        self._ctrl = controller
        self._views = views
        self._status = msg

        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack() #fill?

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(self._root)

        self._show_information()

        self._frame.pack()

        self._root.after(5000, self._views[1])

    def _show_information(self):
        parent_frame = Frame(self._frame)

        if self._status == 0:
            status_text = "Ruokalaji lisättiin kirjastoon!"
        if self._status < 0:
            status_text = """Ruokalaji löytyy jo kirjastosta.\n
            Lisää toinen ruokalaji, tai poista olemassaoleva 
            (poistamista ei vielä implementoitu)."""

        # Keskitys?

        status_label = Label(parent_frame, text = status_text, padx = 10, pady = 10)

        status_label.pack()
        parent_frame.pack()
