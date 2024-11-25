import unittest

class TestCase8(unittest.TestCase):
    def test_error(self):
        raise ValueError("This is an intentional error")

if __name__ == "__main__":
    unittest.main()
