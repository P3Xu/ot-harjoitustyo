from tkinter import Tk
from ui.ui import UI

window = Tk()
window.title("Ruokalistageneraattori")
#window.geometry("1024x768")
#window.resizable(False, False)

ui = UI(window)
ui.start()

"""width = window.winfo_reqwidth()
height = window.winfo_reqheight()

pos_right = int(window.winfo_screenwidth()/2 - width/2)
pos_down = int(window.winfo_screenheight()/2 - height/2)


window.geometry("+{}+{}".format(pos_right, pos_down))
"""

window.mainloop()
