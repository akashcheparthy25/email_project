import unittest

class TestCase6(unittest.TestCase):
    @unittest.skipIf(True, "Condition met, skipping this test")
    def test_conditionally_skipped(self):
        self.assertEqual(1 + 1, 2)

if __name__ == "__main__":
    unittest.main()
