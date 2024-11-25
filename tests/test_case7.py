import unittest

class TestCase7(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(3 + 4, 7)

    @unittest.skip("Test skipped intentionally")
    def test_case2(self):
        self.assertEqual(2 + 2, 5)

if __name__ == "__main__":
    unittest.main()
