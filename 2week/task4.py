"""
https://leetcode.com/problems/edit-distance/
?envType=problem-list-v2&envId=string
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        matrix = [[0 for i in range(len(word2) + 1)] for j in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            matrix[i][0] = i
        for j in range(len(word2) + 1):
            matrix[0][j] = j
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1]
                else:
                    matrix[i][j] = min(
                        matrix[i][j - 1] + 1,
                        matrix[i - 1][j] + 1,
                        matrix[i - 1][j - 1] + 1,
                    )
        return matrix[len(word1)][len(word2)]
