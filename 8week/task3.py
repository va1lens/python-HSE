"""
https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        answer: list[int] = []
        l: int = 0
        count: int = 1
        for r in range(len(nums)):
            if r > 0 and nums[r - 1] + 1 == nums[r]:
                count += 1
            if r - l + 1 > k:
                if nums[l] + 1 == nums[l + 1]:
                    count -= 1
                l += 1
            if r - l + 1 == k:
                if count == k:
                    answer.append(nums[r])
                else:
                    answer.append(-1)
        return answer
