#https://leetcode.com/problems/climbing-stairs/description/

class Solution:
    def climbStairs(selfself, n: int) -> int:
        if n == 1:
            return 1
        else:
            a, b = 0, 1
            for i in range(2, n+1):
                a, b = b, a + b
            return a + b