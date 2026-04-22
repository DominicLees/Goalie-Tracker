import sqlite3
from entities.game import Game

# Create database file if it does not exist
db = sqlite3.connect("data")
cu = db.cursor()
cu.execute("""CREATE TABLE IF NOT EXISTS Games(
    name, 
    shots DEFAULT 0,
    goals DEFAULT 0
)""")
db.commit()

# TODO: docstrings
def getAllGames(fields="*"):
    return cu.execute("SELECT {0} FROM Games".format(fields)).fetchall()

def getGame(name: str) -> Game | None:
    cu.execute("Select * FROM Games WHERE name = ?", (name,))
    result = cu.fetchone()
    if result == None:
        return None
    return Game(result)

def insertNewGame(name: str) -> bool:
    if getGame(name) != None:
        return False
    try:
        cu.execute("INSERT INTO Games(name) VALUES (?)", (name,))
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False

def updateGame(game: Game) -> bool:
    try:
        cu.execute("UPDATE Games SET shots = ?, goals = ? WHERE name = ?", (game.shots, game.goals, game.name))
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def updateGameName(oldName: str, newName: str) -> bool:
    try:
        cu.execute("UPDATE Games SET name = ? WHERE name = ?", (newName, oldName))
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False