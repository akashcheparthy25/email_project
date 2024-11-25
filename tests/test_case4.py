import unittest

class TestCase4(unittest.TestCase):
    def test_multiple(self):
        self.assertEqual(1 + 1, 2)
        self.assertTrue(5 > 1)
        self.assertFalse(2 < 1)

if __name__ == "__main__":
    unittest.main()
