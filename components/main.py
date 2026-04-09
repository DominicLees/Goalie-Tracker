from tkinter import Button, Entry, Frame, Label
import sqlite3

class Main(Frame):
    output: Label | None = None

    def openGame(self, name: str):
        # Retrieve data from db
        db = sqlite3.connect("data")
        cu = db.cursor()
        cu.execute("Select * FROM Games WHERE name = ?", (name,))
        game = cu.fetchone()
        cu.close()
        db.commit()
        db.close()

        # Clear main area
        for child in self.winfo_children():
            child.destroy()

        label = Label(self, text=name, anchor="center")
        label.grid(row=0, columnspan=2)

        Label(self, text="Shots").grid(row=1)
        shots = Entry(self)
        shots.insert(0, game[1])
        shots.grid(row=1, column=1)

        save = Button(self, text="Save", command=lambda: self.updateGame(name, shots.get()))
        save.grid(row=2)

    def updateGame(self, name: str, shots: str):
        db = sqlite3.connect("data")
        cu = db.cursor()
        cu.execute("UPDATE Games SET shots = ? WHERE name = ?", (shots, name))
        cu.close()
        db.commit()
        db.close()
        self.setOutputMsg("Game updated successfully")

    def setOutputMsg(self, msg: str):
        if self.output == None:
            self.output = Label(self)
            self.output.grid(row=self.grid_size()[0] + 1, columnspan=2)

        self.output.config(text=msg)