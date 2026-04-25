from tkinter import *
from tkinter.ttk import *
from components import *
from utils import *

# Create root
root = Tk()
root.title("Goalie Tracker")
# Make root window size of screen
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
tabs = Notebook(root)

# Create main tab
gamesTab = Frame(tabs)
main = Main(gamesTab)
main.grid(row=0, column=1, columnspan=4)
main.place(relx=0.2, relwidth=0.8, relheight=1)

# Create sidebar
sidebar = Sidebar(gamesTab, highlightthickness=1, highlightbackground="black")
sidebar.grid(row=0, column=0)
sidebar.place(relwidth=0.2, relheight=1)
sidebar.main = main

# Create trends tab
trendsTab = Trends(tabs)

# Create tab buttons
tabs.add(gamesTab, text="Games")
tabs.add(trendsTab, text="Trends")
tabs.bind("<<NotebookTabChanged>>", trendsTab.refresh)
tabs.pack(expand=True, fill="both")

# Create menu bar
menubar = Menu(root)
file = Menu(menubar, tearoff=0)
main.fileMenu = file
menubar.add_cascade(label ="File", menu=file)
# New Game
file.add_command(label ="New Game", accelerator="Cmd+N", command=lambda: NewGameWindow(sidebar.newGame))
root.bind("<Command-n>", lambda self: NewGameWindow(sidebar.newGame))
# Rename Game
file.add_command(label ="Rename Game", accelerator="Cmd+R", command=lambda: NewGameWindow(sidebar.renameGame, main.game.name, "Rename Game"), state="disabled")
root.bind("<Command-r>", lambda self: NewGameWindow(sidebar.renameGame, main.game.name, "Rename Game"))
# TODO: Add delete game command
root.config(menu = menubar)

# Populate sidebar
games = getAllGames("name")
for game in games:
    sidebar.createGameButton(game[0])
# Open first game in db
if (len(games) > 0):
    main.openGame(games[0][0])
del games

initStyle()
root.mainloop()