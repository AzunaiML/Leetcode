import unittest
from solution import Solution

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_largestAltitude(self):
        self.assertEqual(1, self.solution.largestAltitude([-5, 1, 5, 0, -7]))
        self.assertEqual(0, self.solution.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))


if __name__ == '__main__':
    unittest.main()
