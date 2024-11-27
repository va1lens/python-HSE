"""
https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/submissions/1463773666/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        max_count: int = 0
        counter: int = 0
        l: int = 0
        for r in range(len(s)):
            counter += 1 if s[r] in vowels else 0
            if r - l + 1 > k:
                counter -= 1 if s[l] in vowels else 0
                l += 1
            max_count = max(max_count, counter)
        return max_count
