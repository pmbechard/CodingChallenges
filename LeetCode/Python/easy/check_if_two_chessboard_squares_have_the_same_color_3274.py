"""
3274. Check if Two Chessboard Squares Have the Same Color
https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/
"""


class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        coord1 = ord(coordinate1[0]) % 2 == int(coordinate1[1]) % 2
        coord2 = ord(coordinate2[0]) % 2 == int(coordinate2[1]) % 2
        return coord1 == coord2
