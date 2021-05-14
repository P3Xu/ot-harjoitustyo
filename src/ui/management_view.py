"""UI-moduuli, joka tarjoaa sovelluksen hallintanäkymän."""

from tkinter import StringVar,Listbox,Scrollbar,Button,Frame,Label,Entry,Text,constants,LabelFrame
from ui.menu_view import MenuView

class ManagementView:
    """Luokka sovelluksen hallintanäkymälle.

    Hallintanäkymässä on mahdollista hallita sovelluksen ruokalajeja sekä raaka-aineita.
    Olemassaolevien ruokien ja raaka-aineiden tarkastelun lisäksi näkymässä on mahdollista
    poistaa ruokalaji kirjastosta, tai lisätä uusi ruokalaji raaka-aineineen kirjastoon.
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
        self._menu_variables = None
        self._entry_variables = {
            "entry state": True,
            "text state": True,
            "entry": StringVar(),
            "textbox": None,}

        self._initialize()

    def pack(self):
        """Pakkaa pääkehyksen."""

        self._wrapper.pack()

    def destroy(self):
        """Tuhoaa pääkehyksen."""

        self._wrapper.destroy()

    def _initialize(self):
        """Alustaa näkymän.

        Luo tarvittavat kehykset ja kutsuu näkymän metodeja, jotka luovat näkymän komponentit.
        """

        self._wrapper = Frame(self._root, padx = 20, pady = 20, bg = "#FFFFEA")
        border = Frame(self._wrapper, padx = 2, pady = 2, bg = "#000000")
        self._frame = Frame(border, padx = 50, pady = 10, bg = "#FFFFEA")
        meals_frame = LabelFrame(
            self._frame, text = "Kirjasto", padx = 150, pady = 10, bg = "#FFFFEA")

        self._menu_variables = MenuView(self._frame, self._ctrl).meal_variables

        self._items_view(meals_frame)
        self._insert_meal_view(meals_frame)
        meals_frame.pack()

        self._actions()

        self._frame.pack(expand=True)
        border.pack(expand=True)
        self._wrapper.pack(expand=True)

    def _items_view(self, parent):
        """Pyytää listauskentät ruokalajeille ja raaka-aineille.

        Args:
            parent: isäntäkehys, johon alikehys liitetään.
        """

        parent_frame = Frame(parent, bg = "#FFFFEA")

        self._generate_items_view(parent_frame)
        self._generate_items_view(parent_frame, False)

        parent_frame.pack()

    def _generate_items_view(self, parent, meal=True):
        """Generoi listauskenttäkokonaisuuden.

        Listauskenttäkokonaisuus generoidaan joko ruokalajille tai raaka-aineelle
        parametristä riippuen.

        Args:
            parent: isäntäkehys, johon kenttä sidotaan.
            meal: vipu, jolla metodille kerrotaan, käsitelläänkö ruokalajien vai
            raaka-aineiden kenttää. Oletuksena käsitellään ruokalajien kenttää.
        """

        parent_frame = Frame(parent, bg = "#FFFFEA")

        if meal is True:
            items_box = self._generate_listbox(parent_frame)
            view_side = constants.LEFT
            item_label = Label(parent_frame, text = "Lisätyt ruokalajit:", pady = 2, bg = "#FFFFEA")
        else:
            items_box = self._generate_listbox(parent_frame, False)
            view_side = constants.RIGHT
            item_label = Label(
                parent_frame, text = "Lisätyt raaka-aineet:", pady = 2, bg = "#FFFFEA")

        items_scrollbar = Scrollbar(parent_frame, bg = "#FFFFEA")
        items_box.config(yscrollcommand = items_scrollbar.set)
        items_scrollbar.config(command = items_box.yview)

        item_label.pack()
        items_box.pack(side = constants.LEFT)
        items_scrollbar.pack(side = constants.RIGHT, fill = constants.Y)
        parent_frame.pack(side = view_side)

    def _generate_listbox(self, parent, meal=True):
        """Generoi listauskentän.

        Listauskenttä generoidaan parametrista riippuen joko ruokalajille tai raaka-aineelle.
        Kenttään syötetään jommat kummat arvoksi ja ruokalajin tapauksessa kenttään sidotaan
        triggeri tuplaklikkaukselle, jolla päästään poistamaan ruokalajeja kirjastosta.

        Args:
            parent: isäntäkehys, johon kenttä sidotaan.
            meal: vipu, jolla metodille kerrotaan, käsitelläänkö ruokalajien vai
            raaka-aineiden kenttää. Oletuksena käsitellään ruokalajien kenttää.

        Returns:
            Palauttaa listbox-objektin, joka sisältää ruokalajit tai raaka-aineet.
        """

        if not meal:
            items = self._ctrl.fetch_ingredients()
            items.sort(key = lambda x: x.name)
        else:
            items = self._ctrl.fetch_meals()
            items.sort(key = lambda x: x.name)

        items_box = Listbox(parent, bg = "#FFFFFF")

        if meal:
            items_box.bind("<Double-Button-1>",
                lambda x: self._process_remove(items_box.get(constants.ACTIVE)))

        for i, item in enumerate(items):
            items_box.insert(i, item)

        return items_box

    def _insert_meal_view(self, parent):
        """Luo ruokalajien lisäämiseen tarvittavat komponentit näkymään.

        Args:
            parent: isäntäkehys, johon näkymä sidotaan.
        """

        parent_frame = Frame(parent, pady = 15, bg = "#FFFFEA")

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

        submit = Button(
            parent_frame,
            text = "Lisää",
            command = lambda: self._insert_meal_to_db(),
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")
        header_label = Label(parent_frame, text = "Lisää uusi ruokalaji:", pady = 2, bg = "#FFFFEA")

        header_label.pack()
        meal_entry.pack()
        ingredients_entry.pack()
        submit.pack()
        parent_frame.pack()

    def _insert_meal_to_db(self):
        """Prosessoi ruokalajin lisäämisen tietokantaan.

        Metodi tarkistaa, ettei kantaan yritetä lisätä oletustekstiä tai pelkästä välilyönnistä
        koostuvia merkkijonoja. Jos kaikki on kunnossa, pyydetään controlleria lisäämään ruokalaji
        tietokantaan ja informoidaan käyttäjää onnistuneesta lisäyksestä.
        """

        meal = self._entry_variables['entry'].get()
        ingredients = self._entry_variables['textbox'].get(0.0, constants.END).splitlines()

        if meal in "Kirjoita tähän ruokalajin nimi" or len(meal.strip()) == 0:
            self._root.after(0, self._views[1])
        elif (ingredients[0] in "Kirjoita tähän ruokalajin aineosat rivinvaihdolla eroteltuna"
            or len(ingredients[0].strip()) == 0 or len(ingredients[-1].strip()) == 0):

            self._root.after(0, self._views[1])
        else:
            self._ctrl.add_meal(meal, ingredients)
            self._views[2]("Ruokalaji lisättiin kirjastoon!", 1)

    def _entry_event(self, entry=True):
        """Prosessoi inputtien tyhjentämisen klikattaessa.

        Args:
            entry: vipu sille, että kumpaa inputtia käsitellään.
        """

        if self._entry_variables['text state'] and not entry:
            self._entry_variables['textbox'].delete(0.0, constants.END)
            self._entry_variables['text state'] = False

        if entry and self._entry_variables['entry state']:
            self._entry_variables['entry'].set("")
            self._entry_variables['entry state'] = False

    def _actions(self):
        """Luo painikkeet muihin näkymiin siirtymistä varten."""

        wrapper = Frame(self._frame, pady = 30, bg = "#FFFFEA")
        action_frame = LabelFrame(wrapper, text = "Toiminnot", padx = 20, pady = 20, bg = "#FFFFEA")

        back = Button(
            action_frame,
            text = "Palaa takaisin",
            command = self._views[0],
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")
        end_session = Button(
            action_frame,
            text = "Lopeta",
            command = self._views[3],
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")
        logout = Button(
            action_frame,
            text = "Kirjaudu ulos",
            command = lambda: self._process_logout(),
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")

        back.grid(row = 0, column = 0, padx = 15)
        end_session.grid(row = 0, column = 2, padx = 15)
        logout.grid(row = 0, column = 1, padx = 15)

        action_frame.pack()
        wrapper.pack()

    def _process_logout(self):
        """Prosessoi käyttäjän uloskirjautumisen."""

        self._ctrl.logout_user()

        self._root.after(0, self._views[4])

    def _process_remove(self, item):
        """Prosessoi ruokalajin poistopyynnön."""

        self._root.after(0, self._views[6](item))
