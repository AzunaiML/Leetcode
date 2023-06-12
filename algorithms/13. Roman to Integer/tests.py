import unittest
from solution import Solution


class SolutionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_romanToInt(self):
        self.assertEqual(self.solution.romanToInt('III'), 3)
        self.assertEqual(self.solution.romanToInt('LVIII'), 58)
        self.assertEqual(self.solution.romanToInt('MCMXCIV'), 1994)


if __name__ == '__main__':
    unittest.main()
