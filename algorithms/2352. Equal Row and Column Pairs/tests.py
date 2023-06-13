import unittest
from solution import  Solution

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.solution = Solution()

    def test_something(self):
        self.assertEqual(1, self.solution.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
        self.assertEqual(3, self.solution.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))

        self.assertEqual(1, self.solution.equalPairs_hashmap([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
        self.assertEqual(3, self.solution.equalPairs_hashmap([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))


if __name__ == '__main__':
    unittest.main()
