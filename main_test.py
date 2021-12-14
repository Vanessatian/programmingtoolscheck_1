import unittest
from main import print_hi_stephen, print_hi_you, print_hi_Meredith


class MyTestCase(unittest.TestCase):
    def test_print_hi_stephen(self):
        self.assertEqual(print_hi_stephen(), f"Hi, Stephen")

    def test_print_hi_you(self):
        self.assertEqual(print_hi_you(), f"Hi, Vanessa")

    def test_print_hi_Meredith(self):
        self.assertEqual(print_hi_Meredith(), f"Hi, Meredith")


if __name__ == '__main__':
    unittest.main()
