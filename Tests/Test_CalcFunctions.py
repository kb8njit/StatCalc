import unittest
import math
from CalcFunctions.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsNone(self.calculator, Calculator)
