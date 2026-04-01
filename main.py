from tkinter import *

def newGame(name: str):
    if len(name) == 0:
        return
    btns = len(sidebar.winfo_children())
    newBtn = Button(sidebar, text=name, command=lambda: print(name))
    newBtn.grid(column=0, row=btns)
    newBtn.place(relwidth=1)

def openNewGameWindow():
    win = Toplevel()
    win.wm_title("New Game")

    # Create text box for new game
    newGameTextbox = Entry(win)
    newGameTextbox.grid(row=0, column=0)
    newGameTextbox.focus()

    # Create submit button
    submit = Button(win, text="Submit", command=lambda: [newGame(newGameTextbox.get()), win.destroy()])
    submit.grid(row=0, column=1)

root = Tk()
root.title("Goalie Tracker")
# Create root window size of screen
root.geometry("{0}x{1}".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Create sidebar
sidebar = Frame(root, highlightthickness=1, highlightbackground="black")
sidebar.grid(row=0, column=0)
sidebar.place(relwidth=0.2, relheight=1)

# Create main area
main = Frame(root)
main.grid(row=0, column=1, columnspan=4)
main.place(relx=0.2, relwidth=0.8, relheight=1)

menubar = Menu(root)
file = Menu(menubar, tearoff=0)
menubar.add_cascade(label ='File', menu=file)
file.add_command(label ='New Game', command=openNewGameWindow)
root.config(menu = menubar)

root.mainloop()