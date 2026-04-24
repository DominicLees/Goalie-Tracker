from tkinter.ttk import Style

def initStyle():
    """Initialises the master styling. Should be called after all initial widgets have been created to avoid layout issues."""
    style = Style()
    style.configure('TNotebook.Tab', font=('URW Gothic L','12','bold') )