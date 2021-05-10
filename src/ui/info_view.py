from tkinter import Frame, Label, constants

class InfoView:
    def __init__(self, root, controller, views, message, view_number):
        self._root = root
        self._ctrl = controller
        self._views = views
        self._msg = message
        self._view_number = view_number

        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = Frame(self._root)

        self._show_information()
        self._frame.pack()

        self._root.after(2500, self._views[self._view_number])

    def _show_information(self):
        parent_frame = Frame(self._frame, padx = 20, pady = 20)

        status_label = Label(parent_frame, text = self._msg, padx = 10, pady = 10, justify = constants.CENTER)

        status_label.pack()
        parent_frame.pack()
