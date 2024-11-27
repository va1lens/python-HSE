"""
https://leetcode.com/problems/permutation-in-string/submissions/1463761139/
?envType=problem-list-v2&envId=sliding-window
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1_counts: list[int] = [0] * 26
        s2_counts: list[int] = [0] * 26
        for i in range(len(s1)):
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i]) - 97] += 1
        if s1_counts == s2_counts:
            return True
        for i in range(len(s1), len(s2)):
            s2_counts[ord(s2[i]) - 97] += 1
            s2_counts[ord(s2[i - len(s1)]) - ord("a")] -= 1
            if s1_counts == s2_counts:
                return True
        return False
