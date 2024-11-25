import unittest

class TestCase3(unittest.TestCase):
    @unittest.skip("Skipping this test for demonstration")
    def test_multiplication(self):
        self.assertEqual(3 * 3, 9)

if __name__ == "__main__":
    unittest.main()
