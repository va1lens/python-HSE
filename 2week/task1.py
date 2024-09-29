"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
?envType=problem-list-v2&envId=string
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length: int = 0
        left: int = 0
        set_char: set[str] = set()
        for right in range(len(s)):
            if s[right] not in set_char:
                set_char.add(s[right])
                max_length = max(max_length, right - left + 1)
            else:
                while s[right] in set_char:
                    set_char.remove(s[left])
                    left += 1
                set_char.add(s[right])
        return max_length
