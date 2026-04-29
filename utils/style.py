from tkinter.ttk import Style
import tkinter.font as tkFont

def initStyle():
    """Initialises the master styling. Should be called after all initial widgets have been created to avoid layout issues."""
    style = Style()
    style.configure('TNotebook.Tab', font=('URW Gothic L','12','bold') )

    default_font = tkFont.nametofont("TkDefaultFont")
    default_font.configure(size=12)