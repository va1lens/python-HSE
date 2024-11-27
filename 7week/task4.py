"""
https://leetcode.com/problems/max-consecutive-ones-iii/submissions/1463766684/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l: int = 0
        r: int = 0
        while r < len(nums):
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
            r += 1
        return r - l
