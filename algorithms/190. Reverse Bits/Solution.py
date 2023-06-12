# https://leetcode.com/problems/reverse-bits/
import unittest

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32): # The input must be a binary string of length 32
            result = (result << 1)
            result |= n & 1
            n >>= 1
        return result

