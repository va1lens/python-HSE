"""
https://leetcode.com/problems/largest-number/description/
?envType=problem-list-v2&envId=array
"""

import functools


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def compare(a: str, b: str):
            if a + b > b + a:
                return -1
            else:
                return 1

        nums_str: list[str] = list(map(str, nums))
        nums_str.sort(key=functools.cmp_to_key(compare))
        largest: str = "".join(nums_str)
        if largest[0] == "0":
            return "0"
        return largest
