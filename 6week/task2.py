"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l: int = 0
        current_sum: int = 0
        min_len = float("inf")
        for r in range(len(nums)):
            current_sum += nums[r]
            while current_sum >= target:
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                current_sum -= nums[l]
                l += 1
        if min_len != float("inf"):
            return min_len
        else:
            return 0
