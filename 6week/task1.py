"""
https://leetcode.com/problems/longest-turbulent-subarray/description/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        inc: int = 1
        dec: int = 1
        res: int = 1
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                dec = inc + 1
                inc = 1
            elif arr[i] > arr[i - 1]:
                inc = dec + 1
                dec = 1
            else:
                inc = 1
                dec = 1
            res = max(res, inc, dec)
        return res
