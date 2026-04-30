from tkinter import Button, Entry, Event, Toplevel
from typing import Callable

class NewGameWindow(Toplevel):
    """Window used to get a name for a game from the user"""
    def __init__(self, cb: Callable[[str], None], text="", title="New Game"):
        super().__init__()
        self.cb = cb
        self.wm_title(title)

        # Create text box for new game
        self.newGameTextbox = Entry(self)
        self.newGameTextbox.insert(0, text)
        self.newGameTextbox.grid(row=0, column=0)
        self.newGameTextbox.bind("<Return>", self.submit)
        self.newGameTextbox.focus()

        # Create submit button
        submit = Button(self, text="Submit", command=self.submit)
        submit.grid(row=0, column=1)

    def submit(self, entry: Event=None):
        """Submit event handler

        Args:
            entry (Event, optional): Event object passed by bind(), not used. Defaults to None.
        """
        name = self.newGameTextbox.get()
        if len(name) == 0:
            return
        
        self.cb(name)
        self.destroy()