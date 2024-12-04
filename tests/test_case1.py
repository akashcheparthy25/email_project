import unittest

class TestCase1(unittest.TestCase):
    def test_addition(self):
        self.asserEqual(2+2,4)


if __name__ == "__main__":
    unittest.main()
