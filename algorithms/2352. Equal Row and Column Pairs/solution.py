#https://leetcode.com/problems/equal-row-and-column-pairs/
from typing import List
import collections

class Solution:

    #O(n^3) solution
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        counter = 0
        for row in range(n):
            for col in range(n):
                if grid[row] == [grid[i][col] for i in range(n)]:
                    counter += 1

        return counter

    # O(n^2) solution
    def equalPairs_hashmap(self, grid: List[List[int]]) -> int:
        n = len(grid)
        counter = 0

        rows_counter = collections.Counter(tuple(r) for r in grid)

        for col in range(n):
            col = [grid[i][col] for i in range(n)]
            counter += rows_counter[tuple(col)]

        return counter