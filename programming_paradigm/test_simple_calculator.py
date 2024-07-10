import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test class for SimpleCalculator operations."""
    def setUp(self):
         """Set up the SimpleCalculator instance before each test."""
         self.calc = SimpleCalculator()
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(2, -3), -1)
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 2),3)
        self.assertEqual(self.calc.subtract(-3, -2),-1)
        self.assertEqual(self.calc.subtract(-3, 2),-5)
    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(5, 2),10)
        self.assertEqual(self.calc.multiply(-3, -2),6)
        self.assertEqual(self.calc.multiply(-3, 2),-6)
        self.assertEqual(self.calc.multiply(3, -1),-3)
        self.assertEqual(self.calc.multiply(0, 2),0)
    def test_division(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 2),3)
        self.assertEqual(self.calc.divide(-6, 2),-3)
        self.assertEqual(self.calc.divide(5, 2),2.5)
        self.assertEqual(self.calc.divide(5.5, 2),2.75)
        self.assertRaises(ZeroDivisionError), self.calc.divide, (10, 0)

if __name__ == "__main__":
    unittest.main()