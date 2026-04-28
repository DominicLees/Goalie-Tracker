import unittest
from components.main import Main
from entities.game import Game

class TestMainMethods(unittest.TestCase):

    def testValidateShots(self):
        main = Main(None)
        main.game = Game("test")

        # Test valid inputs
        self.assertTrue(main.validateShots(""))
        self.assertTrue(main.validateShots("0"))
        self.assertTrue(main.validateShots("10"))
        self.assertTrue(main.validateShots("999"))

        # Test Invalid inputs
        self.assertFalse(main.validateShots("Hello World"))
        self.assertFalse(main.validateShots("-1"))
        self.assertFalse(main.validateShots("1."))
        self.assertFalse(main.validateShots("1000"))

    def testValidateGoals(self):
        main = Main(None)
        main.game = Game("test")

        # Test valid inputs
        self.assertTrue(main.validateGoals(""))
        self.assertTrue(main.validateGoals("0"))
        self.assertTrue(main.validateGoals("10"))
        self.assertTrue(main.validateGoals("999"))

        # Test Invalid inputs
        self.assertFalse(main.validateGoals("Hello World"))
        self.assertFalse(main.validateGoals("-1"))
        self.assertFalse(main.validateGoals("1."))
        self.assertFalse(main.validateGoals("1000"))