import unittest

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == "__main__":
    unittest.main()

"""
Test results: The first test passed beccause the sum of the numbers is equal to 6. The second test failed
because the sum of the numbers added up to 5 instead of 6. The tests worked as expected and caught the
error in the second test.

"""
