from tkinter import Button, Entry, Toplevel
from typing import Callable

class NewGameWindow(Toplevel):
    def __init__(self, cb: Callable[[str], None], text=""):
        super().__init__()
        self.cb = cb
        self.wm_title("New Game")

        # Create text box for new game
        self.newGameTextbox = Entry(self, text=text)
        self.newGameTextbox.grid(row=0, column=0)
        self.newGameTextbox.bind("<Return>", self.submit)
        self.newGameTextbox.focus()

        # Create submit button
        submit = Button(self, text="Submit", command=self.submit)
        submit.grid(row=0, column=1)

    def submit(self):
        name = self.newGameTextbox.get()
        if len(name) == 0:
            return
        
        self.cb(name)
        self.destroy()