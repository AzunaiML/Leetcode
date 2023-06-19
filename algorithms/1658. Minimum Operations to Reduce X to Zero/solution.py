from typing import List


class Solution:

    def minOperations(self, nums: List[int], x: int) -> int:
        target, size, win_sum, j = sum(nums) - x, -1, 0, -1,
        for i, num in enumerate(nums):
            win_sum += num
            while j + 1 < len(nums) and win_sum > target:
                j += 1
                win_sum -= nums[j]
            if win_sum == target:
                size = max(size, i - j)
        return -1 if size < 0 else len(nums) - size




if __name__ == '__main__':
    sol = Solution()

    x = sol.minOperations([1, 1, 4, 2, 3], 5)
    print(x)