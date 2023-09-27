"""
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/
"""


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_stack = [[] for i in range(9)]
        block_stack = [[] for i in range(9)]
        for row in range(9):
            row_stack = []
            for col in range(9):
                block = (row // 3) * 3 + col // 3
                item = board[row][col]
                if item != '.':
                    if item in row_stack or item in col_stack[col] or item in block_stack[block]:
                        return False
                    else:
                        row_stack.append(item)
                        col_stack[col].append(item)
                        block_stack[block].append(item)
        return True
