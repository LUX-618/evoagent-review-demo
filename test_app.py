import unittest

from app import calculate


class CalculateTests(unittest.TestCase):
    def test_numeric_input(self):
        self.assertEqual(calculate("3.5"), 3.5)

    def test_negative_input(self):
        self.assertEqual(calculate("-2"), -2.0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate("not-a-number")


if __name__ == "__main__":
    unittest.main()
