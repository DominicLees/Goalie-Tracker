from tkinter import Frame, Label

class Main(Frame):
    def openGame(self, name: str):
        # Clear main area
        for child in self.winfo_children():
            child.destroy()

        label = Label(self, text=name, anchor="center")
        label.pack()