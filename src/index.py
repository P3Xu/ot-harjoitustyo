from tkinter import Tk
from ui.ui import UI

window = Tk()
window.title("Ruokalistageneraattori")
window.configure(bg = "#FFFFEB")

ui = UI(window)
ui.start()

window.mainloop()
