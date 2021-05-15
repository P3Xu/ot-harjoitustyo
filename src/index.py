from tkinter import Tk, ttk, PhotoImage
from pathlib import Path
from repositories.io import InputOutput
from config import ICON_PATH
from ui.ui import UI

def main():
    window = Tk()

    window.title("Ruokalistageneraattori")
    window.configure(bg = "#FFFFEA")

    if Path(ICON_PATH).is_file():
        icon = PhotoImage(file=ICON_PATH)
        window.tk.call('wm', 'iconphoto', window._w, icon) # pylint: disable=protected-access

    check = InputOutput().read("SELECT * FROM meals")

    if not isinstance(check, list):
        text = "Suorita komento poetry run invoke build ennen ohjelman ensimmäistä käynnistystä!"
        label = ttk.Label(window, text = text, padding = 200)
        label.pack()
    else:
        user_interface = UI(window)
        user_interface.start()

    window.mainloop()

if __name__ == "__main__":
    main()
