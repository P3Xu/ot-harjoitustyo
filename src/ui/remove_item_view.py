"""UI-moduuli, joka tarjoaa varmistusnäkymän ruokalajin poistamiselle."""

from tkinter import Button, Frame, Label

class RemoveItemView:
    """Luokka ruokalajin poistonäkymälle.

    Tässä näkymässä käyttäjältä varmistetaan ruokalajin poistaminen.
    """

    def __init__(self, root, controller, views, item):
        """Konstruktori, alustaa luokan attribuutit.

        Args:
            root: isäntäkehys, johon näkymän pääkehys kiinnitetään.
            controller: käytettävä controller-luokka.
            views: lista muista sovelluksen näkymistä, joihin voi siirtyä kutsumalla halutun
                näkymän numeroa listalta.
            item: poistettava ruokalaji.
        """

        self._root = root
        self._ctrl = controller
        self._views = views
        self._item = item

        self._frame = None

        self._initialize()

    def pack(self):
        """Pakkaa pääkehyksen."""

        self._frame.pack()

    def destroy(self):
        """Tuhoaa pääkehyksen."""

        self._frame.destroy()

    def _initialize(self):
        """Alustaa näkymän."""

        self._frame = Frame(self._root, padx = 50, pady = 40, bg = "#FFFFEA")

        self._show_confirm_request()
        self._actions()

        self._frame.pack()

    def _show_confirm_request(self):
        """Luo näkymän tekstikomponentin."""

        parent_frame = Frame(self._frame, padx = 20, pady = 20, bg = "#FFFFEA")

        text_pre = "Haluatko varmasti poistaa ruokalajin"
        text_post = "kirjastosta?"

        label_pre = Label(parent_frame, text = text_pre, bg = "#FFFFEA")
        label_post = Label(parent_frame, text = text_post, bg = "#FFFFEA")
        label_item = Label(parent_frame, text = self._item, bg = "#FFFFEA")
        label_item.configure(font = "None 10 bold")

        label_pre.grid(row = 0, column = 0)
        label_item.grid(row = 0, column = 1)
        label_post.grid(row = 0, column = 2)

        parent_frame.pack()

    def _actions(self):
        """Luo painikkeet joilla joko prosessoidaan poisto tai palataan takaisin."""

        parent_frame = Frame(self._frame, pady = 10, bg = "#FFFFEA")

        yes_button = Button(
            parent_frame,
            text = "Kyllä",
            command = lambda: self._process_remove(),
            padx = 20, pady = 10,
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")
        no_button = Button(
            parent_frame,
            text = "Ei",
            command = self._views[1],
            padx = 20, pady = 10,
            bg = "#FFFFEA",
            activebackground = "#FFFFFF")

        yes_button.grid(row = 0, column = 0, padx = 15, pady = 5)
        no_button.grid(row = 0, column = 1, padx = 15, pady = 5)

        parent_frame.pack()

    def _process_remove(self):
        """Prosessoi poistotoimenpiteen.

        Pyytää controlleria poistamaan annetun ruokalajin tietokannasta.
        Informoi käyttäjää onnistuneesta poistosta ja palaa takaisin hallintanäkymään.
        """

        self._ctrl.remove_meal(self._item)

        self._root.after(0, self._views[2]("Ruokalaji poistettu onnistuneesti kirjastosta.", 1))
