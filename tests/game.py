import unittest
from entities.game import Game

class TestGameMethods(unittest.TestCase):
    
    def testStr(self):
        game = Game("test")
        self.assertEqual(str(game), "test")

    def testGetSaves(self):
        game = Game("test")
        self.assertEqual(game.getSaves(), 0)

        game.shots = 10
        self.assertEqual(game.getSaves(), 10)

        game.goals = 5
        self.assertEqual(game.getSaves(), 5)

        game.goals = 11
        self.assertEqual(game.getSaves(), 0)

    def testGetSavePct(self):
        game = Game("test")
        self.assertEqual(game.getSavePct(), 0)

        game.shots = 10
        self.assertEqual(game.getSavePct(), 1.0)

        game.goals = 5
        self.assertEqual(game.getSavePct(), 0.5)

        game.goals = 11
        self.assertEqual(game.getSavePct(), -0.1)