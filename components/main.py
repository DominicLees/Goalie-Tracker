from tkinter import Button, Entry, Frame, Label, Menu, Misc
from utils.db import *
import logging

logger = logging.getLogger(__name__)

class Main(Frame):
    """The main frame that contains the form to modify game data. Displayed to the right of the sidebar."""
    
    output: Label | None = None
    fileMenu: Menu
    saves: Entry | None = None
    savePct: Entry | None = None

    def __init__(self, root: Misc):
        super().__init__(root)
        self.columnconfigure([0, 1, 2, 3], weight=1)
        self.empty()

    def openGame(self, name: str):
        """Opens the edit game screen in the main area of the window

        Args:
            name (str): The name of the game in the db
        """
        # Clear main area
        self.clear()

        # Retrieve data from db
        self.game = getGame(name)
        if self.game == None:
            return

        # Create page title
        label = Label(self, text=self.game.name, anchor="center", font=('URW Gothic L','24','bold'))
        label.grid(row=0, columnspan=4)

        # Create saves and save percentage labels
        Label(self, text="Saves: ").grid(row=2, sticky="e")
        self.saves = Label(self, text="0")
        self.saves.grid(row=2, column=1, sticky="w")
        Label(self, text="Save percentage: ").grid(row=2, column=2, sticky="e")
        self.savePct = Label(self, text="0%")
        self.savePct.grid(row=2, column=3, sticky="w")

        # Create shots against entry box
        Label(self, text="Shots against").grid(row=1, sticky="e")
        self.shots = Entry(self, validate="key", validatecommand=(self.register(self.validateShots), "%P"))
        self.shots.insert(0, str(self.game.shots))
        self.shots.grid(row=1, column=1, sticky="w")

        # Create goals conceded entry box
        Label(self, text="Goals conceded").grid(row=1, column=2, sticky="e")
        self.goals = Entry(self, validate="key", validatecommand=(self.register(self.validateGoals), "%P"))
        self.goals.insert(0, str(self.game.goals))
        self.goals.grid(row=1, column=3, sticky="w")

        # Create save button
        save = Button(self, text="Save", command=self.saveGame)
        save.grid(row=3)

        # Create reset button
        reset = Button(self, text="Reset", command=lambda: self.openGame(name))
        reset.grid(row=3, column=1)

        # Enable menu bar
        self.fileMenu.entryconfig("Rename Game", state="active")
        self.fileMenu.entryconfig("Delete Game", state="active")

    def saveGame(self):
        """Saves the currently opened game to the db"""
        if self.game == None:
            return
        # Save game data to db
        success = updateGame(self.game)
        if success:
            self.setOutputMsg("Game updated successfully")
        else:
            self.setOutputMsg("Failed to update game")

    def setOutputMsg(self, msg: str):
        """Creates a label at the bottom of the main area

        Args:
            msg (str): The text to display
        """
        if self.output == None or not self.output.winfo_exists():
            self.output = Label(self)
            self.output.grid(row=self.grid_size()[0] + 1, columnspan=2)

        self.output.configure(text=msg)

    def clear(self):
        """Destroys all child widgets"""
        self.game = None
        for child in self.winfo_children():
            child.destroy()

    def empty(self):
        """Clears the current contents of main and creates a label containing a tip"""
        self.clear()
        Label(self, text="Press Cmd+N to create a new game").place(relx=0.5, rely=0.5, anchor="center")

    def calcSaves(self):
        """Updates the save count and save percentage labels"""
        if self.saves == None or self.savePct == None:
            return
        self.saves.configure(text=str(self.game.getSaves()))
        self.savePct.configure(text=f"{self.game.getSavePct():.3f}")

    def validateShots(self, newValue: str) -> bool:
        """Validate command for shots against entry

        Args:
            newValue (str): The new contents of the entry being validated

        Returns:
            bool: True if the new input was accepted, False the entry content will stay the same
        """
        if newValue == "":
            return True
        try:
            shots = int(newValue)
            if shots >= 0 and shots < 1000:
                self.game.shots = shots
                self.calcSaves()
                return True
        except ValueError as e:
            logger.debug(e)
        except Exception as e:
            logger.exception(e)
        return False
    
    def validateGoals(self, newValue: str) -> bool:
        """Validate command for goals against entry

        Args:
            newValue (str): The new contents of the entry being validated

        Returns:
            bool: True if the new input was accepted, False the entry content will stay the same
        """
        if newValue == "":
            return True
        try:
            goals = int(newValue)
            if goals >= 0 and goals < 1000:
                self.game.goals = goals
                self.calcSaves()
                return True
        except ValueError as e:
            logger.debug(e)
        except Exception as e:
            logger.exception(e)
        return False