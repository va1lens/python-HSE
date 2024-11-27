"""
https://leetcode.com/problems/longest-repeating-character-replacement/submissions/1463755557/
?envType=problem-list-v2&envId=sliding-window
"""

import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans: int = 0
        l: int = 0
        counts: collections.defaultdict[int] = collections.defaultdict(int)
        for r in range(len(s)):
            counts[s[r]] += 1
            if r - l + 1 - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
