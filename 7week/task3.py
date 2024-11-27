"""
https://leetcode.com/problems/maximum-length-of-repeated-subarray/submissions/1463764944/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def findLength(self, nums1: list[int], nums2: list[int]) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        ans: int = 0
        for i in range(1, len(nums1) + 1):
            for j in range(1, len(nums2) + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    ans = max(ans, dp[i][j])
        return ans
