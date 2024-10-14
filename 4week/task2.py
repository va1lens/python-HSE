"""
https://leetcode.com/problems/valid-sudoku/description/
?envType=problem-list-v2&envId=array
"""


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows: list[set[str]] = [set() for i in range(9)]
        cols: list[set[str]] = [set() for i in range(9)]
        squares: list[set[str]] = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if (
                    board[i][j] in rows[i]
                    or board[i][j] in cols[j]
                    or board[i][j] in squares[(i // 3) * 3 + (j // 3)]
                ):
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i // 3) * 3 + (j // 3)].add(board[i][j])
        return True
