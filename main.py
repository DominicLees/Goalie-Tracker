from tkinter import *

def newLabel():
    labels = len(sidebar.winfo_children())
    newLabel = Label(sidebar, text=newTextbox.get())
    newLabel.grid(column=0, row=labels)

root = Tk()
root.title("Goalie Tracker")
# Create root window size of screen
root.geometry("{0}x{1}".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Create sidebar
sidebar = Frame(root, highlightthickness=1, highlightbackground="black")
sidebar.grid(row=0, column=0)
sidebar.place(relwidth=0.2, relheight=1)

# Create main area
main = Frame(root)
main.grid(row=0, column=1, columnspan=4)
main.place(relx=0.2, relwidth=0.8, relheight=1)

# Create text box for new game
newTextbox = Entry(main)
newTextbox.grid(row=0, column=1)

# Create new button
newBtn = Button(main, text="New", command=newLabel)
newBtn.grid(row=0, column=0)

root.mainloop()