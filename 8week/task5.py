"""
https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/submissions/1468097019/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        answer: int = 1
        for i in range(len(s)):
            j: int = i
            count: int = 0
            while j + 1 < len(s) and count <= 1:
                if s[j] == s[j + 1]:
                    count += 1
                j += 1
                if count == 2:
                    j -= 1
            answer = max(answer, j - i + 1)
        return answer
