from tkinter import Event, Frame, Label, Misc
from tkinter.ttk import Notebook
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from utils.db import GameRecords, getAllGames

def total(values: GameRecords, pos: int) -> int:
    """Finds the total value of a specific index in a list of tuples.

    Args:
        values (GameRecords): A list of tuples representing game data.
        pos (int): The position in the tuples to find the average of.

    Returns:
        int: The total value found.
    """
    total = 0
    for game in values:
        total += game[pos]
    return total

def average(values: GameRecords, pos: int) -> float:
    """Finds the average value of a specific index in a list of tuples.

    Args:
        values (GameRecords): A list of tuples representing game data.
        pos (int): The position in the tuples to find the average of.

    Returns:
        float: The average value found.
    """
    recordCount = len(values)
    if recordCount < 1:
        return 0
    return total(values, pos) / len(values)

class Trends(Frame):
    """The trends tab that displays data calculated from all of the logged games"""

    def __init__(self, root: Misc):
        super().__init__(root)
        self.columnconfigure([0, 1], weight=1)

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
        
        # Clear existing widgets
        for child in self.winfo_children():
            child.destroy()
        
        # Get all games and sort by date
        self.games = getAllGames()
        self.games.sort(key=lambda game: game[3])
        # Calculate totals
        totalShots = total(self.games, 1)
        totalGoals = total(self.games, 2)
        # Calculate averages
        averageShots = average(self.games, 1)
        averageGoals = average(self.games, 2)
        averageSaves = averageShots - averageGoals
        
        # Create total games label
        Label(self, text="{0} games logged".format(len(self.games))).grid(columnspan=2)
        
        # Create averages labels
        Label(self, text="Average shots against per game: {0}".format(averageShots)).grid(row=1)
        Label(self, text="Average goals against per game: {0}".format(averageGoals)).grid(row=2)
        Label(self, text="Average saves per game: {0}".format(averageSaves)).grid(row=3)

        # Create totals labels
        Label(self, text="Total shots against: {0}".format(totalShots)).grid(row=1, column=1)
        Label(self, text="Total goals against: {0}".format(totalGoals)).grid(row=2, column=1)
        Label(self, text="Total saves: {0}".format(totalShots - totalGoals)).grid(row=3, column=1)

        graphTabs = Notebook(self)
        graphTabs.grid(row=4, columnspan=2)
        graphTabs.add(Frame(graphTabs), text="Shots Against")
        graphTabs.add(Frame(graphTabs), text="Goals Against")
        graphTabs.add(Frame(graphTabs), text="Saves")
        graphTabs.add(Frame(graphTabs), text="Save%")
        graphTabs.bind("<<NotebookTabChanged>>", self.createGraph)

    def createGraph(self, event: Event):
        """Creates the graph for the data for the currently selected tab on the graphTab Notebook.

        Args:
            event (Event): The event object passed to the function.
        """
        # Check the trends tab was selected before continuing
        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab, "text")
        tab_frame = event.widget.nametowidget(selected_tab)

        # If graph has already been drawn do not plot it again
        if len(tab_frame.winfo_children()) > 0:
            return

        # Create the figure that will contain the graph
        fig = Figure(figsize = (10, 5), dpi = 100)

        # Get coordinates
        x = []
        y = []
        match tab_text:
            case "Shots Against":
                y = list(map(lambda game: game[1], self.games))
                x = [i+1 for i in range(len(self.games))]
            case "Goals Against":
                y = list(map(lambda game: game[2], self.games))
                x = [i+1 for i in range(len(self.games))]
            case "Saves":
                y = list(map(lambda game: game[1] - game[2], self.games))
                x = [i+1 for i in range(len(self.games))]
            case "Save%":
                y = list(map(lambda game: ((game[1] - game[2]) / game[1]), self.games))
                x = [i+1 for i in range(len(self.games))]
        
        # Plot the graph
        graph = fig.add_subplot()
        graph.plot(x, y)

        # Placing the graph in the window
        canvas = FigureCanvasTkAgg(fig, tab_frame)  
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)