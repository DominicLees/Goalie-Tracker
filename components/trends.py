from tkinter import Event, Frame, Label
from utils.db import getAllGames

class Trends(Frame):
    """The trends tab that displays data calculated from all of the logged games"""

    def refresh(self, event: Event):
        """Function called every time the user switches tabs. When the trends tab is selected the contents of the games table is retrieved from the database and the tab is populated.

        Args:
            event (Event): The event object passed to the function.
        """

        # Check the trends tab was selected before continuing
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")
        if tab_text != "Trends":
            return
        
        for child in self.winfo_children():
            child.destroy()
        
        games = getAllGames()
        Label(self, text="{0} games logged".format(len(games))).grid()