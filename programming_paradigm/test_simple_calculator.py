import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # -------------------------
    #       ADDITION TEST
    # -------------------------
    def test_addition(self):
        # Positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        # Negative numbers
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(-5, 3), -2)
        # Zero
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(7, 0), 7)

    # -------------------------
    #    SUBTRACTION TEST
    # -------------------------
    def test_subtraction(self):
        # Positive numbers
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        # Negative numbers
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(-3, 3), -6)
        # Zero
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(5, 0), 5)

    # -------------------------
    #    MULTIPLICATION TEST
    # -------------------------
    def test_multiplication(self):
        # Positive numbers
        self.assertEqual(self.calc.multiply(3, 4), 12)
        # Negative numbers
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -3), 9)
        # Zero
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(25, 0), 0)

    # -------------------------
    #       DIVISION TEST
    # -------------------------
    def test_division(self):
        # Positive numbers
        self.assertEqual(self.calc.divide(10, 2), 5)
        # Negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        # Floats
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        # Zero numerator
        self.assertEqual(self.calc.divide(0, 5), 0)
        # Division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

if __name__ == "__main__":
    unittest.main()
