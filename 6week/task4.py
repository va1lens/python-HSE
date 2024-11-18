"""
https://leetcode.com/problems/subarray-product-less-than-k/description/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        count: int = 0
        l: int = 0
        r: int = 0
        if k <= 1:
            return 0
        p: int = 1
        while r < len(nums):
            p *= nums[r]
            while p >= k:
                p //= nums[l]
                l += 1
            count += r - l + 1
            r += 1
        return count
