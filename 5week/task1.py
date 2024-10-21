"""
https://leetcode.com/problems/set-matrix-zeroes/description/
?envType=problem-list-v2&envId=hash-table
"""


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        count_rows: int = len(matrix)
        count_columns: int = len(matrix[0])
        coordinates_zeros: list[list[int]] = []
        for i in range(count_rows):
            for j in range(count_columns):
                if matrix[i][j] == 0:
                    coordinates_zeros.append([i, j])
        for coordinates in coordinates_zeros:
            for i in range(count_rows):
                matrix[i][coordinates[1]] = 0
            for j in range(count_columns):
                matrix[coordinates[0]][j] = 0
