from tkinter import Button, Frame
from components.main import Main
import sqlite3

class Sidebar(Frame):
    main: Main

    def createGameButton(self, name: str):
        btns = len(self.winfo_children())
        newBtn = Button(self, text=name, command=lambda: self.main.openGame(name))
        newBtn.grid(column=0, row=btns)

    def newGame(self, name: str):
        if len(name) == 0:
            return
        # Save to db
        db = sqlite3.connect("data")
        cu = db.cursor()
        cu.execute("INSERT INTO Games(name, shots) VALUES (?, 0)", (name,))
        cu.close()
        db.commit()
        db.close()

        # Create new sidebar button
        self.createGameButton(name)