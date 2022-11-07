# importing the built-in Python unittest module
import unittest

# importing the class that we want to test as a module
# this is just a user defined module! i.e. calculator is calculator.py :))
import calculator as CalculatorScript

# defining a class for testing the Calculator class
class testCalculator(unittest.TestCase):
    # testCalculator class is a child class of unittest.TestCase class
    calc = CalculatorScript.Calculator()    # instantiating an instance of the Calculator class defined in calculator.py

    # unit tests for checking that calculator accepts 1, 2, 3 numbers
    def test_OneInt(self):
        self.assertEqual(self.calc.addNumbers(6), 6)

    def test_TwoInts(self):
        self.assertEqual(self.calc.addNumbers(3,5), 8)

    def test_ThreeInts(self):
        self.assertEqual(self.calc.addNumbers(100,12,-60), 52)

    # unit test for checking that calculator only accepts integers
    def test_Floats(self):
        with self.assertRaises(Exception):
            self.calc.addNumbers(12.345,6,2.76093)

    # unit test for checking that calculator does not accept non-numeric inputs
    def test_NonNumerals(self):
        with self.assertRaises(Exception):
            self.calc.addNumbers(12,6,"three")

    # unit test for checking that calculator accepts no inputs and returns 0
    def test_NoInput(self):
        self.assertEqual(self.calc.addNumbers(), 0)

    # unit test for checking that calculator does not accept numbers > 100
    def test_IsOver100(self):
        with self.assertRaises(Exception):
            self.calc.addNumbers(12,171,67)

# every test definition must start with a test_ prefix to be recognized by the unittest module
