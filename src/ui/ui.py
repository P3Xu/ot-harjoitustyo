from ui.main_view import MainView
from ui.management_view import ManagementView
from ui.info_view import InfoView
from ui.login_view import LoginView
from ui.create_user_view import CreateUserView
from ui.remove_item_view import RemoveItemView
from ui.wishlist_view import WishlistView
from services.controller import Controller

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None
        self._ctrl = Controller()
        self._views = [
            self._show_main_view,           #0
            self._show_management_view,     #1
            self._show_information_view,    #2
            self._end_session,              #3
            self._show_login_view,          #4
            self._show_create_user_view,    #5
            self._show_remove_item_view,    #6
            self._show_wishlist_view,       #7
            self
        ]
        self.user = None

    def start(self):
        self._show_login_view()

    def _show_main_view(self):
        self._empty_view()

        self._current_view = MainView(self._root, self._ctrl, self._views)
        self._current_view.pack()

    def _show_management_view(self):
        self._empty_view()

        self._current_view = ManagementView(self._root, self._ctrl, self._views)
        self._current_view.pack()

    def _show_information_view(self, msg, view_number):
        self._empty_view()

        self._current_view = InfoView(self._root, self._ctrl, self._views, msg, view_number)
        self._current_view.pack()

    def _show_login_view(self):
        self._empty_view()

        self._current_view = LoginView(self._root, self._ctrl, self._views)
        self._current_view.pack()

    def _show_create_user_view(self):
        self._empty_view()

        self._current_view = CreateUserView(self._root, self._ctrl, self._views)
        self._current_view.pack()

    def _show_remove_item_view(self, item):
        self._empty_view()

        self._current_view = RemoveItemView(self._root, self._ctrl, self._views, item)
        self._current_view.pack()

    def _show_wishlist_view(self):
        self._empty_view()

        self._current_view = WishlistView(self._root, self._ctrl, self._views)
        self._current_view.pack()

    def _empty_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _end_session(self):
        self._root.destroy()
