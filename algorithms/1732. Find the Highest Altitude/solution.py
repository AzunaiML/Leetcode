from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current = 0
        max_val = 0
        for g in gain:
            current += g
            if current > max_val:
                max_val = current

        return max_val