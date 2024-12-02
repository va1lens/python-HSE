"""
https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        max_n: int = max(nums)
        max_count: int = 0
        answer: int = 0
        l: int = 0
        for r in range(len(nums)):
            if nums[r] == max_n:
                max_count += 1
            while max_count == k:
                if nums[l] == max_n:
                    max_count -= 1
                l += 1
            answer += l
        return answer
