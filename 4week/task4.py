"""
https://leetcode.com/problems/h-index/description/
?envType=problem-list-v2&envId=array
"""


class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        for i, v in enumerate(citations):
            if len(citations) - i <= v:
                return len(citations) - i
        return 0
