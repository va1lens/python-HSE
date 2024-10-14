"""
https://leetcode.com/problems/search-a-2d-matrix-ii/description/
?envType=problem-list-v2&envId=array
"""


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m: int = len(matrix)
        n: int = len(matrix[0])
        i: int = 0
        j: int = n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
