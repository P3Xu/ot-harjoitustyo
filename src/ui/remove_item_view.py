from tkinter import Button, Frame, Label

class RemoveItemView:
    def __init__(self, root, controller, views, item):
        self._root = root
        self._ctrl = controller
        self._views = views
        self._item = item

        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(self._root, padx = 50, pady = 40, bg = "#FFFFEA")

        self._show_confirm_request()
        self._actions()

        self._frame.pack()

    def _show_confirm_request(self):
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
        self._ctrl.remove_meal(self._item)

        self._root.after(0, self._views[2]("Ruokalaji poistettu onnistuneesti kirjastosta.", 1))
