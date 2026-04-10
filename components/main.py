from tkinter import Button, Entry, Frame, Label
from utils.db import *

class Main(Frame):
    output: Label | None = None

    def openGame(self, name: str):
        # Retrieve data from db
        game = getGame(name)

        # Clear main area
        for child in self.winfo_children():
            child.destroy()

        label = Label(self, text=name, anchor="center")
        label.grid(row=0, columnspan=2)

        Label(self, text="Shots").grid(row=1)
        shots = Entry(self)
        shots.insert(0, game[1])
        shots.grid(row=1, column=1)

        save = Button(self, text="Save", command=lambda: self.saveGame(name, shots.get()))
        save.grid(row=2)

    def saveGame(self, name: str, shots: str):
        updateGame("UPDATE Games SET shots = ? WHERE name = ?", (shots, name))
        self.setOutputMsg("Game updated successfully")

    def setOutputMsg(self, msg: str):
        if self.output == None:
            self.output = Label(self)
            self.output.grid(row=self.grid_size()[0] + 1, columnspan=2)

        self.output.config(text=msg)