import unittest
from solution import Solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_findMedianSortedArrays(self):
        self.assertEqual(2.0, self.solution.findMedianSortedArrays([1, 3], [2]))
        self.assertEqual(2.5, self.solution.findMedianSortedArrays([1, 2], [3, 4]))


if __name__ == '__main__':
    unittest.main()
