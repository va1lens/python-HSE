"""
https://leetcode.com/problems/longest-consecutive-sequence/description/
?envType=problem-list-v2&envId=array
"""


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        current_consecutive_sequence: int = 1
        longest_consecutive_sequence: int = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    current_consecutive_sequence += 1
                else:
                    longest_consecutive_sequence = max(
                        longest_consecutive_sequence, current_consecutive_sequence
                    )
                    current_consecutive_sequence = 1
