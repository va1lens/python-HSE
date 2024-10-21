"""
https://leetcode.com/problems/group-anagrams/description/
?envType=problem-list-v2&envId=hash-table
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d: defaultdict[list] = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            d[sorted_word].append(word)
        return list(d.values())
