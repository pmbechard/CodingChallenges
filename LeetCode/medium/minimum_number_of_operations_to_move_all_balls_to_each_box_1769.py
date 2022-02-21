"""
1769. Minimum Number of Operations to Move All Balls to Each Box
https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
"""


class Solution:
    def minOperations(self, boxes):
        current_box = 0
        moves = []
        while True:
            current_moves = 0
            for i in range(len(boxes)):
                if boxes[i] != '0' and i != current_box:
                    current_moves += abs(i - current_box)
            current_box += 1
            moves.append(current_moves)
            if len(moves) == len(boxes):
                break
        return moves
