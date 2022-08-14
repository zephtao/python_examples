import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        # Test areas when radius >= 0.
        # assertAlmostEqual: tests if the arguments are equal to 7 decimal places.
        self.assertAlmostEqual(circle_area(1), pi)
        self.assertAlmostEqual(circle_area(0), 0)
        self.assertAlmostEqual(circle_area(2.1), pi * 2.1**2)

    def test_values(self):
        # Make sure value errors are raised when necessary.
        # assertRaises: checks that an exception is made.
        # Arguments: (1) exception to raise, (2) a function, (3, etc.) arguments to the function.
        self.assertRaises(ValueError, circle_area, -2)

    def test_types(self):
        # Make sure type errors are raised when necessary.
        self.assertRaises(TypeError, circle_area, 3+5j) # Complex number
        self.assertRaises(TypeError, circle_area, True) # Boolean
        self.assertRaises(TypeError, circle_area, "radius") # String

# To run this test in the terminal:
# python -m unittest 28_test_circles
# OR python -m unittest (Python will search for tests to run)