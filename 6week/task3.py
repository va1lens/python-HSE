"""
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_len = 0
        freq: list[int] = [0] * 26
        for i in range(len(s)):
            for m in range(26):
                freq[m] = 0
            for j in range(i, len(s)):
                freq[ord(s[j]) - ord("a")] += 1
                flag: bool = True
                for q in range(26):
                    if freq[q] != 0 and freq[q] < k:
                        flag = False
                        break
                if flag:
                    max_len = max(max_len, j - i + 1)
        return max_len
