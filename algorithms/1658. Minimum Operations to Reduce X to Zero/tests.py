import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_something(self):
        self.assertEqual(2, self.solution.minOperations([1, 1, 4, 2, 3], 5))
        self.assertEqual(-1, self.solution.minOperations([5, 6, 7, 8, 9], 4))
        self.assertEqual(5, self.solution.minOperations([3, 2, 20, 1, 1, 3], 10))
        self.assertEqual(-1, self.solution.minOperations([3], 10))
        self.assertEqual(1, self.solution.minOperations([3], 3))


if __name__ == '__main__':
    unittest.main()
