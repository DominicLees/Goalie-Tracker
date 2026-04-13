import sqlite3
from typing import Tuple
from entities.game import Game

db = sqlite3.connect("data")
cu = db.cursor()
cu.execute("""CREATE TABLE IF NOT EXISTS Games(
    name, 
    shots DEFAULT 0
)""")
db.commit()

def getAllGames(fields="*"):
    return cu.execute("SELECT {0} FROM Games".format(fields))

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
        cu.execute("INSERT INTO Games(name, shots) VALUES (?, 0)", (name,))
        db.commit()
        return True
    except:
        return False

def updateGame(game: Game) -> bool:
    try:
        cu.execute("UPDATE Games SET shots = ? WHERE name = ?", (game.shots, game.name))
        db.commit()
        return True
    except Exception as e:
        print(e)
        return False