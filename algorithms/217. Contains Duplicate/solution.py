from typing import  List
#https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        saw_nums = {}
        for i in nums:
            if i in saw_nums:
                return True
            else:
                saw_nums[i] = 1
        return False