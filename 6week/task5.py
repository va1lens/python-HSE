"""
https://leetcode.com/problems/minimum-window-substring/description/
?envType=problem-list-v2&envId=sliding-window
"""

import collections
import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d: collections.defaultdict[int] = collections.defaultdict(int)
        l: int = 0
        res: list[int] = [0, sys.maxsize]
        cur_size: int = 0
        for char in t:
            d[char] += 1
        for r, cur_char in enumerate(s):
            if cur_char in d:
                d[cur_char] -= 1
                if d[cur_char] == 0:
                    cur_size += 1
            while cur_size == len(d):
                cur_len = r - l
                prev_len = res[1] - res[0]
                if cur_len < prev_len:
                    res[0] = l
                    res[1] = r
                l_char: str = s[l]
                if l_char in d:
                    if d[l_char] == 0:
                        cur_size -= 1
                    d[l_char] += 1
                l += 1
        if res[1] == sys.maxsize:
            return ""
        return s[res[0] : res[1] + 1]
