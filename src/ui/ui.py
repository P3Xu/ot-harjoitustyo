from ui.main_view import MainView
from ui.management_view import ManagementView, InfoView
from services.controller import Controller

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._ctrl = Controller()
        self._views = [
            self._show_main_view,
            self._show_management_view,
            self._show_information_view
        ]
        self.msg = None

    def start(self):
        self._show_main_view()
        #self._show_management_view()

    def _show_main_view(self):
        self._empty_view()

        self._current_view = MainView(self._root, self._ctrl, self._views)
        self._current_view.pack()

    def _show_management_view(self):
        self._empty_view()

        self._current_view = ManagementView(self._root, self._ctrl, self._views)
        self._current_view.pack()

    def _show_information_view(self, msg):
        self._empty_view()

        self._current_view = InfoView(self._root, self._ctrl, self._views, msg)
        self._current_view.pack()

    def _empty_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None
