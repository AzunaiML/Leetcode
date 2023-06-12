import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_containsDuplicate(self):
        self.assertEqual(self.solution.containsDuplicate([1, 2, 3, 1]), True)
        self.assertEqual(self.solution.containsDuplicate([1, 2, 3, 4]), False)
        self.assertEqual(self.solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True)


if __name__ == '__main__':
    unittest.main()
