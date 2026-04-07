from tkinter import Button, Frame
from components.main import Main

class Sidebar(Frame):
    main: Main

    def newGame(self, name: str):
        if len(name) == 0:
            return
        btns = len(self.winfo_children())
        newBtn = Button(self, text=name, command=lambda: self.main.openGame(name))
        newBtn.grid(column=0, row=btns)