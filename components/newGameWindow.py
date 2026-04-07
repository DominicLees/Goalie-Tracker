from tkinter import Button, Entry, Toplevel
from typing import Callable

class NewGameWindow:
    def __init__(self, cb: Callable[[str], None]):
        win = Toplevel()
        win.wm_title("New Game")

        # Create text box for new game
        newGameTextbox = Entry(win)
        newGameTextbox.grid(row=0, column=0)
        newGameTextbox.bind("<Return>", lambda self: [cb(newGameTextbox.get()), win.destroy()])
        newGameTextbox.focus()

        # Create submit button
        submit = Button(win, text="Submit", command=lambda: [cb(newGameTextbox.get()), win.destroy()])
        submit.grid(row=0, column=1)