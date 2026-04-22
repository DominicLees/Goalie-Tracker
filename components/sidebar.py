from tkinter import Button, Frame
from components.main import Main
from utils.db import *

# TODO: docstrings
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
        success = insertNewGame(name)
        if not success:
            return
        
        # Create new sidebar button
        self.createGameButton(name)
        self.main.openGame(name)

    def renameGame(self, newName: str):
        if len(newName) == 0:
            return
        oldName = self.main.game.name
        # Save to db
        success = updateGameName(oldName, newName)
        if not success:
            return
        
        # Update button text
        for button in self.winfo_children():
            if button.cget("text") == oldName:
                button.configure(text=newName)
        
        self.main.openGame(newName)