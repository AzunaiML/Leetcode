import unittest
import Solution

class SolutionTests(unittest.TestCase):

    def setUp(self):
        self.solution = Solution.Solution()

    def test_reverseBits(self):
        self.assertEqual(self.solution.reverseBits(43261596), 964176192)

        self.assertEqual(self.solution.reverseBits(4294967293), 3221225471)

        self.assertEqual(self.solution.reverseBits(0), 0)

if __name__ == '__main__':
    unittest.main()
