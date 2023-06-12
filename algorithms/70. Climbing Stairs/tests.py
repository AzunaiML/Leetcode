import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_something(self):
        self.assertEqual(self.solution.climbStairs(2), 2)
        self.assertEqual(self.solution.climbStairs(3), 3)
        self.assertEqual(self.solution.climbStairs(4), 5)
        self.assertEqual(self.solution.climbStairs(5), 8)


if __name__ == '__main__':
    unittest.main()
