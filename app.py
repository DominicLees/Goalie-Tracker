from tkinter import *
from components import *

# Create root
root = Tk()
root.title("Goalie Tracker")
# Make root window size of screen
root.geometry("{0}x{1}".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Create sidebar
sidebar = Sidebar(root, highlightthickness=1, highlightbackground="black")
sidebar.grid(row=0, column=0)
sidebar.place(relwidth=0.2, relheight=1)

# Create main area
main = Main(root)
main.grid(row=0, column=1, columnspan=4)
main.place(relx=0.2, relwidth=0.8, relheight=1)
sidebar.main = main

# Create menu bar
menubar = Menu(root)
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label ="File", menu=file)
file.add_command(label ="New Game", accelerator="Cmd+N", command=lambda: NewGameWindow(sidebar.newGame))
root.bind("<Command-n>", lambda self: NewGameWindow(sidebar.newGame))
root.config(menu = menubar)

root.mainloop()