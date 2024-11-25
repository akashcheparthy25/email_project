import unittest

class TestCase9(unittest.TestCase):
    def test_exception(self):
        with self.assertRaises(ValueError):
            raise ValueError("Intentional ValueError")

if __name__ == "__main__":
    unittest.main()
