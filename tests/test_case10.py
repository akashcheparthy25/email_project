import unittest

class TestCase10(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(2 + 2, 4)

    def test_case2(self):
        self.assertEqual(3 * 3, 10)  # This will fail

    @unittest.skip("Skipping this test")
    def test_case3(self):
        self.assertEqual(1 + 1, 3)  # This won't run

if __name__ == "__main__":
    unittest.main()
