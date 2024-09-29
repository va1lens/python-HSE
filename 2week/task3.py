"""
https://leetcode.com/problems/generate-parentheses/
?envType=problem-list-v2&envId=string
"""


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def generate(open: int, close: int, s: str):
            if open == n and close == n:
                result.append(s)
                return
            if open < n:
                generate(open + 1, close, s + "(")
            if close < open:
                generate(open, close + 1, s + ")")

        generate(0, 0, "")
        return result
