import unittest

class TestCase2(unittest.TestCase):
    def test_subtraction(self):
        self.assertEqual(5 - 3, 3)  # This will fail

if __name__ == "__main__":
    unittest.main()
