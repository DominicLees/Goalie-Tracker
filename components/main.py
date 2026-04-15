from tkinter import Button, Entry, Frame, Label
from utils.db import *

# TODO: docstrings
class Main(Frame):
    output: Label | None = None

    def openGame(self, name: str):
        # Retrieve data from db
        self.game = getGame(name)

        # Clear main area
        for child in self.winfo_children():
            child.destroy()

        # Create page title
        label = Label(self, text=self.game.name, anchor="center")
        label.grid(row=0, columnspan=4)

        # Create shots against entry box
        Label(self, text="Shots against").grid(row=1)
        self.shots = Entry(self, validate="key")
        self.shots.insert(0, str(self.game.shots))
        self.shots.grid(row=1, column=1)

        # Create goals conceded entry box
        Label(self, text="Goals conceded").grid(row=1, column=2)
        self.goals = Entry(self, validate="key")
        self.goals.insert(0, str(self.game.goals))
        self.goals.grid(row=1, column=3)

        # Create saves and save percentage labels
        Label(self, text="Saves: ").grid(row=2)
        self.saves = Label(self, text="0")
        self.saves.grid(row=2, column=1)
        Label(self, text="Save percentage: ").grid(row=2, column=2)
        self.savePct = Label(self, text="0%")
        self.savePct.grid(row=2, column=3)
        if self.game.goals > 0:
            self.calcSaves()
        
        # Add validation commands
        self.shots.configure(validatecommand=(self.register(self.validateShots), "%P"))
        self.goals.configure(validatecommand=(self.register(self.validateGoals), "%P"))

        # Create save button
        save = Button(self, text="Save", command=self.saveGame)
        save.grid(row=3)

        # Create reset button
        reset = Button(self, text="Reset", command=lambda: self.openGame(name))
        reset.grid(row=3, column=1)

    def saveGame(self):
        if self.game == None:
            return
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

    def calcSaves(self):
        saves = int(self.game.shots - self.game.goals)
        self.saves.configure(text=str(saves))
        self.savePct.configure(text=f"{saves / self.game.shots:.3f}")

    def validateShots(self, newValue: str) -> bool:
        if newValue == "":
            return True
        try:
            shots = int(newValue)
            if shots >= 0 and shots < 1000:
                self.game.shots = shots
                self.calcSaves()
                return True
        except Exception as e:
            print(e)
        return False
    
    def validateGoals(self, newValue: str) -> bool:
        if newValue == "":
            return True
        try:
            goals = int(newValue)
            if goals >= 0 and goals < 1000:
                self.game.goals = goals
                self.calcSaves()
                return True
        except Exception as e:
            print(e)
        return False