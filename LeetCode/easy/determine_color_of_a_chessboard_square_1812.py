"""
1812. Determine Color of a Chessboard Square
https://leetcode.com/problems/determine-color-of-a-chessboard-square
"""


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        coords_tuple = (8 - int(coordinates[1]), ord(coordinates[0]) - 97)
        return True if coords_tuple[0] % 2 == coords_tuple[1] % 2 else False
