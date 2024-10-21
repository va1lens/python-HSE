"""
https://leetcode.com/problems/repeated-dna-sequences/description/
?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) <= 10:
            return []
        set_s1: set[str] = set()
        set_s2: set[str] = set()
        for i in range(len(s) - 9):
            s_i = s[i : i + 10]
            if s_i in set_s1:
                set_s2.add(s_i)
            else:
                set_s1.add(s_i)
        return list(set_s2)
