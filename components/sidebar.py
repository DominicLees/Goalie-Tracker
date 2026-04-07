from tkinter import Button, Frame

class Sidebar(Frame):
    def newGame(self, name: str):
        if len(name) == 0:
            return
        btns = len(self.winfo_children())
        newBtn = Button(self, text=name, command=lambda: print(name))
        newBtn.grid(column=0, row=btns)