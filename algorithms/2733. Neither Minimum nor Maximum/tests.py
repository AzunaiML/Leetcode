import unittest
from solution import Solution

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_something(self):
        self.assertIn(self.solution.findNonMinOrMax_2([3, 2, 1, 4]), [2, 3])
        self.assertIn(self.solution.findNonMinOrMax_2([1, 2]), [-1])
        self.assertIn(self.solution.findNonMinOrMax_2([3, 2, 1, 5, 4]), [2, 3, 4])


if __name__ == '__main__':
    unittest.main()
