from tkinter import Button, Event, Frame
from components.main import Main
from utils.db import *

class Sidebar(Frame):
    """The sidebar that contains the buttons to open games from the database. Displayed in the Games tab to the left of the main widget."""
    main: Main

    def createGameButton(self, name: str):
        """Creates a button in the sidebar for opening a game.

        Args:
            name (str): The name of the game associated with the button.
        """
        btns = len(self.winfo_children())
        newBtn = Button(self, text=name, command=lambda: self.main.openGame(name))
        newBtn.grid(column=0, row=btns, sticky="nsew")

    def newGame(self, name: str):
        """Creates a new game in the database and creates the associated sidebar button.

        Args:
            name (str): The name of the new game.
        """
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
        """Renames the currently open game to a new name.

        Args:
            newName (str): The name to change the currently open game's to.
        """
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
                break
        
        self.main.openGame(newName)

    def deleteGame(self, entry: Event=None):
        """Deletes the currently open game.

        Args:
            entry (Event, optional): Event object passed by bind(), not used. Defaults to None.
        """
        if self.main.game == None:
            return

        success = deleteGame(self.main.game.name)
        if not success:
            return
        
        # Delete game button from sidebar
        for button in self.winfo_children():
            if button.cget("text") == self.main.game.name:
                button.destroy()
                break

        # Reassign grid rows to game buttons
        for i, button in enumerate(self.winfo_children()):
            button.grid(row=i)
     
        self.main.empty()
        # Disable Menu bar
        self.main.fileMenu.entryconfig("Rename Game", state="disabled")
        self.main.fileMenu.entryconfig("Delete Game", state="disabled")