"""
https://leetcode.com/problems/word-break/description/
?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp: list[bool] = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            for word in wordDict:
                start: int = i - len(word)
                if start >= 0 and dp[start] and s[start:i] == word:
                    dp[i] = True
                    break
        return dp[-1]
