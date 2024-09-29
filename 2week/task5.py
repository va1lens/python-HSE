"""
https://leetcode.com/problems/decode-ways/
?envType=problem-list-v2&envId=string
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        prev_count: int = 0
        curr_count: int = 1
        for i in range(len(s)):
            next_count: int = 0
            if s[i] != "0":
                next_count = curr_count
            if (
                i > 0
                and s[i - 1] != "0"
                and (s[i - 1] == "1" or (s[i - 1] == "2" and s[i] < "7"))
            ):
                next_count += prev_count
            prev_count, curr_count = curr_count, next_count
        return curr_count
