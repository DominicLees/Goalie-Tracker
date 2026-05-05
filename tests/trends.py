import unittest
from components.trends import average, total

class TestTrendsMethods(unittest.TestCase):

    def testAverage(self):
        data = []
        self.assertEqual(average(data, 0), 0)

        data = [("0", 10, 0), ("1", 20, 0)]
        self.assertEqual(average(data, 1), 15)

        data = [("0", -20, -20), ("1", 0, 20)]
        self.assertEqual(average(data, 1), -10)
        self.assertEqual(average(data, 2), 0)

    def testTotal(self):
        data = []
        self.assertEqual(total(data, 0), 0)

        data = [("0", 10, 0), ("1", 10, 0)]
        self.assertEqual(total(data, 1), 20)

        data = [("0", 0, -10), ("1", 0, 0)]
        self.assertEqual(total(data, 2), -10)