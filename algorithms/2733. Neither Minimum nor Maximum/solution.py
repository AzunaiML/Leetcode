from typing import List

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return -1
        else:
            min_index = 0
            max_index = 0
            for i in range(n):
                if nums[i] > nums[max_index]:
                    max_index = i
                if nums[i] < nums[min_index]:
                    min_index = i

            if max_index + 1 < n and max_index + 1 != min_index:
                return nums[max_index + 1]
            elif max_index - 1 > -1 and max_index - 1 != min_index:
                return nums[max_index - 1]
            elif min_index + 1 < n and min_index + 1 != max_index:
                return nums[min_index + 1]
            elif min_index - 1 > -1 and min_index - 1 != max_index:
                return nums[min_index - 1]


    def findNonMinOrMax_2(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return -1
        else:
            x = y = z = 0
            for n in nums:
                if n > x:
                    x, y, z = n, x, y
                elif n > y:
                    y, z = n, y
                elif n > z:
                    z = n
                if x > y > z != 0:
                    return y