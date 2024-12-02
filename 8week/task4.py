"""
https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/submissions/1468091101/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def maximumBeauty(self, nums: list[int], k: int) -> int:
        nums.sort()
        l: int = 0
        answer: int = 0
        for r in range(len(nums)):
            while nums[r] - nums[l] > 2 * k:
                l += 1
            answer = max(answer, r - l + 1)
        return answer
