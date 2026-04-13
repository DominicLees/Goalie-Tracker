from tkinter import Button, Entry, Frame, Label
from utils.db import *

class Main(Frame):
    output: Label | None = None

    def openGame(self, name: str):
        # Retrieve data from db
        self.game = getGame(name)

        # Clear main area
        for child in self.winfo_children():
            child.destroy()

        label = Label(self, text=self.game.name, anchor="center")
        label.grid(row=0, columnspan=2)

        Label(self, text="Shots").grid(row=1)
        self.shots = Entry(self)
        self.shots.insert(0, str(self.game.shots))
        self.shots.grid(row=1, column=1)

        save = Button(self, text="Save", command=self.saveGame)
        save.grid(row=2)

    def saveGame(self):
        if self.game == None:
            return
        # Update game instance
        self.game.shots = int(self.shots.get())
        # Save game data to db
        success = updateGame(self.game)
        if success:
            self.setOutputMsg("Game updated successfully")
        else:
            self.setOutputMsg("Failed to update game")

    def setOutputMsg(self, msg: str):
        if self.output == None or not self.output.winfo_exists():
            self.output = Label(self)
            self.output.grid(row=self.grid_size()[0] + 1, columnspan=2)

        self.output.configure(text=msg)