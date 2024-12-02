"""
https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/submissions/1468073081/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count: list[int] = [0, 0, 0]
        for c in s:
            count[ord(c) - ord("a")] += 1
        if min(count) < k:
            return -1
        answer: float = float("inf")
        l: int = 0
        for r in range(len(s)):
            count[ord(s[r]) - ord("a")] -= 1
            while min(count) < k:
                count[ord(s[l]) - ord("a")] += 1
                l += 1
            answer = min(answer, len(s) - r + l - 1)
        return answer
