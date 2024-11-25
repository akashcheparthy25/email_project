import unittest

class TestCase5(unittest.TestCase):
    def test_division(self):
        self.assertEqual(10 / 2, 5)
        self.assertEqual(10 / 2, 6)  # This will fail

if __name__ == "__main__":
    unittest.main()
