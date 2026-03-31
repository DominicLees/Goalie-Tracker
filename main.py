from tkinter import *

root = Tk()

root.title("Goalie Tracker")

# Create root window size of screen
root.geometry("{0}x{1}".format(root.winfo_screenwidth(), root.winfo_screenheight()))

# Create sidebar
sidebar = Frame(root)
sidebar.grid(row=0, column=0)

# Create main area
main = Frame(root)
main.grid(row=0, column=1, columnspan=4)

root.mainloop()