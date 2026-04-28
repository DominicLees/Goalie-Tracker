import unittest
from components.trends import average

class TestTrendsMethods(unittest.TestCase):

    def testAverage(self):
        data = []
        self.assertEqual(average(data, 0), 0)

        data = [("0", 0, 0), ("1", 10, 20)]
        self.assertEqual(average(data, 1), 5)
        self.assertEqual(average(data, 2), 10)