import sqlite3
from typing import Tuple

db = sqlite3.connect("data")
cu = db.cursor()
cu.execute("CREATE TABLE IF NOT EXISTS Games(name, shots)")
db.commit()

def getAllGames(fields="*"):
    return cu.execute("SELECT {0} FROM Games".format(fields))

def getGame(name: str):
    cu.execute("Select * FROM Games WHERE name = ?", (name,))
    return cu.fetchone()

def updateGame(query: str, params: Tuple[str]):
    cu.execute(query, params)
    db.commit()