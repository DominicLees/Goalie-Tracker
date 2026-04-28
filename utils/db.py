import sqlite3
from typing import Tuple
from entities.game import Game
import logging

type GameRecords = list[Tuple[str, int, int]]

logger = logging.getLogger(__name__)

# Create database file if it does not exist
db = sqlite3.connect("data")
cu = db.cursor()
cu.execute("""CREATE TABLE IF NOT EXISTS Games(
    name, 
    shots DEFAULT 0,
    goals DEFAULT 0
)""")
db.commit()

# Database functions

def getAllGames(fields="*") -> GameRecords:
    """Retrieves all games from the database.

    Args:
        fields (str, optional): Which fields to get. Defaults to "*".

    Returns:
        GameRecords: Returns all records in a list of tuples.
    """
    logger.info("Retrieving '{0}' fields for all game records".format(fields))
    try:
        return cu.execute("SELECT {0} FROM Games".format(fields)).fetchall()
    except Exception as e:
        logger.exception(e)


def getGame(name: str) -> Game | None:
    """Retrieves a game from the database from its name

    Args:
        name (str): The name of the game to retrieve

    Returns:
        Game | None: If the game was found returns a Game object, otherwise returns None
    """
    logger.info("Retrieving '{0}' from Games table".format(name))
    cu.execute("Select * FROM Games WHERE name = ?", (name,))
    result = cu.fetchone()
    if result == None:
        return None
    return Game(result)

def insertNewGame(name: str) -> bool:
    """Inserts a new game with the provided name into the database

    Args:
        name (str): The value of the name field to be inserted

    Returns:
        bool: True if insert was successful, otherwise false
    """
    logger.info("Inserting '{0}' into Games table".format(name))
    if getGame(name) != None:
        logger.debug("'{0}' already exists in Games table")
        return False
    try:
        cu.execute("INSERT INTO Games(name) VALUES (?)", (name,))
        db.commit()
        return True
    except Exception as e:
        logger.exception(e)
        return False

def updateGame(game: Game) -> bool:
    """Takes a game object and updates the corresponding record in the database to match the current values.

    Args:
        game (Game): Game instance to update the database with. A game record with the same name must already exist in the database.

    Returns:
        bool: True if update was successful, otherwise false
    """
    logger.info("Updating '{0}' in Games table".format(game.name))
    try:
        cu.execute("UPDATE Games SET shots = ?, goals = ? WHERE name = ?", (game.shots, game.goals, game.name))
        db.commit()
        return True
    except Exception as e:
        logger.exception(e)
        return False
    
def updateGameName(oldName: str, newName: str) -> bool:
    """Changes the name of a game record in the database

    Args:
        oldName (str): The name of the record in the database
        newName (str): The value to change the game's name to

    Returns:
        bool: True if update was successful, otherwise false
    """
    logger.info("Changing '{0}' name to '{1}' in Games table".format(oldName, newName))
    try:
        cu.execute("UPDATE Games SET name = ? WHERE name = ?", (newName, oldName))
        db.commit()
        return True
    except Exception as e:
        logger.exception(e)
        return False
    
def deleteGame(name: str) -> bool:
    """Deletes game from the database.

    Args:
        name (str): The name of the game in the database to delete

    Returns:
        bool: True if delete was successful, otherwise false
    """
    logger.info("Deleting '{0}' from Games table".format(name))
    try:
        cu.execute("DELETE FROM Games WHERE name = ?", (name,))
        db.commit()
        return True
    except Exception as e:
        logger.exception(e)
        return False