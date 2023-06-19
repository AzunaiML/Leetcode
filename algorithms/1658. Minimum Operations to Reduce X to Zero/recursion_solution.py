from typing import List

# too slow O(2^n)
class Solution:
    max_int = 10e10

    def minOperations(self, nums: List[int], x: int) -> int:
        answer = self.recursion(nums, x, 0)
        if answer == self.max_int:
            return -1
        else:
            return answer

    def recursion(self, nums: List[int], x: int, total: int):
        if x < 0:
            return self.max_int
        if x == 0:
            return total
        if len(nums) == 1:
            return self.max_int if x - nums[0] != 0 else total + 1
        else:
            total += 1
            left_x = x - nums[0]
            right_x = x - nums[-1]
            return min(self.recursion(nums[:-1], right_x, total), self.recursion(nums[1:], left_x, total))

if __name__ == '__main__':
    sol = Solution()

    x = sol.minOperations([1, 1, 4, 2, 3], 5)
    print(x)